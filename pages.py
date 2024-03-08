from time import sleep

class FeedPage:
    def __init__(self, browser):
        self.browser = browser

    def find_notifications(self):

        heart_button = self.browser.find_element('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[1]/div/div[2]/div[6]/div/span/div/a')
        heart_button.click()


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = self.browser.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input')
        password_input = self.browser.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input')
        username_input.send_keys(username)
        password_input.send_keys(password)
        sleep(5)
        login_button = self.browser.find_element('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button')
        login_button.click()
        sleep(5)

        return FeedPage(self.browser)

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def go_to_login_page(self):

        cookie_button = self.browser.find_element('xpath', '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
        cookie_button.click()
        
        return LoginPage(self.browser)