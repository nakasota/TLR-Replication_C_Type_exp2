#!/usr/bin/env python3
"""
Clean Proposals for Embedding

Reads all Markdown files in
  data/preprocess/accepted_proposals/cleaned_evaluable_proposals/
and writes cleaned versions (with headings, comment separators,
hyperlinks stripped, stopwords removed, tokens stemmed, <a> tags removed,
and blank lines removed) to
  data/preprocess/accepted_proposals/cleaned_evaluable_proposals_for_embedding/
preserving the original files.
"""

import re
import sys
from pathlib import Path
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Try to load stopwords; if missing, instruct user to install them manually.
try:
    STOP_WORDS = set(stopwords.words('english'))
except LookupError:
    print("❗ NLTK stopwords not found. Please run:", file=sys.stderr)
    print("    python -c \"import nltk; nltk.download('stopwords')\"", file=sys.stderr)
    sys.exit(1)

STEMMER = PorterStemmer()

def clean_markdown(text: str) -> str:
    """
    - Remove lines that are headings or comment separators
    - Strip Markdown links [text](url) → text
    - Strip raw URLs
    - Remove <a>...</a> tags
    - Remove stopwords outside of ```code``` blocks
    - Stem remaining tokens outside of code blocks
    - Treat <pre>...</pre> as natural text (not code), removing the tags
    - Remove all blank lines (except ``` fences)
    """
    heading_re  = re.compile(r"^=+\s*\[.*?\]\s*=+\s*$")
    comment_re  = re.compile(r"^---\s*Comment\s*#\d+\s*by\s+.*?---\s*$")
    md_link_re  = re.compile(r"\[([^\]]+)\]\([^)]+\)")
    url_re      = re.compile(r"https?://\S+")

    cleaned_lines = []
    in_code = False

    for line in text.splitlines():
        # toggle code-block state on ``` fences
        if line.strip().startswith("```"):
            in_code = not in_code
            cleaned_lines.append(line)
            continue

        # remove blank lines everywhere
        if not line.strip():
            continue

        if in_code:
            # leave non-blank code-block lines untouched
            cleaned_lines.append(line)
            continue

        # outside code blocks: strip <pre> tags so content inside is processed as text
        line = line.replace('<pre>', '').replace('</pre>', '')
        # then remove HTML anchor tags
        line = re.sub(r'</?a\b[^>]*>', '', line)

        # drop headings/comments
        if heading_re.match(line) or comment_re.match(line):
            continue

        # strip markdown links & raw URLs
        line = md_link_re.sub(r"\1", line)
        line = url_re.sub("", line)

        # tokenize, remove stopwords, then stem
        tokens = line.split()
        processed = []
        for tok in tokens:
            lower = tok.lower()
            if lower in STOP_WORDS:
                continue
            stemmed = STEMMER.stem(tok)
            processed.append(stemmed)
        cleaned_lines.append(" ".join(processed))

    result = "\n".join(cleaned_lines)
    # preserve trailing newline
    if text.endswith("\n"):
        result += "\n"
    return result

def main():
    base    = Path(__file__).parent.parent
    src_dir = base / 'data' / 'preprocess' / 'accepted_proposals' / 'cleaned_evaluable_proposals_content_validated'
    dst_dir = base / 'data' / 'preprocess' / 'accepted_proposals' / 'cleaned_evaluable_proposals_for_embedding_content_validated'

    if not src_dir.is_dir():
        print(f"❌ Source directory not found: {src_dir}", file=sys.stderr)
        sys.exit(1)
    dst_dir.mkdir(parents=True, exist_ok=True)

    md_files = sorted(src_dir.glob('*.md'))
    if not md_files:
        print(f"⚠️  No markdown files found in {src_dir}")
        return

    print(f"🧹 Cleaning {len(md_files)} files for embedding...")
    for md in md_files:
        text    = md.read_text(encoding='utf-8')
        cleaned = clean_markdown(text)
        out     = dst_dir / md.name
        out.write_text(cleaned, encoding='utf-8')
        print(f"  ✅ {md.name}")

    print(f"\n🎉 All cleaned files written to {dst_dir}")

if __name__ == '__main__':
    main()
