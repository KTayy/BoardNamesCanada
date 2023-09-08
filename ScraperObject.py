# -*- coding: utf-8 -*-
"""
get board member names for each member company


future functionality:
    add titles
    scrape committees
    refactor to use selenium for static and dynamic
    
@author: ktayfour
"""

import ast
import openai
from bs4 import BeautifulSoup
from selenium import webdriver
from LocationDatabase import DATABASE
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from key import KEY


openai.api_key = KEY

class Company_Scraper:

    """
    A class that scrapes and cleans board pages for each company.
    
    Attributes:
    - companyName (str): Name of the company to scrape.
    - soupLocation (dict): HTML tag location of board members stored in LocationDatabase.
    """
    
    countScraperErrors = 0  
    
    @classmethod
    def count_scraper_Errors(cls):
        cls.countScraperErrors += 1
        print(f"number of errors encountered {cls.countScraperErrors}")
        
    def __init__(self, companyName: str, soupLocation: dict):
        """Initializes the scraper with company name and location."""
        
        self.companyName = companyName 
        self.soupLocation = soupLocation    # html tag location of board members stored in LocationDatabase


    def scrape_website(self):  
        """
        Scrapes the website and returns cleaned content.
        
        Returns:
            dict: Cleaned content from the website.
        """
        try:
            soup = self.dynamic_scraper()
            soup_cleaned = self.default_cleaner(soup)
            content = self.ai_cleaner(soup_cleaned)
        except Exception as e:
            print(f"An error occurred for {self.companyName}: {e}")
            return {self.companyName : f"{e}" }
        return content
    
    
    def ai_cleaner(self, soup):
                
        """
        Uses OpenAI's GPT-3.5 model to clean the scraped data.
        
        Args:
            soup (BeautifulSoup): Scraped content from the website.
        
        Returns:
            dict: Cleaned names from the provided soup.
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You will be provided with unstructured data, and your task is to find the full names within it and return it in list format."
                    },
                    {
                        "role": "user",
                        "content": str(soup[self.companyName])
                    }
                ],
                temperature=0,
                max_tokens=256
            )
        except Exception as e:
            print(f"An error occurred for {self.companyName}: {e}")
            return {self.companyName : "error in parsing"}
            
        try:
            values = ast.literal_eval(response["choices"][0]["message"]["content"])
        except (ValueError, SyntaxError):
            print(f"The provided string for {self.companyName} is not a valid Python literal. ")
            return {self.companyName : "null" }
        names = {self.companyName : values }
        return names
            
        
    def default_cleaner(self, soup):
        
        """
        Cleans the provided soup using default cleaning logic.
        
        Args:
            soup (BeautifulSoup): Scraped content from the website.
        
        Returns:
            dict: Cleaned names from the provided soup.
        """
        contents = soup.find_all(self.soupLocation[1],self.soupLocation[2])
        values = [content.text.strip() for content in contents]
        names = {self.companyName : values }
        return names
    
    
    def dynamic_scraper(self):

        """
        Uses a dynamic scraping method to fetch the content from the website.
        
        Returns:
            BeautifulSoup: Scraped content from the website.
        """

        url = self.soupLocation[0] # soupLocation = [url, html-tag, {class = class-tag}]    
        def scraper_func(url):
            try:
                driver = webdriver.Chrome()
                print("driver on")
                driver.get(url)
                print("got url")
                driver.implicitly_wait(10)
                print("waited")
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                driver.quit()
                return soup, None
            except Exception as e:
                return None, str(e)
        with ThreadPoolExecutor() as executor:
            future = executor.submit(scraper_func, url)
            try:
                result, error_message = future.result(timeout=30)  # Timeout set to 30 seconds
            except TimeoutError:
                executor.shutdown(wait=False)
                result, error_message = None, "Timeout occurred."
        if error_message:
            print(f"An error occurred: {error_message}")
        return result
    
    def get_iframes_info(self):
        """
        Get information about iframes present in the given web page.
        
        Parameters:
        - driver: The web driver instance.
        
        Returns:
        - A list of names or ids of the iframes.
        """
        driver = self.soupLocation[0]
        # Find all iframes on the page
        iframes = driver.find_elements_by_tag_name('iframe')
        
        # Print the number of iframes
        print(f"Number of iframes: {len(iframes)}")
        
        # Collect attributes of each iframe (like 'name' or 'id')
        iframe_attributes = []
        for iframe in iframes:
            attr = iframe.get_attribute('name') or iframe.get_attribute('id')
            iframe_attributes.append(attr)
            print(attr)
        
        return iframe_attributes
    
    

    
def initialize_company_scrapers():
    
    """
    Initializes company scraper objects for each company in the DATABASE.
    
    Returns:
        dict: Dictionary of initialized scraper objects.
    """

    my_objects = {}
    count_of_companies_initialized = 0
    count_of_companies_not_initialized = 0
    count_of_companies = len(DATABASE)
    
    for key, value in DATABASE.items():
        if "error_message" in value:
            print(DATABASE[key]['error_message'])
            count_of_companies_not_initialized += 1
        else:
            if not isinstance(key, str):
                raise TypeError(f"{key} company_name must be a string.")
            if not isinstance(value, dict):
                print("no souplocation in DATABASE[{self.companyName}]:")
                print('''looking for dictionary: {["url", "html-tag", {"class" : "class-tag"}]}''')    
                
            else:
                soupLocation = value["location"]
                companyName = key
                
                my_objects[companyName] = Company_Scraper(companyName = companyName, soupLocation = soupLocation)
                count_of_companies_initialized += 1
    print("")
    print(f"un-initialized companies: {count_of_companies_not_initialized}")
    print(f"initialized companies: {count_of_companies_initialized}")
    print(f"total companies tried: {count_of_companies}")
    return my_objects


    
