import pandas as pd
import matplotlib.pyplot as plt
import os

csv_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Task2_EDA",
    "cleaned_books.csv"
)

df = pd.read_csv(csv_path)
charts_folder = os.path.join(
    os.path.dirname(__file__),
    "charts"
)
rating_counts = df["Rating"].value_counts()

plt.figure(figsize=(8, 5))

rating_counts.plot(kind="bar")

plt.title("Number of Books by Rating")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.tight_layout()

plt.savefig(os.path.join(charts_folder, "ratings_bar_chart.png"))

plt.show()

plt.figure(figsize=(8, 5))

plt.hist(df["Price"], bins=5)

plt.title("Distribution of Book Prices")
plt.xlabel("Price")
plt.ylabel("Number of Books")

plt.tight_layout()

plt.savefig(os.path.join(charts_folder, "price_histogram.png"))

plt.show()

availability_counts = df["Availability"].value_counts()

plt.figure(figsize=(6, 6))

plt.pie(
    availability_counts,
    labels=availability_counts.index,
    autopct="%1.1f%%"
)

plt.title("Book Availability")

plt.savefig(os.path.join(charts_folder, "availability_pie_chart.png"))

plt.show()