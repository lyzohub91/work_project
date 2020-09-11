from selenium import webdriver


def get_driver():
    driver = webdriver.Chrome(executable_path=r"C:\Users\andrii.lyzogub\PycharmProjects"
                                              r"\work_project\venv\chromedriver_win32\chromedriver.exe")
    return driver
