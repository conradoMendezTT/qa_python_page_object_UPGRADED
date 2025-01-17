# Ejercicio 4: Métodos de Instancia vs Métodos de Clase
# Objetivo: Diferenciar claramente entre métodos de instancia y métodos de clase.
# Tarea:
# Crea una clase Calculator con un atributo de clase history (lista vacía).
# Agrega métodos de instancia para add y subtract, que modifiquen history con la operación realizada.
# Agrega un método de clase clear_history para reiniciar la historia.
# Crea instancias, realiza operaciones, y muestra cómo history refleja las operaciones realizadas.


class Calculator:
    history = []

    def add (self, number_to_add):
       # Calculator.history.append(number_to_add) # --> Accedo al atributo de otra manera
        self.history.append(number_to_add)
        #for i in Calculator.history:
        print(self.history)
           # print(f"Actual history values are {i}" )

    def subtract (self, number_to_remove):
        history = Calculator.history

        for i in history:
            if i == number_to_remove:
                history.remove(i)

        print(f"El nuevo history que tenemos es: {self.history}")

        print(history)
    @classmethod
    def clear_history (cls):
        cls.history.clear()


#Creating Instances = Objects
calc_1= Calculator()
calc_2 = Calculator()
calc_3 = Calculator()

#Adding numbers of instances / methods
calc_1.add(12)
calc_2.add(124)
calc_3.add(1234)


#Substracting numbers of instances / methods
calc_1.subtract(12)

#Cleaning Class attribute
print("Borrando el history....")
Calculator.clear_history()


print(f"El history ahora es {Calculator.history}")

