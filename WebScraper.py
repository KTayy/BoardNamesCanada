import csv
import ScraperObject as scrapers
from datetime import date


# Assuming the necessary imports and initializations have been done at the beginning of the script

def _scrape_board_members_debug(initialized_objects, limit=None):
    """
    Scrapes the board members for a limited number of companies.
    
    Args:
        initialized_objects (dict): Dictionary of initialized scraper objects.
        limit (int, optional): Number of companies to scrape. useful when debugging.
        
    Returns:
        dict: Dictionary containing company names as keys and board members as values.
    """
    board_members = {}
    
    # Iterating over a subset of initialized objects based on the provided limit
    for key in list(initialized_objects.keys())[:limit]:
        print("\n" + "="*10 + "\n")
        print(key)
        
        member_board = initialized_objects[key].scrape_website()
        board_members.update(member_board)
        
        print(member_board)
        print("\n" + "="*10 + "\n")
    
    return board_members

def scrape_board_members(initialized_objects):
    """
    Scrapes the board members using scraper objects
    
    Args:
        initialized_objects (dict): Dictionary of initialized scraper objects.

        
    Returns:
        dict: Dictionary containing company names as keys and board members as values.
    """
    board_members = {}
    i = 0
    
    for key in list(initialized_objects.keys()):
        i += 1
        print("\n" + "="*10 + "\n")
        print(i,": ", key)
        
        member_board = initialized_objects[key].scrape_website()
        board_members.update(member_board)
        
        print(member_board)
        print("\n" + "="*10 + "\n")
    
    return board_members

def export_to_csv(board_members, filename_prefix):
    """
    Exports the scraped board members to a CSV file.
    
    Args:
        board_members (dict): Dictionary containing board members data.
        filename_prefix (str): Prefix for the CSV filename.
        
    Returns:
        str: Filename of the exported CSV.
    """
    # Prepare data for export
    prepared_data = [(company, person) for company, persons in board_members.items() for person in persons]
    
    # Exporting to CSV using a comma as the delimiter
    csv_filename_updated = f"{filename_prefix}.csv"
    with open(csv_filename_updated, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')  # Using comma as delimiter
        writer.writerow(["Company", "Name"])  # writing the headers
        for row in prepared_data:
            writer.writerow(row)
    
    return csv_filename_updated

# Initialize company scrapers
initialized_objects = scrapers.initialize_company_scrapers()

# Scrape board members for a subset of companies
board_members = scrape_board_members(initialized_objects)

# Export the scraped data to a CSV file
filename_prefix = date.today().strftime('%Y-%m-%d') + "_member_boards"
csv_file = export_to_csv(board_members, filename_prefix)

print(csv_file)
