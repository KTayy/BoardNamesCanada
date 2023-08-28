import re
from bs4 import BeautifulSoup
# subclass function for cleanup specific to each company.
# require : soup from beautiful soup
# PC: return a dictionary names {company: [values]} where values has the cleaned up board directors

def default_clean_soup(soup):
    contents = soup.find_all(self.soupLocation[1],self.soupLocation[2])
    values = [content.text.strip() for content in contents]

    names = {self.companyName : values }
    return names
    
def aig_clean_soup(self, soup):
    main_content_div = soup.find(self.soupLocation[1], self.soupLocation[2])
    content = main_content_div.find_all(self.soupLocation[3], self.soupLocation[4])
    values = []
    for item in content:
        name_element = item.find("h2")
        if name_element:
            names.append(name_element.text.strip())
    names = {self.companyName: values}      
    return names


def otpp_clean_soup(self,soup):
    contents = soup.find_all(self.soupLocation[1], self.soupLocation[2])
    values = []
    for content in contents:
        h2_element = content.find('h2')
        value = h2_element.text.strip()
        values.append(value)
    names = {self.companyName: values}
    return names

def opb_clean_soup(self,soup):
    contents = soup.find_all(self.soupLocation[1], self.soupLocation[2])
    values = []
    for content in contents:
        h3_element = content.find('h3')
        value = h3_element.text.strip()
        value = re.sub(r"\s",",", value)
        #title = value.split(",")[-1]
        value = value.split(",")[0] + " " + value.split(",")[1]
        values.append(value)
    names = {self.companyName: values}
    return names

def imco_clean_soup(self,soup):
    contents = soup.find_all(self.soupLocation[1], self.soupLocation[2])
    values = []
    for content in contents:
        a_tag = content.find('a')
        name = a_tag.text.strip()
        name = re.sub(r"\s",",", name)
        name = name.split(",")[0] + " " + name.split(",")[-1]
        values.append(name)
    names = {self.companyName: values}
    return names


def aimco_clean_soup(self, soup):
    content = soup.find_all(self.soupLocation[1], self.soupLocation[2])
    values = [] 
    for content in contents:
        if content.name == 'p' and 'person-name' in content.get('class',[]):
            name = content.get_text(strip=True)
            values.append(name)
    names = {self.companyName: values}
    return content
        
        # p_tag = content.find('p')
        # name = p_tag.text.strip()
        # name = re.sub(r"\s",",", name)
        # name = name.split(",")[0] + " " + name.split(",")[-1] 
        # values.append(name)    
    names = {self.companyName: values}
    return names

def bdc_clean_soup(self,soup):
    name_tags = soup.find_all(self.soupLocation[1])
    values = [name_tag.text.strip() for name_tag in name_tags]
    names = {self.companyName:values}
    return names

def bmo_clean_soup(self,soup):
    contents = soup.find_all(self.soupLocation[1],self.soupLocation[2])
    values = [content.text.strip() for content in contents]

    names = {self.companyName : values }
    return names

def canadalife_clean_soup(self,soup):
    contents = soup.find_all(self.soupLocation[1], self.soupLocation[2])
    values = [content.text.strip() for content in contents]
    # for content in soup:
        #do something
    
    names = {self.companyName:values}
    return values

#################### ^^^^^^ done ^^^^^^ ################################


def upp_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names





def cibc_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names



def manulife_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names




def nbc_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def rbc_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def scotiabank_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def td_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names






def cdic_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def cib_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names


def cmhc_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def cdpq_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def cppib_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def defenity_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names


def desjardins_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def equitable_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names


def edc_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names


def fairfax_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def home_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def ieso_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def laurentian_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def meridian_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def munich_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def omers_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def optrust_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def payments_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def pc_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names



def igm_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def mackenzie_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def psp_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def nbc_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def questrade_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def sagicor_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def sunlife_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names

def vancity_clean_soup(self,soup):
    content = soup.find_all(class_ = self.soupLocation[1])
    values = []
    # for content in soup:
        #do something
    
    names = {self.companyName:[content.text for content in soup]}
    return names