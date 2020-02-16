from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


def test_score_service(url, driver):
    driver.get(url)
    score = list(driver.find_element_by_id("score").text.split())[-1]
    if 1 >= int(score) >= 1000:
        return True
    else:
        return False


def main_function():
    url = "http://127.0.0.1:8777/"
    driver = webdriver.Chrome(executable_path=r'chromedriver', chrome_options=chrome_options)
    try:
        check_app = test_score_service(url, driver)
        if check_app:
            return 0
        else:
            return -1
    except ValueError:
        return -1


def run_test():
    test_app = main_function()
    if test_app == 0:
        print("Test finished successfully")
        return False
    elif test_app == -1:
        print("OS exit code {}".format(test_app))
        print("Test has failed")
        return True
    else:
        print("Something went wrong")
        return True


run_test()
