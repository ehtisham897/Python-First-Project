..This Project Title:
Web Scraping and Data Processing: Books Website Price, Rating, and Title Extraction.
..Short Summary About the Project:
In this project, I developed a Python script to scrape book data (Title, Price, and Rating) from a live website (books.toscrape.com).
The extracted data was first saved into a CSV file and then converted into an Excel (.xlsx) file using another Python script.
This project demonstrates my skills in web scraping (BeautifulSoup, Requests) and data handling (Pandas).
..Tools and Libraries We Used:
Python

Requests (HTTP library)

BeautifulSoup (Web scraping)

CSV Module (Data export)

Pandas (CSV to Excel conversion)

Openpyxl (Excel writing engine)

..This is My Step-by-Step Work Methods:
1. I selected books.toscrape.com for scraping, a website designed for web scraping practice.
2. Data Extraction Script:
Include:
Fetched the webpage using requests library.

Parsed the HTML content using BeautifulSoup.

Extracted Book Title, Price, and Rating.

Stored the data into a CSV file (books.csv).

3. Data Conversion Script:
This include:
Read the CSV file using pandas.

Converted the CSV data into an Excel (.xlsx) file (books.xlsx).
4. Final Outcome:
A clean and structured Excel file containing the list of books, their prices, and ratings