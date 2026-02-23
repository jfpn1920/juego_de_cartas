import random
class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor
    def __str__(self):
        return f"{self.valor} de {self.palo}"
class Baraja:
    def __init__(self):
        self.palos = ["corazones", "diamantes", "treboles", "picas"]
        self.valores = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
            "7": 7, "8": 8, "9": 9, "10": 10,
            "J": 11, "Q": 12, "K": 13, "A": 14
        }
        self.cartas = []
        self.crear_baraja()
    def crear_baraja(self):
        for palo in self.palos:
            for valor in self.valores:
                carta = Carta(palo, valor)
                self.cartas.append(carta)
    def mezclar(self):
        random.shuffle(self.cartas)
    def repartir_carta(self):
        if self.cartas:
            return self.cartas.pop()
        else:
            return None
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carta = None
    def recibir_carta(self, carta):
        self.carta = carta
    def mostrar_carta(self):
        if self.carta:
            print(f"{self.nombre} recibió: {self.carta}")
def jugar():
    print(" juegos de cartas \n")
    nombre1 = input("ingrese nombre del jugador 1: ")
    nombre2 = input("ingrese nombre del jugador 2: ")
    jugador1 = Jugador(nombre1)
    jugador2 = Jugador(nombre2)
    baraja = Baraja()
    baraja.mezclar()
    jugador1.recibir_carta(baraja.repartir_carta())
    jugador2.recibir_carta(baraja.repartir_carta())
    jugador1.mostrar_carta()
    jugador2.mostrar_carta()
    valores = baraja.valores
    valor1 = valores[jugador1.carta.valor]
    valor2 = valores[jugador2.carta.valor]
    print("\n resultado:")
    if valor1 > valor2:
        print(f" {jugador1.nombre} gana la partida!")
    elif valor2 > valor1:
        print(f" {jugador2.nombre} gana la partida!")
    else:
        print("es un empate!")
jugar()