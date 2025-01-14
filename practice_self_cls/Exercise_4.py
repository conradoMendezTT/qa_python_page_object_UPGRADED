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
        Calculator.history.append(number_to_add)
        for i in Calculator.history:

            print(f"Actual history values are {i}" )

    def substract (self, number_to_remove):
        history = Calculator.history

        for i in history:
            if i == number_to_remove:
                history.remove(i)

calc_1 = Calculator()

calc_1.add(1)
calc_1.add(4)
calc_1.add(6)

