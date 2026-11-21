"""Check the reviewed public catalog; optionally compare it with GitHub's public inventory."""
import argparse
import json
import os
from pathlib import Path
import urllib.request

parser = argparse.ArgumentParser()
parser.add_argument('--live', action='store_true')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
projects = json.loads((root / 'projects/catalog.json').read_text())['projects']
repos = [row['repo'] for row in projects if row.get('repo')]
slugs = [row['slug'] for row in projects]
assert len(repos) == len(set(repos)), 'Duplicate repository entries'
assert len(slugs) == len(set(slugs)), 'Duplicate project anchors'
for row in projects:
    assert row['title'] and row['description'] and row['status'] and row['category']
    assert row.get('url') is None or row['url'].startswith('https://')
    if row.get('repo'):
        assert row['repository'] == 'https://github.com/Simple-Minds-Studios/' + row['repo']
assert {'the-anonymous-family', 'still-here'} <= set(repos), 'Family-history exhibits are missing'
if args.live:
    actual = set()
    page = 1
    while True:
        url = f'https://api.github.com/orgs/Simple-Minds-Studios/repos?type=public&per_page=100&page={page}'
        headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'SMS-public-catalog-check'}
        if os.environ.get('GH_TOKEN'):
            headers['Authorization'] = 'Bearer ' + os.environ['GH_TOKEN']
        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.load(response)
        actual.update(repo['name'] for repo in result if not repo['private'])
        if len(result) < 100:
            break
        page += 1
    missing = actual - set(repos)
    stale = set(repos) - actual
    if missing or stale:
        raise SystemExit(f'Public catalog differs from GitHub. Missing: {sorted(missing)}; stale: {sorted(stale)}')
    print(f'GitHub comparison passed: all {len(actual)} public repositories are represented')
print(f'Catalog validated: {len(projects)} entries, including both family-history exhibits')
