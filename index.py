from ilha import IlhaProibida
from canvas import Canvas

from estados import EnumTerreno, EnumEstadosTerrenos


if __name__ == "__main__":
    ilha = IlhaProibida()

    canvas = Canvas()

    for t in ilha.terrenos:
        if t.tipo_terreno == EnumTerreno.PALACIO_CORAL:
            print("To no palacio")
            t.set_estado(EnumEstadosTerrenos.AFUNDADO)

        if t.tipo_terreno == EnumTerreno.CAVERNA_LAVA:
            print("To na caverna")
            t.set_estado(EnumEstadosTerrenos.ALAGADO)
        
        canvas.draw_island(t)