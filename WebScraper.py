
from bs4 import BeautifulSoup
from selenium import webdriver
from urls import URLS
import CleanerFunctions as clnr
import GetNames as getnames

initializedObjects = getnames.initialize_company_objects()
test_soup = initializedObjects["CANADA LIFE"].dynamic_scraper()
test_result = clnr.default_clean_soup(test_soup)


# contents = test.find_all("h2",{"class": "bio-name"})
# names = [content.text.strip() for content in contents]
print(test)


def trial_web_scraper(companyName):
    test_soup = initializedObjects[companyName].dynamic_scraper()
    print("=========")
    print("")
    print(companyName)
    print("")
    print(test_soup)
    print("")
    print("=========")

for company_name in list(initializedObjects.keys())[:5]:
    if company_name in company_data:
        print(f"Processing {company_name}: {company_data[company_name]}")
        sample_method(company_name)



# do do:
# AIG//
# AIMCO//
# BDC//
# BMO//
# CANADA LIFE//
# CDIC
# CDPQ
# CIB
# CIBC
# CMHC
# CPPIB
# DEFENITY
# DESJARDINS
# EDC
# EQUITABLE BANK
# HOME CAPITAL
# IESO
# IGM FINANCIAL
# IMCO
# LAURENTIAN
# MACKENZIE INVESTMENTS
# Manulife
# MERIDIAN
# MUNICH RE
# NBC
# OMERS
# OPB
# OPTRUST
# OTPP
# PAYMENTS CANADA
# PSP INVESTMENTS
# RBC
# SAGICOR
# SCOTIABANK
# SUN LIFE
# TD
# UPP
# VANCITY

