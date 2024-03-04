## Проект по тестированию сайта SuperJob.ru
> <a target="_blank" href="https://superjob.ru/">Ссылка на сайт</a>

#### Список проверок, реализованных в web автотестах
- [x] Проверка доступности вкладки "реклама" на главной странице
- [x] Проверка поиска по типу "резюме или вакансия"
- [x] Проверка поиска вакансий по смене региона
- [x] Проверка авторизации
- [x] Проверка logout
- [x] Проверка создания аккаунта
- [x] Проверка отклика на вакансию
- [x] Проверка создания резюме
- [x] Проверка создания и скрытия резюме из отображаемых

#### Список проверок, реализованных в mobile автотестах
- [x] Проверка авторизации
- [x] Проверка поиска вакансии при авторизованном пользователе
- [x] Проверка поиска вакансии при неавторизованном пользователе
- [x] Проверка информации о компании SJ
- [x] Проверка меню откликов вприложении

#### Список проверок, реализованных в api автотестах
- [x] Проверка успешного получения списка вакансий
- [x] Проверка успешного запроса на восстановление пароля
- [x] Проверка некорректного запроса на обновление токена
- [x] Проверка некорретного запроса на удаление профиля компании

### Структура проекта

### Проект реализован с использованием
Python Pytest PyCharm Selenoid Selene Jenkins Allure Report Telegram AllureTestOps 

<img src="/resources/python-original.svg" alt="Image 1" width="45" height="45"><img src="/resources/pytest-original.svg" alt="Image 2" width="45" height="45"><img src="/resources/PyCharm_Icon.svg" alt="Image 3" width="45" height="45"><img src="/resources/selenoid.png" alt="Image 4" width="45" height="45"><img src="/resources/jenkins-original.svg" alt="Image 5" width="45" height="45">
<img src="/resources/allure.png" alt="Image 6" width="45" height="45"><img src="/resources/telegram.svg" alt="Image 7" width="45" height="45"><img src="/resources/AllureTestOps.png" alt="Image 8" width="45" height="45">

# Для запуска автотестов используется Jenkins

### Для запуска автотестов в Jenkins
#### 1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/Graduation_Project_AQA/">проект</a>

![This is an image](/resources/screens/jenkins_main.png)

#### 2. Выбрать пункт **Собрать с параметрами**
#### 3. В случае необходимости изменить версию браузера
#### 4. Нажать **Собрать**
#### 5. Результат запуска сборки можно посмотреть в отчёте Allure

![This is an image](/resources/screens/allure_report.png)

### Локальный запуск автотестов
1. Клонируйте репозиторий на свой локальный компьютер при помощи git clone
2. Создайте и активируйте виртуальное окружение
  ```bash
  python -m venv .venv
    source .venv/bin/activate
  ```
3. Установите зависимости с помощью poetry
  ```bash
    pip install poetry
    poetry install
  ```
4. Для запусков тестов локально используйте команд:
  ```bash
  pytest -sv tests/mobile/
  pytest -sv tests/ui/
  pytest -sv tests/api/
  ```

Получение отчёта allure:
```bash
allure serve allure-results
```

### Настроено автоматическое оповещение о результатах сборки Jenkins в Telegram-бот
![This is an image](/resources/screens/allure.png)

### Интеграция с jira
![This is an image](/resources/screens/jira.png)

### Интеграция с Allure TestOps
![This is an image](/resources/screens/testops.png)

### Пример видеозаписи прохождения мобильных тестов
![This is an image](/resources/screens/company_info.gif)

### Пример видеозаписи прохождения UI тестов
![This is an image](/resources/screens/mobile_login.gif)
