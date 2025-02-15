from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Clase para la página de inicio de sesión
class LoginPageAround:
    email_field = (By.ID, 'email')
    password_field = (By.ID, 'password')
    sign_in_button = (By.CLASS_NAME, 'auth-form__button')

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_sign_in_button()

# Clase para el encabezado
class HeaderPageAround:
    header_user = (By.CLASS_NAME, 'header__user')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_header(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.header_user))

    def email_in_header(self):
        return self.driver.find_element(*self.header_user).text

# Clase con la prueba automatizada
class TestAround:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    def test_check_email_in_header(self):
        self.driver.get('https://around-v1.es.practicum-services.com/')

        login_page = LoginPageAround(self.driver)
        email = "Introduce tu correo electrónico"
        password = "Introduce tu contraseña"
        login_page.login(email, password)

        header_page = HeaderPageAround(self.driver)
        header_page.wait_for_load_header()
        email_from_header = header_page.email_in_header()

        assert email_from_header == email

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()