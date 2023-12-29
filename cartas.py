from terrenos import Terreno
from estados import EnumEstadosTerrenos

class Carta():
    def __init__(self, face):
        self.face = face
        pass

class CartaTesouro(Carta):
    pass


class CartaEnchente(Carta):
    pass


class CartaSacoDeAreia(Carta):
    pass


class CartaFugaHelicoptero(Carta):
    pass


class CartaAlagamento():
    """
    Cada carta de alagamento representa um terreno, para facilitar acesso a ações do terreno
    iremos receber como parametro o terreno representado pela carta
    """
    def __init__(self, terreno: Terreno):
        self.terreno = terreno

    def afundar(self):
        if self.terreno.get_estado() == EnumEstadosTerrenos.SECO:
            self.terreno.set_estado(EnumEstadosTerrenos.ALAGADO)
        elif self.terreno.get_estado() == EnumEstadosTerrenos.ALAGADO:
            self.terreno.set_estado(EnumEstadosTerrenos.AFUNDADO)
        else:
            print("Estado do terreno invalido!")

        
    
