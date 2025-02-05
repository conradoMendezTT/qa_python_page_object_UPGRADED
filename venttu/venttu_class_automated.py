from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LoginPageVenttu:

    email_field = (By.ID, "Usuario")
    password_field = (By.ID, "Password")
    sign_in_button = (By.ID, "signInBtn")
    email_error_warning = (By.ID, "warningUsuario")
    password_error_warning = (By.ID, "warningPassword")

    def __init__(self, driver):
        self.driver = driver

    def send_email(self, email_to_send):
         email_field = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.email_field)) #La funcion recibe una tupla
         email_field.send_keys(email_to_send)

    def send_password(self, password_to_send):
        pass_field = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.password_field))
        pass_field.send_keys(password_to_send)

    def click_sign_in_button(self):
        log_in_btn = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.sign_in_button))
        log_in_btn.click()

    def login(self, email, password):
        self.send_email(email)
        self.send_password(password)
        self.click_sign_in_button()


class TestVenttu:

    driver = None

    @classmethod
    def setup_class(cls):
        # Crea un controlador para Chrome
        cls.driver = webdriver.Chrome()

    def test_set_email(self):
        # Abre la página de la aplicación de prueba
        self.driver.get('https://around-v1.es.practicum-services.com/')

        # Crea una clase de objeto de página para la página de inicio de sesión
        login_venttu = LoginPageVenttu(self.driver)
        # Iniciar sesión
        login_venttu.login('correo@electrónico', 'contraseña')

        # Utiliza assert para comprobar que el valor actual de Ocupación coincida con el valor esperado

       #METERALGUNA ASSERTION ACA PARA EL ERROR EN PANTALLA

    def test_display_warning_email_box(self):

    def test_display_warning_password_box(self):


    @classmethod
    def teardown_class(cls):
        # cerrar el navegador
        cls.driver.quit()