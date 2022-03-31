import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setUp():
    global moviename, YearofRelease, Directorname, distributor, producer, driver
    moviename = input("Enter the movie name: ")
    YearofRelease = input("Enter the year of release: ")
    Directorname = input("Enter the director name: ")
    distributor = input("Enter the distributor: ")
    producer = input("Enter the producer: ")

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()

def test_moviedetails(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    time.sleep(1)
    driver.find_element_by_name("mname").send_keys(moviename)
    time.sleep(1)
    driver.find_element_by_name("myear").send_keys(YearofRelease)
    time.sleep(1)
    driver.find_element_by_name("mdirector").send_keys(Directorname)
    time.sleep(1)
    driver.find_element_by_name("mdist").send_keys(distributor)
    time.sleep(1)
    driver.find_element_by_name("mproducer").send_keys(producer)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select").click()
    time.sleep(1)
    driver.find_element_by_name("subbtn").click()


