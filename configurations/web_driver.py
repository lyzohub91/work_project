from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"C:\Users\andrii.lyzogub\PycharmProjects\work_project\venv\chromedriver_win32\chromedriver.exe")
# написати фікстуру для закриття driver
# скрін коли тест фейлиться (декоратор) -на кожен метод
#allure report +

#поділити по suits - 1. поділити по папках 2.Помаркати тести(всі в одній папці), markers in pytest.ini
