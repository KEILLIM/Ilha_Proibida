# __authors__ Keila, Felipe, Leonardo, Pedro 
"""Página de entrada do jogo Ilha Proibida.

Kanban - https://workflowy.com/s/desenvolvimento-agil/r7b3ywIA9AdE4e21#/fa1fee833e99

EQUIPE Terra 
.. codeauthor:: Keila Lima de Oliveira <keila90.if@gmail.com>
.. codeauthor:: Felipe Nunes <felipenunes.7921@gmail.com>
.. codeauthor:: Leonardo Cesar <leonardocesarc@gmail.com>
.. codeauthor:: Pedro França <pedro.franca@ufrj.br>

Changelog
---------
.. versionadded::    2.0

|   **Open Source Notification:** This file is part of open source program **Ilha Proibida**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""

import random
# import sys, os, re
from estados import (EnumTerreno, EnumEstadosTerrenos, EnumTesouros, EnumPeao, EnumOceano,
                     TerrenoComTesouro, EnumCartas)
from cartas import (CartaTesouro, CartaEnchente, CartaSacoDeAreia, CartaFugaHelicoptero, 
                    CartaAlagamento)
from terrenos import Terreno

from singleton_pattern import singleton


@singleton
class IlhaProibida:
    """
    
    """
    def __init__(self):
        """
        Inicializa a instância do jogo Ilha Proibida.

        Primeiro cria o baralho das cartas de tesouros (TAFV, cinco de cada)

        """
        # 1) preparar baralho de tesouros
        self.baralho_tesouros = [CartaTesouro(face=getattr(EnumTesouros, f)) for f in EnumTesouros.list_names() * 5]
        self.baralho_tesouros += [CartaFugaHelicoptero(face=EnumCartas.HELICOPTERO) for _ in range(0, 3)]
        self.baralho_tesouros += [CartaEnchente(face=EnumCartas.ENCHENTE) for _ in range(0, 3)]
        self.baralho_tesouros += [CartaSacoDeAreia(face=EnumCartas.SACO_DE_AREIA) for _ in range(0, 2)]

        # Embaralha as cartas
        random.shuffle(self.baralho_tesouros)

        # 2) preparar terrenos
        self.TAM_TABULEIRO = 6
        self.oceano = Terreno(tipo_terreno=EnumOceano.OCEANO, estado=EnumEstadosTerrenos.OCEANO_TESOURO)
        self.qtde_oceanos_tab = [2, 1, 0, 0, 1, 2]
        self.terrenos = [Terreno(tipo_terreno=t, estado=EnumEstadosTerrenos.SECO) for t in EnumTerreno]

        # 3) Prepara baralho de alagamento 
        self.baralho_alagamento = [CartaAlagamento(terreno=t) for t in self.terrenos]

        # Embaralha as cartas
        random.shuffle(self.baralho_alagamento)


        # Preparar tesouros
        self.monta_tabuleiro()
        self.imprime_tabuleiro()

    def monta_tabuleiro(self):
        """
        Constroi o tabuleiro para inicio do jogo 
        """
        terrenos_aux = self.terrenos.copy()

        self.tabuleiro = list()
        for l in range(0, self.TAM_TABULEIRO):
            list_cols = list()
            lim_inferior_oceano = self.qtde_oceanos_tab[l]
            lim_superior_oceano = self.TAM_TABULEIRO - self.qtde_oceanos_tab[l]
            
            for c in range(0, self.TAM_TABULEIRO):
                if c >= lim_inferior_oceano and c < lim_superior_oceano:
                    t = random.choice(terrenos_aux)
                    t.set_posicao(l,c)
                    # para evitar repeticao
                    terrenos_aux.remove(t)
                    list_cols.append(t)
                else:
                    list_cols.append(self.oceano)
            
            self.tabuleiro.append(list_cols)

        return self.tabuleiro
    
    def imprime_tabuleiro(self):
        for l in range(0, len(self.tabuleiro)):
            print([t.tipo_terreno.name for t in self.tabuleiro[l]])


class MarcadorNivelEnchente():
    pass


class Peao():
    pass


class Tesouro():
    pass


if __name__ == "__main__":
    #IlhaProibida()
    ilha = IlhaProibida()
    # print("-"*20)
    # ilha2 = IlhaProibida()
    # print(ilha is ilha2)
    print("Terrenos", "-"*20)
    for i in ilha.terrenos:
        print("Tipo Terreno:", i.tipo_terreno, " - Estado: ", i.get_estado().name, " - Posicao Tabuleiro:", i.get_posicao(), i.tesouro)

    print("Cartas", "-"*20)
    for i in ilha.baralho_tesouros:
        print(i.face.name)

    print("Cartas Alagamento", "-"*20)
    for i in ilha.baralho_alagamento:
        print(i.terreno.tipo_terreno.name)