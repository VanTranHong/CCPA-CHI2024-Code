import selenium
import pyautogui as py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service


import time
import os
import codecs
import csv
import pandas as pd
import numpy as np
import datetime
import socket
import re


#########################   Please specify the state that you are conducting your experiment in #############
state = "CA"
keyboard = "command" ### if you use Mac, please change this to "command"
fname = "./website_list.csv"
#############################################
options = webdriver.ChromeOptions()
options.add_argument('--headless')
today = str(datetime.date.today())
# get the IP address
s =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))
IP = s.getsockname()[0]




#Specify the place that you are going to store the results
main_path = os.getcwd()
store_folder = main_path +"/" +state+"/"


if not os.path.isdir(store_folder): 
    os.mkdir(store_folder)

# This is the folder to store the html page source
page_source = store_folder + "page_source/"
if not os.path.isdir(page_source): 
    os.mkdir(page_source)
page_source = page_source + today +"/"
if not os.path.isdir(page_source): 
    os.mkdir(page_source)




# This is the folder to store the screenshots ############
screenshots = store_folder + "screenshots/"
if not os.path.isdir(screenshots): 
    os.mkdir(screenshots)
screenshots = screenshots + today+"/"
if not os.path.isdir(screenshots): 
    os.mkdir(screenshots)

# This is used to store the text used to search for the feature
search_text = store_folder + "search_text/"
if not os.path.isdir(search_text): 
    os.mkdir(search_text)
search_text = search_text + today+"/"
if not os.path.isdir(search_text): 
    os.mkdir(search_text)



with open (search_text+"ip_address.txt","w") as f:
    f.write(IP)
    f.close()




def get_link_name(domain,index):


    screenshots_folder = screenshots+str(index)+"/"
    if not os.path.isdir(screenshots_folder):   
        os.mkdir(screenshots_folder)

    page_source_folder = page_source+str(index)+"/"
    if not os.path.isdir(page_source_folder):   
        os.mkdir(page_source_folder)

    search_text_folder = search_text+str(index)+"/"
    if not os.path.isdir(search_text_folder):
        os.mkdir(search_text_folder)

    options = webdriver.ChromeOptions()
# # options.add_argument('--headless')
    options.add_experimental_option("detach", False)
    # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36")
    # Specify the path to chromedriver
    service = Service(executable_path="./chromedriver", chrome_options=options)
    # driver = webdriver.Chrome(executable_path = "./chromedriver", chrome_options=options)
   
    driver = webdriver.Chrome(service=service)
    

   
 
    try: 
        driver.get(domain)
        driver.maximize_window()
        # print(driver.page_source)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        wait = WebDriverWait(driver,6)


        pagesource_text = driver.page_source
        filename = open(page_source_folder +"pagesource.html","w")

        # # Adding input data to the HTML file
        filename.write(pagesource_text)

        # # Saving the data into the HTML file
        filename.close()



    #  take screenshot with the search bar 

        py.moveTo(150, 400)
        py.click()
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
            
        
        py.hotkey(keyboard,"f")
        py.typewrite("do not sell or share", interval = 0.15 )
        screenshot = py.screenshot()

        # Save the screenshot to a file
        screenshot.save(screenshots_folder  + "step0.png")

    
        time.sleep(3)

        py.hotkey(keyboard,"f")
        py.typewrite("do not sell", interval = 0.15 )
        screenshot = py.screenshot()

        # Save the screenshot to a file
        screenshot.save(screenshots_folder  + "step1.png")
        time.sleep(3)

        py.hotkey(keyboard,"f")
        py.typewrite("privacy choice", interval = 0.15 )
        screenshot = py.screenshot()

        # Save the screenshot to a file
        screenshot.save(screenshots_folder  + "step2.png")
        time.sleep(3)

        py.hotkey(keyboard,"f")
        py.typewrite("opt out", interval = 0.15 )
        screenshot = py.screenshot()

        # Save the screenshot to a file
        screenshot.save(screenshots_folder  + "step3.png")
        time.sleep(3)


        py.hotkey(keyboard,"f")
        py.typewrite("do not share", interval = 0.15 )
        screenshot = py.screenshot()

        # Save the screenshot to a file
        screenshot.save(screenshots_folder  + "step4.png")


    # search through the page source to find the text of opt-out link
        elements = ["a", "button", "span"]
        regex_patterns = [r'\bdo\b.*\bsell\b', r'\bdo\b.*\bshare\b', r'\bopt\b.*\bout\b', r'\bprivacy\b.*\bchoice\b']
        found_text = set()
        for element in elements:
        
            found_elements = driver.find_elements(By.TAG_NAME, element)
            
            for found_element in found_elements:
                
                if bool(re.search(r'do.*sell', found_element.text, re.IGNORECASE)):
                    found_text.add(found_element.text)
                if bool(re.search(r'do.*share', found_element.text, re.IGNORECASE)):
                    found_text.add(found_element.text)
                if bool(re.search(r'opt.*out', found_element.text, re.IGNORECASE)):
                    found_text.add(found_element.text)
                if bool(re.search(r'privacy.*choice', found_element.text, re.IGNORECASE)):
                    found_text.add(found_element.text)
                
        
    
        if len(found_text) >0:
            print("Found text")
            print(found_text)
            df_text = pd.DataFrame(list(found_text), columns = ["text"])
            df_text.to_csv(search_text_folder + "pagesource_text.csv", index = False)


        
    except selenium.common.exceptions.WebDriverException:
        pass




df = pd.read_csv(fname)
for index, row in df.iterrows():

    index = row["Index"]
    
   
    url = "https://www.walmart.com/"
    keysearch = get_link_name(url,index)
    break














    
        
  