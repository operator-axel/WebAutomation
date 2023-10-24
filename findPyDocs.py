#! python3 
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


print('What are we searching for?!?')
searchText = input()

browser = webdriver.Firefox()

browser.get('https://pypi.org/')

elem = browser.find_element(By.ID, 'search')
elem.send_keys(searchText + Keys.RETURN)