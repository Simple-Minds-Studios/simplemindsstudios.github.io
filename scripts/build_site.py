"""Build the tracked public website for a Pages project path or custom domain."""
import argparse
from pathlib import Path
import re
import shutil
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--base-path", default="")
parser.add_argument("--output", default="_site")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
out = (root / args.output).resolve()
if out == root or root not in out.parents:
    raise SystemExit("Output must be a subdirectory of this repository")
files = subprocess.check_output(["git", "ls-files", "-z"], cwd=root).decode().split("\0")
files = [f for f in files if f and not f.startswith((".git", "scripts/", "_site/")) and f != "CNAME"]
base = "/" + args.base_path.strip("/") + "/" if args.base_path.strip("/") else "/"
roots = {f.split("/")[0] for f in files}
pattern = re.compile(r"([\"'])/(" + "|".join(re.escape(x) for x in sorted(roots, key=len, reverse=True)) + r")(?=[/\"'?#])")
if out.exists():
    shutil.rmtree(out)
for name in files:
    src = root / name
    dst = out / name
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    if base != "/" and src.suffix in (".html", ".js", ".css"):
        text = dst.read_text()
        text = pattern.sub(lambda m: m.group(1) + base + m.group(2), text)
        text = text.replace('href="/"', 'href="' + base + '"').replace("href='/'", "href='" + base + "'")
        text = re.sub(r"url\(/(?!/)", "url(" + base, text)
        dst.write_text(text)
assert (out / "index.html").stat().st_size > 0
assert not (out / "CNAME").exists()
print(f"Built {len(files)} files at base path {base}")
