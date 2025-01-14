
# Ejercicio 1: Atributos de Clase e Instancia Básicos
# Objetivo: Practicar la creación y modificación de atributos de clase e instancia.
# Tarea:
# Crea una clase Person con un atributo de clase species con el valor "Homo sapiens".
# Añade un atributo de instancia name que se inicialice en el constructor.
# Crea un método de clase change_species que cambie species.
# Crea un método de instancia que imprima name y species.
# Crea instancias, modifica el species, y observa cómo cambian los atributos.

class Person:
    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name


    @classmethod
    def change_species(cls, new_specie):
        cls.species = new_specie

    def print_name_and_species(self):
        name_instancia = self.name
        name_clase = self.species

        print(f"El elemento de instancia es {name_instancia} y el de la clase es {name_clase}")


person_1 = Person("Conrado")
person_1.print_name_and_species()

person_1.change_species("Humano")
person_1.print_name_and_species()


