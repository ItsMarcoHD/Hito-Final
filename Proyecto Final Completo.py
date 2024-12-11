class Reserva:
    def __init__(self, tipo, precio):
        self.tipo = tipo
        self.precio = precio

class ReservaExcursion(Reserva):
    def __init__(self, lugar, precio_por_persona, personas):
        super().__init__('Excursión', precio_por_persona * personas)
        self.lugar = lugar
        self.personas = personas

    def __str__(self):
        return f"Excursión: {self.lugar}, Personas: {self.personas}, Precio Total: ${self.precio}"

class ReservaComida(Reserva):
    def __init__(self, tipo_comida, precio_por_persona, personas):
        super().__init__('Comida', precio_por_persona * personas)
        self.tipo_comida = tipo_comida
        self.personas = personas

    def __str__(self):
        return f"Comida: {self.tipo_comida}, Personas: {self.personas}, Precio Total: ${self.precio}"

class ReservaAlojamiento(Reserva):
    def __init__(self, tipo_habitacion, noches, precio_por_noche):
        super().__init__('Alojamiento', precio_por_noche * noches)
        self.tipo_habitacion = tipo_habitacion
        self.noches = noches

    def __str__(self):
        return f"Alojamiento: {self.tipo_habitacion}, Noches: {self.noches}, Precio Total: ${self.precio}"

class SistemaReservas:
    def __init__(self):
        self.reservas = []

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)
        print(f"Reserva de {reserva.tipo} agregada exitosamente.")

    def mostrar_reservas(self):
        if not self.reservas:
            print("No hay reservas.")
            return
        for reserva in self.reservas:
            print(reserva)

    def calcular_precio_total(self):
        return sum(reserva.precio for reserva in self.reservas)

    def procesar_pago(self, metodo_pago):
        precio_total = self.calcular_precio_total()
        print(f"Procesando pago de ${precio_total} mediante {metodo_pago}...")
        print("Pago realizado con éxito.")

def menu():
    sistema = SistemaReservas()

    comidas = [("Buffet", 20.0), ("Comida rápida", 10.0), ("Gourmet", 50.0)]
    alojamientos = [("Habitación individual", 30.0), ("Habitación doble", 50.0), ("Suite", 100.0)]
    excursiones = [("Volcán Villarrica", 50.0), ("Lago Villarrica", 30.0), ("Playa Grande Lican-Ray", 20.0)]

    while True:
        print("\n1. Reservar Excursión")
        print("2. Reservar Comida")
        print("3. Reservar Alojamiento")
        print("4. Ver Reservas")
        print("5. Calcular Precio Total")
        print("6. Pagar")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            print("\nOpciones de excursión:")
            for i, (lugar, precio) in enumerate(excursiones, 1):
                print(f"{i}. {lugar} (${precio} por persona)")
            seleccion = int(input("Elige un lugar para la excursión (1-3): "))
            if 1 <= seleccion <= len(excursiones):
                lugar, precio_por_persona = excursiones[seleccion - 1]
                personas = int(input("Cantidad de personas: "))
                excursion = ReservaExcursion(lugar, precio_por_persona, personas)
                sistema.agregar_reserva(excursion)
            else:
                print("Selección no válida.")

        elif opcion == '2':
            print("\nOpciones de comida:")
            for i, (tipo, precio) in enumerate(comidas, 1):
                print(f"{i}. {tipo} (${precio} por persona)")
            seleccion = int(input("Elige un tipo de comida (1-3): "))
            if 1 <= seleccion <= len(comidas):
                tipo_comida, precio_por_persona = comidas[seleccion - 1]
                personas = int(input("Cantidad de personas: "))
                comida = ReservaComida(tipo_comida, precio_por_persona, personas)
                sistema.agregar_reserva(comida)
            else:
                print("Selección no válida.")

        elif opcion == '3':
            print("\nOpciones de alojamiento:")
            for i, (tipo, precio) in enumerate(alojamientos, 1):
                print(f"{i}. {tipo} (${precio} por noche)")
            seleccion = int(input("Elige un tipo de alojamiento (1-3): "))
            if 1 <= seleccion <= len(alojamientos):
                tipo_habitacion, precio_por_noche = alojamientos[seleccion - 1]
                noches = int(input("Cantidad de noches: "))
                alojamiento = ReservaAlojamiento(tipo_habitacion, noches, precio_por_noche)
                sistema.agregar_reserva(alojamiento)
            else:
                print("Selección no válida.")

        elif opcion == '4':
            sistema.mostrar_reservas()

        elif opcion == '5':
            print(f"Precio total de todas las reservas: ${sistema.calcular_precio_total()}")

        elif opcion == '6':
            print("\nMétodos de pago disponibles:")
            metodos_pago = ["Tarjeta de crédito", "PayPal", "Transferencia bancaria"]
            for i, metodo in enumerate(metodos_pago, 1):
                print(f"{i}. {metodo}")
            seleccion = int(input("Selecciona un método de pago (1-3): "))
            if 1 <= seleccion <= len(metodos_pago):
                metodo_pago = metodos_pago[seleccion - 1]
                sistema.procesar_pago(metodo_pago)
            else:
                print("Método de pago no válido.")

        elif opcion == '7':
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
