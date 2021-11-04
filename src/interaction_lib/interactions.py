from selenium import webdriver
from src.interaction_lib.left_board import LeftBoard
from src.interaction_lib.right_board import RightBoard


class WazirxWeb:
    URL = "https://www.wazirx.com/exchange"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.URL)

        self.lb = LeftBoard(self.driver)
        self.rb = RightBoard(self.driver)

    # noinspection PyMethodMayBeStatic
    def start_console(self):
        while True:
            command = input(">>> ").split(" ")
            while len(command) < 3:
                command.append("")
            command = "self.{}.{}({})".format(*command)

            try:
                exec(command)
            except Exception as e:
                print(e)


if __name__ == "__main__":
    WazirxWeb()
