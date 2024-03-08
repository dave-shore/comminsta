from selenium import webdriver
from pages import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--user", type = str,
                    help = "Instagram username.")
parser.add_argument("--pw", type = str,
                    help = "Instagram password.")
args = parser.parse_args()

if __name__ == "__main__":

    browser = webdriver.Firefox()
    browser.implicitly_wait(5)

    home_page = HomePage(browser)
    login_page = home_page.go_to_login_page()
    login_page.login(args.user, args.pw)