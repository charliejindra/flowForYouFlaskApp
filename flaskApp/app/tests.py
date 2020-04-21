from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest 

browser = webdriver.Chrome()
browser.get("https://flowforyou.pythonanywhere.com/index")

def test_homepage():
    #Tests that default homepage is u/p
    CurrentUrl = browser.current_url
    assert CurrentUrl == "https://flowforyou.pythonanywhere.com/index"
   
def test_about():
    #Test the about page
    browser.get(" https://flowforyou.pythonanywhere.com/about")
    CurrentUrl = browser.current_url
    assert CurrentUrl == "https://flowforyou.pythonanywhere.com/about"
    

def test_resources():
    #Test the resources page
    browser.get(" https://flowforyou.pythonanywhere.com/resources")
    CurrentUrl = browser.current_url
    assert CurrentUrl == "https://flowforyou.pythonanywhere.com/resources"



def test_buttons():
    #Test the nav buttons
    browser.get("https://flowforyou.pythonanywhere.com/index")
    CurrentUrl = browser.current_url
    Button = browser.find_element_by_xpath("/html/body/div/div[3]/button")
    Button.click()
    time.sleep(1)
    Button = browser.find_element_by_xpath("/html/body/div/div[2]/a[1]")
    Button.click()
    time.sleep(1)
    Button = browser.find_element_by_xpath("/html/body/div/div[3]/button")
    Button.click()
    time.sleep(1)
    Button = browser.find_element_by_xpath("/html/body/div/div[2]/a[2]")
    Button.click()
    time.sleep(1)
    Button = browser.find_element_by_xpath("/html/body/div/div[3]/button")
    Button.click()
    time.sleep(1)
    Button = browser.find_element_by_xpath("/html/body/div/div[2]/a[3]")
    Button.click()
    time.sleep(1)

def test_map():
    browser.get("https://flowforyou.pythonanywhere.com/index")
    time.sleep(1)
    html = browser.find_element_by_tag_name("map")
    html.send_keys(Keys.CONTROL, Keys.ADD)

    html.send_keys(Keys.CONTROL, "50")


    
    #exits the browser
    time.sleep(5)
    browser.close()
    browser.quit()