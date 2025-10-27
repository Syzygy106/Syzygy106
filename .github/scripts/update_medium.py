import feedparser, re, os, html
from datetime import datetime


MEDIUM_USERNAME = os.environ.get('MEDIUM_USERNAME', '').lstrip('@')
MAX_POSTS = int(os.environ.get('MAX_POSTS', '5'))
FEED_URL = f'https://medium.com/feed/@{MEDIUM_USERNAME}'


if not MEDIUM_USERNAME:
    raise SystemExit('Set MEDIUM_USERNAME env variable.')


feed = feedparser.parse(FEED_URL)
items = []
for e in feed.entries[:MAX_POSTS]:
    title = html.unescape(e.title)
    link = e.link
    date = getattr(e, 'published', '')[:16]
    items.append(f"- [{title}]({link}) <sub>· {date}</sub>")


block = "\n".join(items) if items else "- _No recent posts found._"


with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()


pattern = re.compile(r"(<!-- MEDIUM:START -->)(.*?)(<!-- MEDIUM:END -->)", re.S)
new = re.sub(pattern, r"\1\n" + block + r"\n\3", readme)


with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new)


