# -*- coding: utf-8 -*-
"""
get board member names for each member company


future functionality:
    add titles
    scrape committees
    refactor to use selenium for static and dynamic
    
@author: ktayfour
"""


from bs4 import BeautifulSoup
from selenium import webdriver
from urls import URLS
from concurrent.futures import ThreadPoolExecutor, TimeoutError
import CleanerFunctions as clnr


class Company:
    def __init__(self, companyName: str, soupLocation: dict, soup_cleaner = None):
        
        #initializations
        self.companyName = companyName
        self.soupLocation = soupLocation
        if soup_cleaner:
            self.soup_cleaner = soup_cleaner

    def scrape_website(self):        
        soup = self.dynamic_scraper()
        names = self.default_cleaner(soup)
        return names          
                
    def default_cleaner(self, soup):
        contents = soup.find_all(self.soupLocation[1],self.soupLocation[2])
        values = [content.text.strip() for content in contents]
        names = {self.companyName : values }
        return names
    
    def dynamic_scraper(self):
        url = self.soupLocation[0] # soupLocation = [url, html-tag, {class = class-tag}]    
        def scraper_func(url):
            try:
                driver = webdriver.Chrome()
                driver.get(url)
                driver.implicitly_wait(10)
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
    

    
    

    
def initialize_company_objects():
    my_objects = {}
    count_of_companies_initialized = 0
    count_of_companies_not_initialized = 0
    count_of_companies = len(URLS)
    
    for key, value in URLS.items():
        if "error_message" in value:
            print(URLS[key]['error_message'])
            count_of_companies_not_initialized += 1
        else:
            if not isinstance(key, str):
                print(key)
                raise TypeError(f"company_name must be a string.")
            if not isinstance(URLS[value], dict):
                print(f"no souplocation in URLS[{self.companyName}]:")
                print('''looking for dictionary: {["url", "html-tag", {"class" : "class-tag"}]}''')
                
            else:
                soupLocation = value["location"]
                companyName = key
                if callable(value['function']):
                    soup_cleaner = value['function']
                    my_objects[companyName] = Company(companyName, soupLocation, soup_cleaner)
                else:
                    my_objects[companyName] = Company(companyName, soupLocation)
                count_of_companies_initialized += 1
    print("")
    print(f"un-initialized companies: {count_of_companies_not_initialized}")
    print(f"initialized companies: {count_of_companies_initialized}")
    print(f"total companies tried: {count_of_companies}")
    return my_objects


    
