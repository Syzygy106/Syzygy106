import os, re, html, pathlib, sys, urllib.request, feedparser

USERNAME = os.environ.get("MEDIUM_USERNAME", "").lstrip("@")
LIMIT = int(os.environ.get("MAX_POSTS", "5"))
README_PATH = pathlib.Path("README.md")

if not USERNAME:
    print("ERROR: Set MEDIUM_USERNAME env variable.", file=sys.stderr)
    sys.exit(1)

FEED_URL = f"https://medium.com/feed/@{USERNAME}"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

# --- fetch with UA (Medium 403 workaround) ---
try:
    req = urllib.request.Request(FEED_URL, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
except Exception as e:
    print(f"ERROR: fetching Medium feed: {e}", file=sys.stderr)
    sys.exit(1)

# --- parse feed ---
d = feedparser.parse(data)
if getattr(d, "bozo", 0):
    print(f"WARNING: feed parse issue: {getattr(d, 'bozo_exception', '')}", file=sys.stderr)

entries = d.entries[:LIMIT]
if not entries:
    block = "- _No recent posts found._"
else:
    rows = []
    for e in entries:
        title = html.unescape(getattr(e, "title", "Untitled"))
        link = getattr(e, "link", "")
        date = getattr(e, "published", getattr(e, "updated", ""))[:16]  # YYYY-MM-DD HH:MM
        rows.append(f"- [{title}]({link}) <sub>· {date}</sub>")
    block = "\n".join(rows)

# --- read/validate README markers ---
readme_text = README_PATH.read_text(encoding="utf-8")
if "<!-- MEDIUM:START -->" not in readme_text or "<!-- MEDIUM:END -->" not in readme_text:
    print("ERROR: README markers <!-- MEDIUM:START/END --> not found.", file=sys.stderr)
    sys.exit(1)

# --- replace block ---
new_text = re.sub(
    r"(<!-- MEDIUM:START -->)(.*?)(<!-- MEDIUM:END -->)",
    r"\1\n" + block + r"\n\3",
    readme_text,
    flags=re.S,
)

if new_text != readme_text:
    README_PATH.write_text(new_text, encoding="utf-8")
    print("README updated.")
else:
    print("No changes.")


