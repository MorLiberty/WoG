from selenium import webdriver


def test_score_service(url, driver):
    driver.get(url)
    score = list(driver.find_element_by_id("score").text.split())[-1]
    if 1 <= int(score) <= 1000:
        return True
    else:
        return False


def main_function():
    url = "http://127.0.0.1:8777/"
    driver = webdriver.Chrome(executable_path=r'chromedriver')
    try:
        check_app = test_score_service(url, driver)
        if check_app:
            return 0
        else:
            return -1
    except ValueError:
        return -1


test_app = main_function()
if test_app == 0:
    print("Test finished successfully")
elif test_app == -1:
    print("OS exit code {}".format(test_app))
    print("Test has failed")
else:
    print("Something went wrong")
