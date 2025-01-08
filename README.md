# Web Crawler and Database Integration Project

This project is a comprehensive web crawler and database integration system designed to scrape, process, and store links from the Open Canada website. It monitors new documents uploaded on the site, stores the data in a MongoDB database, and sends email notifications for new updates.This project is part of my contribution to the The Investigative Journalism Foundation (IJF), showcasing my commitment to open data initiatives and transparency.https://theijf.org/open-by-default-contributors

---

## Features

- **Web Crawling**: Scrapes document links from the Open Canada website using `requests` and `BeautifulSoup`.
- **Database Operations**: Integrates with MongoDB to store and manage scraped data.
- **Change Detection**: Identifies new links by comparing current data with previously scraped links.
- **Email Notifications**: Sends email updates when new links are detected.
- **Data Export**: Creates a DataFrame of new links for further analysis.

---

## Project Structure

### 1. `WebCrawler.py`
Contains the core functionality for scraping the Open Canada website:
- **`get_latest_documents()`**: Scrapes document links from multiple pages.
- **`read_previous_links()`**: Reads previously stored links from a file.
- **`write_new_links()`**: Appends new links to the file.
- **`send_email()`**: Sends an email with the list of new links.

### 2. `database_operations.py`
Handles database operations using MongoDB:
- **`link_exists()`**: Checks if a link already exists in the database.
- **`insert_links_to_database()`**: Inserts new links into the MongoDB collection.
- **`create_dataframe()`**: Converts new links into a Pandas DataFrame.
- **`process_crawler_data()`**: Processes the data by fetching new links, storing them, and sending notifications.

### 3. `main.py`
The entry point of the project:
- Configures the database and collection.
- Fetches the latest links and processes them.
- Handles exception management and ensures proper closure of database connections.

---

## Prerequisites

1. Python 3.x
2. MongoDB installed and running locally.
3. Required Python libraries:
   - `pymongo`
   - `pandas`
   - `beautifulsoup4`
   - `requests`
   - `smtplib` (built-in)

Install dependencies using:
```bash
pip install pymongo pandas beautifulsoup4 requests
