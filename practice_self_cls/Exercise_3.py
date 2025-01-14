# Ejercicio 3: Configuración Global
# Objetivo: Usar métodos de clase para manejar configuraciones globales.
# Tarea:
# Crea una clase Config con atributos de clase setting1 y setting2.
# Agrega métodos de clase set_config y show_config para modificar e imprimir estas configuraciones.
# Modifica las configuraciones globalmente y muestra cómo afectan a diferentes instancias.



class Config:
    setting1 = 0
    setting2 = 0

    @classmethod
    def set_config(cls, new_setting1_config_code, new_setting2_config_code):
        cls.setting1 = new_setting1_config_code
        cls.setting2 = new_setting2_config_code

    @classmethod
    def show_config(cls):
        print(f"Currently configuration is {cls.setting1} and {cls.setting2}")



configuration_1 = Config()
configuration_1.show_config()

configuration_1.set_config(12 , 13)
configuration_1.show_config()