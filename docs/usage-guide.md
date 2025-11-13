# Usage Guide

This document describes how to run the Truth Social Comment Scraper locally.

## Installation

```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

Basic Usage
From the repository root:
bashpython src/main.py --post "https://truthsocial.com/@IStandWithTrump47/113943538543524813"

By default, this will:

Fetch comments (replies) for the given post.

Clean the content into plain text if --clean-content is provided.

Export the dataset as JSON into data/comments.json.

Common Options

--limit N – Maximum number of comments to collect.

--sort {newest,oldest,popular} – Sorting strategy applied to comments.

--language en – Filter by language. Comma-separated list for multiple languages.

--min-replies, --min-reblogs, --min-favourites – Filter by minimum engagement.

--format {json,csv} – Output format.

--output PATH – Output file path.

Example:
bashpython src/main.py \
  --post "https://truthsocial.com/@SomeUser/1234567890" \
  --limit 500 \
  --sort popular \
  --language en \
  --min-favourites 10 \
  --clean-content \
  --format csv \