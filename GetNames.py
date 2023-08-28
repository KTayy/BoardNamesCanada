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

# create class 
class Company:
# what to pass into soup.find_all https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all   
# soupLocation = [url, html-tag, {class = class-tag}]     
    def __init__(self, companyName: str, soup_cleaner): 
        
         
        if not isinstance(companyName, str):
            raise TypeError("company_name must be a string.")
        else: 
            self.companyName = companyName
        
        
        if not isinstance(URLS[self.companyName], dict):
            raise TypeError(f"no souplocation in URLS[{self.companyName}] - it should be a dictionary\n[url, html-tag, {{class = class-tag}}]")
            
        elif "location" in URLS[self.companyName]:
            self.soupLocation = URLS[self.companyName]["location"]
            self.soup_cleaner = soup_cleaner
            print(f"{self.companyName} - souplocation initialized")
        
                
    
    def dynamic_scraper(self):
        url = self.soupLocation[0]
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
    
    def scrape_website(self):        
        soup = self.dynamic_scraper()
        names = self.soup_cleaner(self,soup)
        return names
    
    
# initialze classes:
    # create Company object instances with a cleanup attribute for each company
    # company_name = Company("name", name_clean_soup) ; 
    # where name is in URLS[Keys] and
    # name_clean_soup is in URLS[Keys]['function']
    
def initialize_company_objects():
    my_objects = {}
    count_of_companies_initialized = 0
    count_of_companies = len(URLS)
    
    for key, value in URLS.items():
        companyName = key
        soup_cleaner = clnr.
 #       if "function" in value:
 #           soup_cleaner = value["function"]
#            my_objects[companyName] = Company(companyName, soup_cleaner)
#            count_of_companies_initialized += 1
#        else:
#            print(f"{key} has no board URL to check")
    print(f"initialized companies: {count_of_companies_initialized}")
    print(f"total companies tried: {count_of_companies}")
    return my_objects


    
