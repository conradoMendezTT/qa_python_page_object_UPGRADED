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
         email_field = WebDriverWait(self.driver, 10).until(expected_conditions
                                                            .visibility_of_element_located(self.email_field)) #La funcion recibe una tupla
         email_field.send_keys(email_to_send)

    def send_password(self, password_to_send):
        pass_field = WebDriverWait(self.driver, 10).until(expected_conditions
                                                          .visibility_of_element_located(self.password_field))
        pass_field.send_keys(password_to_send)
        pass_field.clear()

    def click_sign_in_button(self):
        log_in_btn = WebDriverWait(self.driver, 10).until(
            expected_conditions
                .visibility_of_element_located(self.sign_in_button))
        log_in_btn.click()

    def login(self, email, password):
        self.send_email(email)
        self.send_password(password)
        self.click_sign_in_button()

    def is_email_warning_message_displayed(self):
        try:
            email_warning = WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located(self.email_error_warning)
            )
            return email_warning.is_displayed()
        except:
            return False  # Si no se encuentra o no está visible, retorna False

    def is_password_warning_message_displayed(self):
        try:
            email_warning = WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located(self.password_error_warning)
            )
            return email_warning.is_displayed()
        except:
            return False  # Si no se encuentra o no está visible, retorna False

    def get_element_text(self, element):
        try:
            # Si element es un selector (tupla), lo localizamos; si no, asumimos que es un WebElement
            element = (WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(element))
                       if isinstance(element, tuple) else element)

            text = element.text.strip()
            if not text:
                raise ValueError("El elemento no contiene texto visible.")

            return text

        except Exception as e:
            raise RuntimeError(f"Error al obtener el texto del elemento: {e}")

    def element_text_assertion(self, text_to_assert, element):
        assert self.get_element_text(element) == text_to_assert, "El texto del elemento no coincide."

    def signing_button_text_assertion(self):
        sign_in_btn = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.sign_in_button)
        )
        self.element_text_assertion("Iniciar", sign_in_btn)


class TestVenttu:

    driver = None

    @classmethod
    def setup_class(cls):
        # Crea un controlador para Chrome
        cls.driver = webdriver.Chrome()

    #setup_method(self) es un metodo especial de pytest.
    # se ejecuta por cada instancia de la clase de test.
    def setup_method(self):
        self.driver.get('https://login.venttu.com/')
        #Abrir la pestana completa
        self.driver.maximize_window()


    def test_set_email(self):
        # Crea una clase de objeto de página para la página de inicio de sesión
        login_venttu = LoginPageVenttu(self.driver)
        login_venttu.login('correo@electrónico', 'contraseña')


    def test_display_warning_email_box(self):
        login = LoginPageVenttu(self.driver)
        login.click_sign_in_button()
        assert login.is_email_warning_message_displayed() == True

    def test_display_warning_password_box(self):
        login = LoginPageVenttu(self.driver)
        login.send_email("tripleten_cohort_20@POC.com")
        login.click_sign_in_button()
        assert login.is_password_warning_message_displayed() == True

    def test_sign_in_button_text_assertion(self):
        login = LoginPageVenttu(self.driver)
        login.signing_button_text_assertion()


    @classmethod
    def teardown_class(cls):
        #Cerrar el navegador
        cls.driver.quit()
        cls.driver.quit()