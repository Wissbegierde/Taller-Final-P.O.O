import random, sys

class Carta:
    def __init__(self, numero, palo):
        if numero == 1:
            self.numero = 'A'
        elif numero == 11:
            self.numero = 'J'
        elif numero == 12:
            self.numero = 'Q'
        elif numero == 13:
            self.numero = 'K'
        else:
            self.numero = numero
        self.palo = palo
    
    def is_figura(self):
        if self.numero == 'A':
            return False
        elif ['J','Q','K'].count(self.numero) == 1:
            return True
        else:
            return False
        
    def get_valor(self):
        if self.numero == 'A':
            opt = int(input("La carta es un As, desea que tenga un valor de 1 o 11?"))
            if opt != 1 and opt != 11:
                print("Error")
                sys.exit(-1)
            else:
                return opt    
            
        elif self.is_figura():
            return 10
        else:
            return self.numero
    
    def is_as(self):
        return self.numero == 1
        
    def __str__(self):
        return "{}{}".format(self.numero, self.palo)

class Baraja:
    def __init__(self):
        
        palo1 = []
        palo2 = []
        palo3 = []
        palo4 = []
        for i in range(1,14):
            palo1.append(Carta(i, '♠'))
            palo2.append(Carta(i, '♡'))
            palo3.append(Carta(i, '♣'))
            palo4.append(Carta(i, '♢'))
        random.shuffle(palo1)
        random.shuffle(palo2)
        random.shuffle(palo3)
        random.shuffle(palo4)
        self.baraja = palo1+palo2+palo3+palo4
        random.shuffle(self.baraja)
        #for c in self.baraja:
        #    print("{} , {}".format(c.numero, c.palo))
    
    def obtener_carta(self):
        carta = self.baraja.pop(len(self.baraja)-1)
        return carta

class Juego:
    def __init__(self):
        jugadores = int(input("¿Cuantos jugadores jugarán?: "))
        
        self.baraja = Baraja()
        self.jugadores = [0] * jugadores
        self.turno = 0
        
    def jugar_turno(self):
        
        print("Turno del jugador {}.".format(self.turno+1))
        opt = input("El puntaje del jugador {} es {}, ¿Desea pedir una carta? Y/N \n".format(self.turno+1, self.jugadores[self.turno]))
        if opt == 'N':
            return
        
        carta = self.baraja.obtener_carta()
        print("La carta obtenida es {}.".format(carta))
        self.jugadores[self.turno] += carta.get_valor()
        print("Ahora el puntaje del jugador {} es {}.".format(self.turno+1, self.jugadores[self.turno]))
        if self.jugadores[self.turno]>21:
            print("El jugador {} ha perdido.".format(self.turno+1))
            self.jugadores[self.turno] = -1
        self.verificar_ganador()
        
        self.avanzar_turno()
    
    def avanzar_turno(self):
        self.turno += 1
        if self.turno == len(self.jugadores):
            self.turno = 0
        while self.jugadores[self.turno]==-1:
            self.turno += 1
            if self.turno == len(self.jugadores):
                self.turno = 0
    
    def verificar_ganador(self):
        jugadores_jugando = []
        i = 1
        for jugador in self.jugadores:
            if jugador != -1:
                par = []
                par.append(i)
                par.append(jugador)
                jugadores_jugando.append(par)
            i += 1
        if len(jugadores_jugando)==1 :
            print("¡El jugador {} ha ganado! con una puntuación de {}.".format(jugadores_jugando[0][0], jugadores_jugando[0][1]))
            sys.exit(0)
        
juego = Juego()
while True:
    print("Para jugar un turno, presione cualquier tecla y Enter.")
    print()
    x = input("")
    juego.jugar_turno()