# using python selenium automation and action chains visit the url and Drag and Drop operation of white color rectangular box into yellow rectangular box

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.common.exceptions import NoSuchElementException,NoSuchAttributeException
from selenium.webdriver.support.color import Color

class Jquery:
    def __init__(self, weburl):
        self.url = weburl
        firefox_option = webdriver.FirefoxOptions()
        firefox_option.add_argument("--headless")
        # Create a new WebDriver instance
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_option)
        self.driver.maximize_window()
    def navigation(self):
        try:
            # navigate browser to given webpage
            self.driver.get(self.url)
        except NoSuchAttributeException as error:
            print(error)

    def new(self):
        try:
            # in given webpage there are two frame, so we handle that using iframe method
            # we want to switch from one frame to another frame
            self.driver.switch_to.frame(0)
            # we are using ID as locators to find element
            drag_element = self.driver.find_element(by=By.ID, value='draggable')
            drop_element = self.driver.find_element(by=By.ID, value='droppable')
            rgb = drop_element.value_of_css_property("background-color")
            hex_before = Color.from_string(rgb).hex
            print(f"before drop_element background-color:{hex_before}")
            # action_chains class are used to interact low level interaction like mouse over, key press, muse buttons
            actions = ActionChains(self.driver)
            sleep(5)
            # using drag and drop method in action_chains
            actions.drag_and_drop(drag_element,drop_element).perform()
            # after dropping we want to verify its background-color should be changed into yellow or hexa_value!
            after_drop = drop_element.value_of_css_property("background-color")
            hexa_after = Color.from_string(after_drop).hex
            print(f"after drop_element background-color:{hexa_after}")
            # after dropping we want to verify its text, bockground-color should be changed into Dropped!
            if drop_element.text == 'Dropped!':
                print("it is verified ")
                print(drop_element.text)
            if drop_element.value_of_css_property("background-color") == after_drop:
                print("its color is changed to yellow")
            else:
                print("it is not dropped")

        except NoSuchElementException as error1:
            print(error1)
    def quit(self):
        # quit driver
        self.driver.quit()

link = "https://jqueryui.com/droppable/"
data = Jquery(link)
data.navigation()
data.new()
data.quit()