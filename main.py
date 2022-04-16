#this is a bomb game bot for the game "bomb game".
#this bot is made by: "Nitro Sniper"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(f"https://techwithtim.net/")
    print (driver.title)
    input("Press enter to continue...")
    #search = driver.find_element_by_name('s')
    search = driver.find_element(By.NAME, 's')
    search.send_keys('test')
    search.send_keys(Keys.RETURN)
    input("Press enter to continue...")
    driver.quit()

if __name__ == "__main__":
    main()