from estados import EnumTerreno, TerrenoComTesouro, EnumEstadosTerrenos, EnumOceano

class Terreno():
    """ Terrenos da ilha definidos no EnumTerrenos seus tipos.

    :param local: 
    :param estado: Estados definidos no EnumEstadosTerrenos
    :param posx: Coordenada x do terreno.
    :param posy: Coordenada y do terreno.
    """
    def __init__(self, tipo_terreno: EnumTerreno, estado):
        self.tipo_terreno = tipo_terreno
        self._estado = estado 
        self.posx = -1
        self.posy = -1

        # Atribui tesouro automaticamente
        if tipo_terreno in TerrenoComTesouro.keys():
            self.tesouro = TerrenoComTesouro[tipo_terreno]
        else:
            self.tesouro = None

    def set_posicao(self, posx, posy):
        self.posx = posx
        self.posy = posy
    
    def get_posicao(self):
        return self.posx, self.posy
    
    def set_estado(self, estado):
        if estado in EnumEstadosTerrenos:
            if not(self.tipo_terreno in EnumOceano.list_names()):
                self._estado = estado
            else:
                print("Terreno é oceano, nao pode ter estado mudado")
        else:
            print("Estado invalido")

    def get_estado(self):
        return self._estado
