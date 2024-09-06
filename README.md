# Rate My Professor Scraper

## Description

The **Rate My Professor Scraper** is a Python-based program that extracts professor ratings and reviews from the Rate My Professor website. This scraper collects data such as professor names, overall ratings, difficulty levels, and individual reviews, and outputs it into a structured format like CSV or JSON for further analysis.

## Features

- Scrapes professor names, ratings, difficulty scores, and student comments.
- Supports searching by university and department.
- Outputs data in CSV or JSON format.
- Simple command-line interface for ease of use.
- Handles pagination and multiple pages of reviews.
- Handles rate-limiting and errors gracefully.

## Requirements

- Python 3.x
- Required Python packages:
  - `requests`
  - `beautifulsoup4`
  - `pandas` (for CSV output)
  - `json` (for JSON output)

To install the required Python packages, run:
```bash
pip install -r requirements.txt
