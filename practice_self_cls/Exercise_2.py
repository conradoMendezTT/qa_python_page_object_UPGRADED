# Ejercicio 2: Contador de Instancias
# Objetivo: Entender cómo los métodos de clase pueden manipular atributos de clase para llevar un registro.
# Tarea:
# Crea una clase Counter con un atributo de clase count inicializado en 0.
# Incrementa count cada vez que se crea una nueva instancia de Counter.
# Crea un método de clase reset_count que reinicie el contador a 0.
# Crea varias instancias y muestra cómo cambia count.



class Counter:
    count = 0

    @classmethod
    def reset_count(cls):
        cls.count = 0

    def __init__(self):
        Counter.count += 1
        print(f"Contador de intancia: {Counter.count}")



instance_1 = Counter()
instance_2 = Counter()

print("Reseteando atributos de clase")

instance_1.reset_count()

instance_3= Counter()
