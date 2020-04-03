from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest 

browser = webdriver.Chrome()
browser.get("http://127.0.0.1:5000/")

def test_homepage():
    #Tests that default homepage is up
    CurrentUrl = browser.current_url
    assert CurrentUrl == "http://127.0.0.1:5000/"
   
def test_about():
    #Test the about page
    browser.get(" http://127.0.0.1:5000/about")
    CurrentUrl = browser.current_url
    assert CurrentUrl == "http://127.0.0.1:5000/about"
    

def test_resources():
    #Test the resources page
    browser.get(" http://127.0.0.1:5000/resources")
    CurrentUrl = browser.current_url
    assert CurrentUrl == "http://127.0.0.1:5000/resources"


def test_settings():
    #Test the settings page
    browser.get(" http://127.0.0.1:5000/settings")
    CurrentUrl = browser.current_url
    assert CurrentUrl == "http://127.0.0.1:5000/settings"



def test_buttons():
    #Test the nav buttons
    browser.get("http://127.0.0.1:5000/index")
    CurrentUrl = browser.current_url
    Button = browser.find_element_by_xpath("/html/body/div/ul/li[1]/a")
    Button.click()
    time.sleep(1)
    Button = browser.find_element_by_xpath("/html/body/div/ul/li[2]/a")
    Button.click()
    time.sleep(1)
    Button = browser.find_element_by_xpath("/html/body/ul/li[3]/a")
    Button.click()
    time.sleep(1)
    Button = browser.find_element_by_xpath("/html/body/ul/li[4]/a")
    Button.click()
    time.sleep(1)

def test_map():
    browser.get("http://127.0.0.1:5000/index")
    time.sleep(1)
    html = browser.find_element_by_tag_name("html")
    html.send_keys(Keys.CONTROL, Keys.ADD)

    html.send_keys(Keys.CONTROL, "0")


    
    #exits the browser
    time.sleep(5)
    browser.close()
    browser.quit()