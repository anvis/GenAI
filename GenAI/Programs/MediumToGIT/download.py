import feedparser

def fetch_medium_urls(username):
    feed_url = f"https://medium.com/feed/@{username}"
    feed = feedparser.parse(feed_url)
    return [entry.link for entry in feed.entries]

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

def extract_markdown(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    article = soup.find('article')
    if article:
        return md(str(article))
    return None

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

def extract_markdown(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    article = soup.find('article')
    if article:
        return md(str(article))
    return None

def tag_metadata(entry):
    title = entry.title
    date = entry.published
    tags = [tag.term for tag in entry.tags] if 'tags' in entry else []
    return f"# {title}\n\n**Published:** {date}\n**Tags:** {', '.join(tags)}\n\n"

import os

def save_to_repo(markdown, title, folder="medium-archive"):
    os.makedirs(folder, exist_ok=True)
    filename = f"{folder}/{title.replace(' ', '_')}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown)


def archive_medium(username):
    feed = feedparser.parse(f"https://medium.com/feed/@anveshgouds")
    for entry in feed.entries:
        url = entry.link
        md_content = extract_markdown(url)
        if md_content:
            metadata = tag_metadata(entry)
            full_md = metadata + md_content
            save_to_repo(full_md, entry.title)