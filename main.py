import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage to scrape
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Make an HTTP GET request to the URL and store the response in a variable
response = requests.get(URL)
website_html = response.text

# Create a BeautifulSoup object to parse the HTML content of the webpage
soup = BeautifulSoup(website_html, "html.parser")

# Find all the elements with the "h3" tag and "title" class, which contain the movie titles
all_movies = soup.find_all(name="h3", class_="title")

# Extract the text from each of the "h3" elements and store them in a list
movie_titles = [movies.getText() for movies in all_movies]

# Reverse the order of the movie titles
movies = movie_titles[::-1]

# Open a file named "movies.txt" in write mode and set the encoding to utf-8
with open("movies.txt", mode="w", encoding="utf-8") as file:
    # Write each movie title to the file with a newline character
    for movie in movies:
        file.write(f"{movie}\n")



