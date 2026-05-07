
import time
from pages.homepage import HomePage
from pages.product import ProdustPage



def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    produst_page = ProdustPage(browser)
    produst_page.check_titile_is("Samsung galaxy s6")



def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor()
    time.sleep(6)
    homepage.check_products_count(2)




