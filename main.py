from common_imports import *
import makecsv
from getpass import getpass

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")


login = input("Login: ")
password = getpass("Password: ")

login_input = driver.find_element(by=By.ID, value='username')
password_input = driver.find_element(by=By.ID, value='password')


login_input.send_keys(login)
try:
    password_input.send_keys(password + Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER)
except:
    pass
time.sleep(2)
makecsv.getjobs(driver)



