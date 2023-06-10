''' Scraper for indeed/google/glassdoor'''
import requests
import json
import csv
from datetime import datetime
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
from os.path import exists



class Scraper():
    
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.minimize_window()
        pass
        
    def get_indeed(self, url: str, filters: dict):
        self.get_soup_indeed(url)
        job_list = []
        for div in self.soup.find_all(name="div", attrs={"class":"job_seen_beacon"}):
            title = div.find("span").text
            location = div.find("div", attrs={"class":"companyLocation"}).text
            location = location.split(",", 1)[0]
            location = location.strip()
            job_url = div.find("a",).get("href")
            try:
                days_ago = div.find("span", attrs={"class":"date"}).text
            except:
                days_ago = "N/A"
            company_name = div.find("span", attrs={"class":"companyName"}).text
            # print("Location:", location)
            try:
                a = div.find("div", attrs={"class":"attribute_snippet"})
                salary = a.text
                # print("Salary/Info:", salary)
            except:
                salary = "N/A"
                # print("Salary/Info: N/A")
            days_ago = days_ago.replace("PostedPosted", "")
            job_url = "https://ca.indeed.com"+job_url
            now = datetime.now()
            current_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            job_list.append([title, company_name, location, job_url, days_ago, "google"])
            # job_list.append([title, company_name, location, salary, days_ago, current_time, job_url])
        self.job_list = job_list
        return self.job_list

    def get_google(self, url: str, filters: dict):
        self.get_soup(url)
        job_list = []
        for div in self.soup.find_all(name="li", attrs={"class":"iFjolb gws-plugins-horizon-jobs__li-ed"}):        
            url = div.find("span", attrs={"class":"DaDV9e"})
            try:
                url = url.find("a").get("href")
            except:
                pass
            title = div.find("div", attrs={"class":"BjJfJf PUpOsf"}).text
            company_name = div.find("div", attrs={"class":"vNEEBe"}).text
            location = div.find("div", attrs={"class":"Qk80Jf"}).text
            location = location.split(",", 1)[0]
            location = location.strip()
            try:
                days_ago = div.find("span", attrs={"class":"LL4CDc"}).find("span").text
            except:
                days_ago = "N/A"
            salary = "N/A"
            job_url = url
            now = datetime.now()
            current_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            job_list.append([title, company_name, location, url, days_ago, "indeed"])
            # job_list.append([title, company_name, location, salary, days_ago, current_time, job_url])
        self.job_list = job_list
        return self.job_list
    
    def get_glassdoor(self, url: str, filters: dict):
        self.get_soup(url)
        job_list = []
        domain = "https://www.glassdoor.ca"
        for div1 in self.soup.find_all(name="li", attrs={"class":"react-job-listing"}):
            company = div1.find("div", attrs={"class":"job-search-1bgdn7m"}).text
            company = company[:-5] # remove rating
            title = div1.find("div", attrs={"class":"job-title mt-xsm"}).text
            location = div1.find("div", attrs={"class":"location mt-xxsm"}).text
            url = div1.find("a", attrs={"class":"d-flex justify-content-between p-std jobCard"}).get('href')
            listing_age = div1.find("div", attrs={"class":"d-flex align-items-end ml-xsm listing-age"}).text
            url = domain + url
            job_list.append([title, company, location, url, listing_age, "glassdoor"])    
        return job_list
        



    def get_soup(self, url):
        self.url = url
        self.driver.get(self.url)
        self.driver.implicitly_wait(20)
        time.sleep(1)
        self.html = self.driver.page_source
        self.encode = (self.html.encode('utf-8'))
        self.soup = BeautifulSoup(self.html, "html.parser")
        return self.soup
    
    def get_soup_indeed(self, url):
        self.url = url
        self.driver.get(self.url)
        self.driver.implicitly_wait(20)
        # time.sleep(self.wait_time)
        time.sleep(5)
        self.html = self.driver.page_source
        self.encode = (self.html.encode('utf-8'))
        # self.driver.quit()
        self.soup = BeautifulSoup(self.html, "html.parser")
        return self.soup
