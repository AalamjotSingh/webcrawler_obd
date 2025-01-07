from WebCrawler import get_latest_documents, send_email, read_previous_links, write_new_links
from database_operations import DatabaseOperations

def main():
    # MongoDB database and collection names
    database_name = 'LinksDB'
    collection_name = 'links'

    # Create an instance of DatabaseOperations
    db_operations = DatabaseOperations(database_name=database_name, collection_name=collection_name)

    try:
        # Get the latest documents from Webcrawler
        current_links = set(get_latest_documents())

        # Load previous links from previous_links file
        previous_links = read_previous_links("previous_links.txt")

        if not current_links:
            print("Failed to fetch latest documents.")
            return

        current_links = {f'https://open.canada.ca{link}' for link in current_links}

        # creating a new set containing elements that are present in current_links but not in previous_links. 
        new_links = current_links - previous_links

        # If there are new links, send an email and store them
        if new_links:
            send_email(list(new_links))
            full_links = [f"https://open.canada.ca{link}" for link in new_links]

            db_operations.insert_links_to_database(new_links)

            # Appending new links to the file
            print("-----------------------main function in main.py writing file----------------------------------")
            write_new_links("previous_links.txt", list(new_links))

            # Creating DataFrame for new links 
            new_links_df = db_operations.create_dataframe(list(new_links))
            print("DataFrame for new link main.py:")
            print(new_links_df)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Closing MongoDB connection
        db_operations.client.close()

if __name__ == "__main__":
    main()