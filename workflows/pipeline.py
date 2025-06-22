import os
from scraping.scrapper import fetch_chapter
from agents.writer import spin_chapter
from agents.reviewer import review_chapter
from agents.human_loop import manual_review
from versioning.chromadb import save_version
from versioning.chromadb import search_similar_rl as search_similar


def ensure_dir(file_path: str):
    directory = os.path.dirname(file_path)
    os.makedirs(directory, exist_ok=True)

def run_pipeline(url: str, chapter_id: str):
    raw, img = fetch_chapter(url)

    screenshot_path = "out/screenshot.png"
    ensure_dir(screenshot_path)
    with open(screenshot_path, "wb") as f:
        f.write(img)

    spun = spin_chapter(raw)
    human = manual_review(spun)
    reviewed = review_chapter(human)

    save_version(chapter_id, reviewed, {"source": url})
    print("✅ Saved version:", chapter_id)

    sims = search_similar(spun)
    print("📚 Similar content snippet:", sims[:200])
