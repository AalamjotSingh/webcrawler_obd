import datetime
import pandas as pd
from pymongo import MongoClient
from datetime import datetime

from WebCrawler import get_latest_documents, send_email, write_new_links

class DatabaseOperations:
    def __init__(self, database_name, collection_name):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def link_exists(self, link):
        """Check if a link already exists in the database."""
        count = self.collection.count_documents({"link": link})
        return count > 0        

    def insert_link(self, link, date_scraped):
        link_document = {
            "link": link,
            "dateScraped": date_scraped
        }
        self.collection.insert_one(link_document)

    def insert_links_to_database(self, links):
        current_time_utc = datetime.utcnow()
        for link in links:
            self.insert_link(link, current_time_utc)

    def create_dataframe(self, links):
        current_time_utc = datetime.utcnow()
        data = {
            "link": links,
            "dateScraped": [current_time_utc] * len(links)
        }
        df = pd.DataFrame(data)
        return df

    def process_crawler_data(self):
        current_links = get_latest_documents()
        print("Current Links:")
        print(current_links)

        # Load previous links from MongoDB
        previous_links = set(self.collection.distinct("link"))

        if not current_links:
            print("Failed to fetch latest documents.")
            return

        new_links = [link for link in current_links if link not in previous_links]

        # If there are new links, send an email, store them in MongoDB, and append to the file
        if new_links:
            send_email(new_links)

            # Insert new links into MongoDB
            self.insert_links_to_database(new_links)

            # Append new links to the file
            write_new_links("previous_links.txt", new_links)

            # Create DataFrame for new links
            new_links_df = self.create_dataframe(new_links)
            print("DataFrame for new links:")
            print(new_links_df)