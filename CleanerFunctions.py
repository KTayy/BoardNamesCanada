import re
from bs4 import BeautifulSoup
# subclass function for cleanup specific to each company.
# require : soup from beautiful soup
# PC: return a dictionary names {company: [values]} where values has the cleaned up board directors

def scotiabank_clean_soup(self, soup):
    def extract_names(text):
        potential_names = []
        lines = text.split("\n")
        for line in lines:
            # Removing any unwanted details and special characters
            line = re.sub(r'View details', '', line, flags=re.IGNORECASE)
            line = re.sub(r'\(.*?\)', '', line)
            line = line.strip()

            # Filtering for potential names
            if len(line.split()) <= 4 and not any(char.isdigit() for char in line):
                potential_names.append(line)
        return potential_names

    names = []
    for chunk in soup[self.companyName]:
        names.extend(extract_names(chunk))

    # Filter out empty names or names that don't seem valid
    refined_names = [name for name in names if name and len(name.split()) > 1]

    # Removing duplicates and filtering out non-names
    refined_names = list(set(refined_names))
    refined_names = [name for name in refined_names if not any(word in name.lower() for word in ["includes", "shares"])]

    return {self.companyName: refined_names}



def nbc_clean_soup(self,soup):   
    data = soup[self.companyName]
    names_raw = re.findall(r'([\w\s\.-]+)\s*Elected', data[0])
    names_cleaned = [name.replace('\n', ' ').strip() for name in names_raw]
    names = {self.companyName: names_cleaned}
    return names


def opb_clean_soup(self,soup):
    data = soup[self.companyName]
    pattern = re.compile(r'^(.*?)(?=\n\t+\w)')
    names = []
    
    for item in data:
        match = pattern.search(item)
        if match:
            names.append(match.group(1).strip())
    names = {self.companyName: names}
    return names


def imco_clean_soup(self,soup):
    data = soup[self.companyName]
    names = [' '.join(name.split()) for name in data]
    names = {self.companyName: names}
    return names


def bmo_clean_soup(self,soup):
    print(soup)
    # values = []
    # names = {self.companyName : values }
    # return names




def aig_clean_soup(self, soup):
    print(soup)


def bdc_clean_soup(self,soup):
    print(soup)


def canadalife_clean_soup(self,soup):
    print(soup)



def upp_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names


#################### ^^^^^^ done ^^^^^^ ################################





def cibc_clean_soup(self,soup):
    print(soup)
    # values = []
    # # # for content in soup:
    # #     #do something
    
    # # names = {self.companyName:[content.text for content in soup]}
    # return names




    
    
    
    
def td_clean_soup(self,soup):
    print(soup)





def cdic_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names

def cib_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names


def cmhc_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names

def cdpq_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names

def cppib_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names
def defenity_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names


def desjardins_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names

def equitable_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names


def edc_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names

def fairfax_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names


def home_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names


def ieso_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names


def laurentian_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names


def meridian_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names


def munich_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names


def omers_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names


def optrust_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names


def payments_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names


def pc_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names




def igm_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names


def mackenzie_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names


def psp_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names

 # might need fixing


def questrade_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names


def sagicor_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names


def sunlife_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names


def vancity_clean_soup(self,soup):
    print(soup)
    # content = soup.find_all(class_ = self.soupLocation[1])
    # values = []
    # # for content in soup:
    #     #do something
    
    # names = {self.companyName:[content.text for content in soup]}
    # return names
