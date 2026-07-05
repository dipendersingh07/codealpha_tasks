# Book Web Scraper

A Python project that scrapes book information from the Books to Scrape website and exports it to a CSV file.

## Features
- Extracts Book Title
- Extracts Price
- Extracts Rating
- Extracts Availability
- Saves data to a CSV file

## Technologies Used
- Python
- Requests
- BeautifulSoup4
- Pandas

## Files
- scraper.py
- books.csv
- requirements.txt

## How to Run

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Run the program

```bash
python scraper.py
```

## Output

A CSV file named **books.csv** is created containing:

- Title
- Price
- Rating
- Availability