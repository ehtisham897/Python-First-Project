import requests
from bs4 import BeautifulSoup
import csv

# Website URL that we want to scrape:
url = 'http://books.toscrape.com'

# Send a GET request to the website:
response = requests.get(url)

# Check if the request was successful (status code 200):
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the book items:
    books = soup.find_all('article', class_='product_pod')

    # List to store the product details:
    book_list = []

    # Loop through each book and extract title, price, and rating:
    for book in books:
        title = book.find('h3').find('a')['title']  # Book title
        price = book.find('p', class_='price_color').text.strip()  # Book price
        
        # Find rating
        rating_element = book.find('p', class_='star-rating')
        rating_classes = rating_element.get('class')  # Example: ['star-rating', 'Three']
        if len(rating_classes) > 1:
            rating = rating_classes[1]  # 'One', 'Two', 'Three', etc.
        else:
            rating = 'Not Rated'

        # Add book data to the list
        book_list.append([title, price, rating])

    # Save the data to a CSV file
    with open('books.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Book Title', 'Price', 'Rating'])  # Write the header
        writer.writerows(book_list)  # Write book data

    print("Data successfully saved to 'books.csv'.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
