"""Keep the homepage's public collection synchronized with the reviewed catalog."""
import json
import re
from html import escape
from pathlib import Path

root = Path(__file__).resolve().parents[1]
catalog = json.loads((root / 'projects/catalog.json').read_text())
projects = catalog['projects']
assert all(row.get('repo') != 'fractalnomia' for row in projects), 'Private source must not be included in the public catalog'
start = '/* SMS_PUBLIC_CATALOG_START */'
end = '/* SMS_PUBLIC_CATALOG_END */'
page = root / 'assets/homepage/homepage.js'
text = page.read_text()
assert text.count(start) == text.count(end) == 1, 'Homepage catalog markers are missing or duplicated'
a = text.index(start)
b = text.index(end, a) + len(end)
payload = start + '\nconst projects = ' + json.dumps(projects, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + ';\n' + end
page.write_text(text[:a] + payload + text[b:])
print(f'Synchronized {len(projects)} public entries into the homepage')

# Render the no-JavaScript directory from the same reviewed entries.
categories = dict.fromkeys(row['category'] for row in projects)
sections = []
for category in categories:
    cards = []
    for row in projects:
        if row['category'] != category:
            continue
        links = []
        if row.get('url'):
            label = 'Read the working manual' if row.get('repo') == 'sms-standards' else 'View prototype' if row['status'] == 'Prototype' else 'Explore project'
            links.append(f'<a href="{escape(row["url"], quote=True)}">{label} ↗</a>')
        links.append(f'<a href="{escape(row["repository"], quote=True)}">Repository ↗</a>')
        steward = f'<p class="steward">Project steward: {escape(row["steward"])}</p>' if row.get('steward') else ''
        cards.append(f'<article data-project id="project-{escape(row["slug"], quote=True)}"><span class="status">{escape(row["status"])}</span><h3>{escape(row["title"])}</h3><p>{escape(row["description"])}</p>{steward}<div class="links">{"".join(links)}</div></article>')
    anchor = re.sub(r'[^a-z0-9]+', '-', category.lower()).strip('-')
    sections.append(f'<section data-category id="{anchor}"><h2>{escape(category)}</h2><div class="grid">{"".join(cards)}</div></section>')
directory = root / 'projects/index.html'
text = directory.read_text()
start = '<div id="collection">'
end = '</div><p id="empty"'
a = text.index(start) + len(start)
b = text.index(end, a)
text = text[:a] + ''.join(sections) + text[b:]
repo_count = sum(bool(row.get('repo')) for row in projects)
text = re.sub(r'(<p id="count"[^>]*>).*?(</p>)', lambda m: m[1] + f'{len(projects)} entries · {repo_count} public repositories and Hart, in Motion' + m[2], text, count=1)
directory.write_text(text)
print(f'Synchronized {len(projects)} public entries into the project directory')
