import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


def scrape_books():
    try:
        url = "https://books.toscrape.com"

        response = requests.get(url, timeout=10)
        response.encoding = "utf-8"

        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article")
        books_data = []

        for book in books:
            title = book.find("h3")
            link = title.find("a")

            price = book.find("p", class_="price_color")

            rating = book.find("p", class_="star-rating")

            availability = book.find("p", class_="instock availability")

            book_data = {
                "Title": link["title"],
                "Price": price.text.strip(),
                "Rating": rating["class"][1],
                "Availability": availability.text.strip()
            }

            books_data.append(book_data)

        return books_data

    except Exception as e:
        print("Error:", e)
        return []


def main():
    books = scrape_books()

    if books:
        df = pd.DataFrame(books)

        print(df.head())

        output_file = os.path.join(os.path.dirname(__file__), "books.csv")
        df.to_csv(output_file, index=False)

        print("\nCSV file created successfully!")

    else:
        print("No data was scraped.")


if __name__ == "__main__":
    main()