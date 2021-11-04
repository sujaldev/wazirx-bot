from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class RightBoard:
    def __init__(self, driver):
        self.driver = driver
        self.elements = RightBoardElements(self.driver)

    def click(self, elem):
        self.driver.execute_script(
            "arguments[0].click();",
            elem
        )

    @staticmethod
    def __input_into(elem, value):
        current_input_text = elem.get_attribute("value")
        elem.send_keys(len(current_input_text) * Keys.BACKSPACE)
        elem.send_keys(value)

    def switch_to_open_orders(self):
        self.click(self.elements.open_orders_tab)

    def switch_to_completed_orders(self):
        self.click(self.elements.completed_orders_tab)

    def switch_to_buy_tab(self):
        self.click(self.elements.buy_tab)

    def switch_to_sell_tab(self):
        self.click(self.elements.sell_tab)

    def input_at_price(self, new_value):
        self.__input_into(self.elements.at_price_input, new_value)

    def input_amount(self, new_value):
        self.__input_into(self.elements.amount_input, new_value)

    def input_total(self, new_value):
        self.__input_into(self.elements.total_input, new_value)

    def buy_sell_button(self):
        self.click(self.elements.buy_sell_button)


class RightBoardElements:
    CONTAINER_PATH = "./div/div[3]/div/div[3]"

    # UPPER SECTION
    OPEN_ORDERS_PATH = CONTAINER_PATH + "/div[3]/div/div[1]"
    COMPLETED_ORDERS_PATH = CONTAINER_PATH + "/div[3]/div/div[2]"
    TOGGLE_CONTEXT_CURRENCY_PATH = CONTAINER_PATH + "/div[3]/div[2]/div/div/div[1]/div/div/input"
    CANCEL_ALL_ORDERS_PATH = CONTAINER_PATH + "/div[3]/div[2]/div/div/div[1]/button"
    ORDER_LIST_PATH = CONTAINER_PATH + "/div[3]/div[2]/div/div/div[3]/div/div"

    # LOWER SECTION
    BUY_TAB_PATH = CONTAINER_PATH + "/div[4]/div/div[1]/div[1]"
    SELL_TAB_PATH = CONTAINER_PATH + "/div[4]/div/div[1]/div[2]"
    AT_PRICE_PATH = CONTAINER_PATH + "/div[4]/div/div[2]/div/form/div[2]/div/div/input"
    AMOUNT_PATH = CONTAINER_PATH + "/div[4]/div/div[2]/div/form/div[3]/div/div/input"
    TOTAL_BASE_CURRENCY_PATH = CONTAINER_PATH + "/div[4]/div/div[2]/div/form/div[4]/div/div/input"
    BUY_OR_SELL_BUTTON_PATH = CONTAINER_PATH + "/div[4]/div/div[2]/div/form/button"

    def __init__(self, driver):
        self.driver = driver
        self.root = self.driver.find_element(By.ID, "root")

        self.container = self.root.find_element(By.XPATH, self.CONTAINER_PATH)

        # UPPER SECTION
        self.open_orders_tab = self.root.find_element(By.XPATH, self.OPEN_ORDERS_PATH)
        self.completed_orders_tab = self.root.find_element(By.XPATH, self.COMPLETED_ORDERS_PATH)
        # self.toggle_context_only_orders = self.root.find_element(By.XPATH, self.TOGGLE_CONTEXT_CURRENCY_PATH)
        # self.cancel_all_orders = self.root.find_element(By.XPATH, self.CANCEL_ALL_ORDERS_PATH)
        # self.order_list_view = self.root.find_element(By.XPATH, self.ORDER_LIST_PATH)

        # LOWER SECTION
        self.buy_tab = self.root.find_element(By.XPATH, self.BUY_TAB_PATH)
        self.sell_tab = self.root.find_element(By.XPATH, self.SELL_TAB_PATH)

    @property
    def at_price_input(self):
        return self.root.find_element(By.XPATH, self.AT_PRICE_PATH)

    @property
    def amount_input(self):
        return self.root.find_element(By.XPATH, self.AMOUNT_PATH)

    @property
    def total_input(self):
        return self.root.find_element(By.XPATH, self.TOTAL_BASE_CURRENCY_PATH)

    @property
    def buy_sell_button(self):
        return self.root.find_element(By.XPATH, self.BUY_OR_SELL_BUTTON_PATH)
