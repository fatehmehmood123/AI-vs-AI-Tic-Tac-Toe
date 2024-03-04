import requests  # To fetch website content
from bs4 import BeautifulSoup  # Example library for parsing HTML

# Website URL and target article URL
website_url = "https://medium.com"
article_url = "https://medium.com/p/3fe6b455de67"

# Fetch website content
response = requests.get(article_url)

# Parse HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find data elements based on your website structure
# Example: Find all paragraphs within the article content
data = soup.find_all("p")

# Extract and store data
with open("scraped_data.txt", "w") as file:
    for paragraph in data:
        text = paragraph.text.strip()  # Extract and clean text
        file.write(text + "\n")  # Write to text file with newline

print("Data scraped and stored in scraped_data.txt!")
