import re
from bs4 import BeautifulSoup
from selenium import webdriver
from urls import URLS
import CleanerFunctions as clnr
import GetNames as getnames
test = "CIBC"
initializedObjects = getnames.initialize_company_objects()


# values = soup.find_all('span',{"class": "subhead-medium-light"})
# content = [content.text.strip() for content in values]
# print(content)

# data = values[test]
# print(values)
# names = [' '.join(name.split()) for name in data]
# print(names)


for key in list(initializedObjects.keys())[5:10]:
    print(" ")
    print("=========")
    print("")
    print(key)
    print("")
    test = initializedObjects[key].scrape_website()
    print(test)
    print("=========")
    print(" ")




# do do:
# AIG
# AIMCO
# BDC
# BMO
# CANADA LIFE
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

