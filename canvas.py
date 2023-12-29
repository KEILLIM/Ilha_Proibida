"""
Baseado na implementação: https://github.com/Finn-Ko/IlhaProibidaPage/blob/main/page/pySrc/canvas.py
"""

from browser import document, window, html

from terrenos import Terreno
from estados import EnumEstadosTerrenos

class Canvas:
    def __init__(self):
        """
        Inicializa a instância da classe Canvas.

        Cria uma instância do Canvas, obtendo o elemento canvas do documento HTML
        e o contexto 2D associado para desenho.

        """
        self.__canvas__ = document['gameCanvas']
        self.__ctx__ = self.__canvas__.getContext('2d')

    def draw_island(self, terrain : Terreno):
        """
        Desenha uma ilha no canvas.

        Args:
            island (objeto): Instância da classe que representa uma ilha.

        """
        img = window.Image.new()
        img.src = terrain.tipo_terreno.link()

        def on_image_load(e):
            """
            Manipula o evento de carregamento da imagem.

            Esta função é chamada quando a imagem da ilha termina de carregar.
            Ela desenha a ilha no canvas com informações sobre jogadores, terreno e outros detalhes.

            Args:
                e (evento): Evento de carregamento da imagem.

            """
            if terrain.get_estado() == EnumEstadosTerrenos.AFUNDADO:
                self.__ctx__.globalAlpha = 0.4
            
            if terrain.get_estado() == EnumEstadosTerrenos.ALAGADO:
                self.__ctx__.globalAlpha = 0

            self.__ctx__.drawImage(img, terrain.posx * 100 + 5, terrain.posy * 100 + 5, 90, 90)
            self.__ctx__.fillStyle = "black"
            self.__ctx__.fillRect(terrain.posx * 100 + 5, terrain.posy * 100 + 80, 90, 15)
            self.__ctx__.fillStyle = "white"
            self.__ctx__.font = "8px Luminari"
            self.__ctx__.fillText(terrain.tipo_terreno.name, terrain.posx * 100 + 10, terrain.posy * 100 + 90, 90, 20)

          
            self.__ctx__.globalAlpha = 1

        img.bind("load", on_image_load)

if __name__ == "__main__":
    Canvas()
