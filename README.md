# lessons_Python_Automation
### 1 Урок:
Типы данных. Понятие переменной  
+ Списки  
+ Функции  
+ Области видимости переменной  
+ Стек вызовов  
  ***Пример:***
```
first_name = input('Введите ваше имя: ')
last_name = input('Введите вашу фамилию: ')
print(f'Вас зовут: {first_name} {last_name}')
```
### 2 Урок:
+ Ветвления. Условные операторы  
+ Циклы  
+ Логические операторы  
  ***Пример:***
```
lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
lst2 = []
for i in range(0, len(lst)):
    if lst[i] < 30 and lst[i] % 3 == 0:
        lst2.append(lst[i])
print(lst2)
```
### 3 Урок:
+ Основные понятия ООП  
+ Методы и поля класса  
+ Взаимодействие классов  
+ Вложенные классы  
  ***Пример***
```
class Person:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        print('user created')

    def greeting(self):
        print(f'{self.name} says HELLO!')


class Student(Person):

    def __init__(self, name, age, average_grade) -> None:
        super().__init__(name, age)
        self.average_grade = average_grade

    def greeting(self):
        print(f'Student with name {self.name} says HELLO!')
```
### 4 Урок
+ Разработка калькулятора
+ Тестирование калькулятора
+ Более сложные автотесты
+ Маркеры и параметризация тестов  
  ***Пример***
```
@pytest.mark.negative
@pytest.mark.parametrize('input, output, expectation', [
    ('!you', '!you', does_not_raise()),
    ('12level', '12level', does_not_raise()),
    (None, None, pytest.raises(AttributeError)),
    ])
def test_check_capitilize_negative(input, output, expectation):
    with expectation:
        result = StringUtils().capitilize(input)
        assert output == result
```
### 5 Урок
+ Знакомство с Selenium
+ Базовые методы Selenium
+ Локаторы
+ Автоматизация сбора данных  
  ***Пример***
```
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1980,1080")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'http://the-internet.herokuapp.com/entry_ad'

driver.get(url)

button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(('xpath', "//p[text()='Close']"))
    )
button.click()
```
### 6 Урок
+ Методы get_title и current_url
+ Работа с cookie
+ Изменение размеров окна браузера
+ Работа с элементами на странице
+ Работа с атрибутами элементов
+ Методы is_enabled, is_displayed и is_selected
+ Работа с вложенными элементами и группами элементов
+ Методы quit и close
+ Ожидания  
  ***Пример***
```
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--ignore-certificate-errors")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 20, poll_frequency=1)
URL = "http://uitestingplayground.com/ajax"

driver.get(URL)

wait.until(EC.url_to_be((URL)))

AJAX_BUTTON = ("xpath", "//button[@id='ajaxButton']")
wait.until(EC.element_to_be_clickable((AJAX_BUTTON))).click()

GREEN_FIELD = ("xpath", "//p[@class='bg-success']")
GREEN_FIELD_TEXT = wait.until(
    EC.visibility_of_element_located((GREEN_FIELD))
    ).text

print(f'Текст поля - {GREEN_FIELD_TEXT}')
```
### 7 Урок
  ***Пример***
```

```
