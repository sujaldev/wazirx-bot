from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LeftBoard:
    def __init__(self, driver):
        self.driver = driver
        self.elements = LeftBoardElements(self.driver)

        # STATE VARIABLES
        self.search_state = ""

    def click(self, elem):
        self.driver.execute_script(
            "arguments[0].click();",
            elem
        )

    # OPERATIONS
    def switch_base_currency(self, new_currency):
        try:
            elem = self.elements.base_currencies[new_currency.lower()]
            self.click(elem)
        except KeyError:
            raise Exception("Invalid Base Currency! Try one of these: INR, USDT, WRX or BTC.")

    def sort_by(self, sort_filter):
        try:
            sort_btn = self.elements.sort[sort_filter.lower()]
            self.click(sort_btn)
        except KeyError:
            raise Exception("Invalid Sort Filter! Try one of these: PAIR, VOLUME OR CHANGE")

    def search(self, search_text):
        self.search_state = search_text
        self.elements.search.send_keys(search_text)

    def clear_search(self):
        self.elements.search.send_keys(
            len(self.search_state) * Keys.BACKSPACE
        )
        self.search_state = ""

    def get_currency_dict(self):
        currencies = {}

        currency_containers = self.elements.currency_list.find_elements(By.TAG_NAME, "a")
        for currency in currency_containers:
            current_name = currency.get_attribute("href").replace("https://wazirx.com/exchange/", "")
            currencies.update({current_name: {
                "element": currency,
                "change": float(currency.find_element(
                    By.XPATH,
                    "./div[2]/div[2]/span"
                ).get_attribute("innerHTML").replace("▼ ", "").replace("▲ ", "").replace("%", "")),

                "price": float("".join([
                    c for c in currency.find_element(
                        By.XPATH,
                        "./div[3]/div/span"
                    ).get_attribute("innerHTML") if c.isdigit() or c == "."
                ])),
            }})

        return currencies

    def switch_currency(self, currency_code):
        """
        FORMAT: CRYPTO-BASE
        EXAMPLE: DOGE-INR
        """
        crypto_code, base_code = currency_code.split("-")

        self.switch_base_currency(base_code)

        self.search(crypto_code)
        output = self.get_currency_dict()
        try:
            self.click(output[currency_code.upper()]["element"])
            self.clear_search()
        except KeyError:
            raise Exception("Invalid Crypto Currency!")


class LeftBoardElements:
    CONTAINER_PATH = "./div/div[3]/div/div[1]/div"
    BASE_CURRENCIES_PATH = CONTAINER_PATH + "/div[1]/div[1]/div/label[{}]/input"
    SEARCH_INPUT_PATH = CONTAINER_PATH + "/div[1]/div[2]/div/input"
    SORT_BUTTONS_PATH = CONTAINER_PATH + "/div[1]/div[3]/div[{}]/span"
    CURRENCY_LIST_PATH = CONTAINER_PATH + "/div[2]"

    def __init__(self, driver):
        self.driver = driver
        self.root = self.driver.find_element(By.ID, "root")

        self.container = self.root.find_element(By.XPATH, self.CONTAINER_PATH)
        self.base_currencies = self.generate_elem_dict_by_xpath(
            ["inr", "usdt", "wrx", "btc"],
            self.BASE_CURRENCIES_PATH
        )
        self.search = self.root.find_element(By.XPATH, self.SEARCH_INPUT_PATH)
        self.sort = self.generate_elem_dict_by_xpath(
            ["pair", "volume", "change"],
            self.SORT_BUTTONS_PATH
        )
        self.currency_list = self.root.find_element(By.XPATH, self.CURRENCY_LIST_PATH)

    def generate_elem_dict_by_xpath(self, keys, xpath):
        elem_dict = {}
        for i, key in enumerate(keys):
            elem_dict[key] = self.root.find_element(By.XPATH, xpath.format(i + 1))

        return elem_dict
