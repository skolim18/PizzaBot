import time
from selenium import webdriver
from utils import CHROMEDRIVER_PATH, chrome_options


class Pizza:
    """Klasa główna aplikacji, wykonuje wszystkie najważniejsze operacje w programie"""

    # pylint: disable=too-many-instance-attributes
    # 10 atrybutów jest wytłumaczalne dla tego typu klasy.

    def __init__(self, hunger=None, drink=4):
        self.hunger = hunger
        self.drink = drink
        self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
        self.drink_button = '//*[@id="_buying-flow-modal-content"]/div/div/div[5]/div[2]/div[3]/button'
        self.go_to_cart_button = '//*[@id="_shopping-cart"]/div[3]/a'
        self.water = '//*[@id="_buying-flow-modal-content"]/div/div/div[3]/div/div/div[2]/div/div/div/div[' \
                     '3]/div/div/div[2]/button '
        self.cola = '//*[@id="_buying-flow-modal-content"]/div/div/div[3]/div/div/div[2]/div/div/div/div[' \
                    '9]/div/div/div[2]/button '
        self.cappy = '//*[@id="_buying-flow-modal-content"]/div/div/div[3]/div/div/div[2]/div/div/div/div[' \
                     '15]/div/div/div[2]/button '
        self.small_pizza = '//*[@id="cb09d6a1-c93f-11e7-93f9-525400841de1"]/div[2]'
        self.large_pizza = '//*[@id="ce6b7613-c93f-11e7-93f9-525400841de1"]/div[2]'

    def hunger_drink(self):
        """Metoda weryfikuje czy użytkownik wprowadził poprawne numery oraz wysyła komunikat o zamówieniu"""
        if isinstance(self.hunger, int):
            if 0 < int(self.hunger) <= 5:
                print("Dobrze, wybrałeś numer {}, więc weźmiemy małą pizzę =)".format(self.hunger))
            elif 5 < int(self.hunger) <= 10:
                print('Dobrze, wybrałeś numer {}, więc weźmiemy dużą pizzę =)'.format(self.hunger))
            else:
                print("Nie wybrałeś poprawnego oznaczenia, w związku z tym zamówimy małą pizzę!")
        else:
            print("Nie wybrałeś poprawnego oznaczenia, w związku z tym zamówimy małą pizzę!")

        if isinstance(self.drink, int):
            if int(self.drink) == 1:
                print("Zamawiam wodę!")
            elif int(self.drink) == 2:
                print("Zamawiam Coca Cole!")
            elif int(self.drink) == 3:
                print("Zamawiam Cappy Pomarańczowy!")
            elif int(self.drink) == 4:
                print('Dobrze, przechodzimy dalej!')
            else:
                print('Nie wybrałeś poprawnego oznaczenia, w związku z tym nie zamówimy żadnego napoju')
        else:
            print('Nie wybrałeś poprawnego oznaczenia, w związku z tym nie zamówimy żadnego napoju')
        return self.hunger, self.drink

    @staticmethod
    def user_input():
        """Metoda służąca do wprowadzenia danych z poziomu użytkownika"""
        while True:
            try:
                return Pizza(
                    int(input("W skali od 1 do 10 wybierz jak bardzo głodny jesteś:")),
                    int(input("Chcesz coś do picia?\n"
                              "[1] - Woda\n"
                              "[2] - Coca Cola \n"
                              "[3] - Cappy Pomarańczowy \n"
                              "[4] - Nie dziękuję \n")))
            except ValueError:
                print("Nie wybrałeś właściwej opcji!")
                continue

    def pick_pizza(self, xpath):
        """Metoda która po podaniu parametru zwróci nam xpath do przycisku"""
        picker = self.driver.find_element_by_xpath(xpath)
        picker.click()

    def pick_drink(self, xpath):
        """Metoda która po podaniu parametru zwróci nam xpath do przycisku dodawania napoju"""
        picker = self.driver.find_element_by_xpath(xpath)
        picker.location_once_scrolled_into_view
        picker.click()
        time.sleep(1)

    def next_button(self, button_xpath):
        """Metoda dzięki której bot klika w guziki"""
        button_picker = self.driver.find_element_by_xpath(button_xpath)
        button_picker.click()

    def fill_textbox(self):
        """Metoda która uzupełnia pola tekstowe"""
        self.driver.find_element_by_xpath(
            '//*[@id="order-form"]/div[1]/div[1]/div/div[3]/label/input').click()
        name = "Bartosz"
        self.driver.find_element_by_xpath(
            '//*[@id="order-form"]/div[3]/div/div[2]/div/div/div[1]/div/input').send_keys(name)
        surname = "Skolimowski"
        self.driver.find_element_by_xpath(
            '//*[@id="order-form"]/div[3]/div/div[2]/div/div/div[2]/div/input').send_keys(surname)
        street = '1 Maja'
        self.driver.find_element_by_xpath(
            '//*[@id="order-form-street"]').send_keys(street)
        number = '50'
        self.driver.find_element_by_xpath(
            '//*[@id="order-form-streetNumber"]').send_keys(number)
        city = 'Katowice'
        self.driver.find_element_by_xpath(
            '//*[@id="order-form-city"]').send_keys(city)
        phone = '123456789'
        self.driver.find_element_by_xpath(
            '//*[@id="order-form"]/div[3]/div/div[2]/div/div/div[3]/div/div/input').send_keys(phone)
        email = 'john.doe@doe.com'
        self.driver.find_element_by_xpath(
            '//*[@id="order-form"]/div[3]/div/div[2]/div/div/div[4]/div/input').send_keys(email)
        additional_text = 'Zostałam zamówiona przez bota!'
        self.driver.find_element_by_xpath(
            '//*[@id="order-form"]/div[3]/div/div[4]/div/div/textarea').send_keys(additional_text)

    def get_pizza(self):
        """Metoda która wykonuje wcześniej podane funkcje"""
        self.driver.get(url="http://www.basiliana.pl/menu")
        time.sleep(5)
        if isinstance(self.hunger, int):
            if 0 < int(self.hunger) <= 5:
                self.pick_pizza(self.small_pizza)
            elif 5 < int(self.hunger) <= 10:
                self.pick_pizza(self.large_pizza)
            else:
                self.pick_pizza(self.small_pizza)
        else:
            self.pick_pizza(self.small_pizza)
        time.sleep(3)
        if isinstance(self.drink, int):
            if self.drink == 1:
                self.pick_drink(self.water)
            elif self.drink == 2:
                self.pick_drink(self.cola)
            elif self.drink == 3:
                self.pick_drink(self.cappy)
            else:
                self.next_button(self.drink_button)
        else:
            self.next_button(self.drink_button)
        self.next_button(self.drink_button)
        time.sleep(1)
        self.next_button(self.go_to_cart_button)
        time.sleep(1)
        self.fill_textbox()
        time.sleep(500)
