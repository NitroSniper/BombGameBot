#this is a bomb game bot for the game "bomb game".
#this bot is made by: "Nitro Sniper"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
import time

def is_element_visible(element):
    return element.value_of_css_property('display') != 'none'

def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    WAIT = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    badwait = WebDriverWait(driver, 10)
    # RoomCode = input("Enter Room Code: ")
    RoomCode = 'NKNR'
    driver.get(f"https://jklm.fun/{RoomCode}")
    #info = WAIT.until(EC.presence_of_element_located((By.CLASS_NAME, 'styled nickname')))
    driver.implicitly_wait(6)
    test = driver.find_element(By.CLASS_NAME, 'styled.nickname')
    test.clear()
    test.send_keys('Nitro Sniper\n')
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    #print (driver.page_source)
    joined = driver.find_element(By.CLASS_NAME, 'joined')
    seating = driver.find_element(By.CLASS_NAME, 'seating')
    
    while True:
        if not seating.is_displayed() and is_element_visible(joined): # if the game has started
            print ("Joined and Seating")
            print (driver.find_element(By.CLASS_NAME, 'syllable').text)
            # print(driver.execute_script('return milestone.playerStatesByPeerId[milestone.currentPlayerPeerId]'))
            #print (driver.execute_script('return JSON.stringify(players[0], null, 4)'))
            print (driver.execute_script('return milestone.playerStatesByPeerId'))
            print (driver.execute_script('return selfPeerId'))

        time.sleep(1)
    input("Press enter to continue...")
if __name__ == "__main__":
    main()