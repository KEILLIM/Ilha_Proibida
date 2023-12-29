from enum import Enum


class EnumExt(Enum):
    @classmethod
    def list_values(cls):
        return list(map(lambda c: c.value, cls))
    
    @classmethod
    def list_names(cls):
        return list(map(lambda c: c.name, cls))


class EnumExtLink(Enum):
    @classmethod
    def list_values(cls):
        return list(map(lambda c: c.value, cls))
    
    @classmethod
    def list_names(cls):
        return list(map(lambda c: c.name, cls))

    @classmethod
    def list_links(cls, ext="jpg"):
        list_links = dict()
        for key, value in zip(cls.list_names(), cls.list_values()):
            list_links[key] = f"https://imgur.com/{value}.{ext}"
        return list_links
    
    def link(cls, ext="jpg"):
        return str(f"https://imgur.com/{cls.value}.{ext}")

class EnumTerreno(EnumExtLink):
    PISTA_POUSO = "CU3TLYh"
    PORTAO_BRONZE = "BL6lB7H"
    PALACIO_CORAL = "tLDbzd2"
    VALE_TENEBROSO = "OZE1myn"
    PORTAO_OURO = "J6ow4jR"
    PORTAO_PRATA = "v0g7eGm"
    PORTAO_COBRE = "45aU3nf"
    PORTAO_FERRO = "yKU6ngz"
    ATALAIA = "sdJ4W5O"
    JARDIM_SUSSUROS = "pjVcyoy"
    JARDIM_UIVOS = "ZNuPWqZ"
    TEMPLO_SOL = "O0OSVFt"
    TEMPLO_LUA = "J160xpm"
    CAVERNA_LAVA = "2j1IAyf"
    CAVERNA_SOMBRAS = "b4xtltc"
    OBSERVATORIO = "E9MflTP"
    PANTANO_BRUMAS = "NDioDZg"
    ROCHA_FANTASMA = "TCmLjeT"
    PALACIO_MARES = "rYxQaTa"
    PENEDO_BALDIO = "MvN7kTU"
    BOSQUE_CARMESIM = "Uni02EK"
    DUNAS_ENGANO = "cG5UYCf"
    PONTE_SUSPENSA = "GC8V8CQ"
    LAGOA_PERDIDA = "7o1qq10"


class EnumTesouros(EnumExtLink):
    PEDRA_TERRA = "KXZXTei"
    ESTATUA_VENTO = "qp5Zbn8"
    CRISTAL_FOGO = "LK4p1xG"
    CALICE_OCEANO = "rUNsKEH"

class EnumCartas(EnumExtLink):
    # Do Baralho
    HELICOPTERO = "H"
    SACO_DE_AREIA = "SA"
    ENCHENTE = "E"

TerrenoComTesouro = {
    EnumTerreno.JARDIM_SUSSUROS: EnumTesouros.ESTATUA_VENTO,
    EnumTerreno.JARDIM_UIVOS: EnumTesouros.ESTATUA_VENTO,
    EnumTerreno.TEMPLO_SOL: EnumTesouros.PEDRA_TERRA,
    EnumTerreno.TEMPLO_LUA: EnumTesouros.PEDRA_TERRA,
    EnumTerreno.CAVERNA_LAVA: EnumTesouros.CRISTAL_FOGO,
    EnumTerreno.CAVERNA_SOMBRAS: EnumTesouros.CRISTAL_FOGO,
    EnumTerreno.PALACIO_CORAL: EnumTesouros.CALICE_OCEANO,
    EnumTerreno.PALACIO_MARES: EnumTesouros.CALICE_OCEANO
}
   
class EnumEstadosTerrenos(EnumExt):
    OCEANO_TESOURO = -1
    SECO = 0
    ALAGADO = 1
    AFUNDADO = 2


class EnumPeao(EnumExtLink):
    PAWN = "zO3kiRp"


class EnumOceano(EnumExtLink):
    OCEANO = "gVHmY2v"


if __name__ == "__main__":
    print(EnumTerreno.list_names())
    