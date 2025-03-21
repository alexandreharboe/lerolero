#!/usr/bin/python3
"""Gerador de lero-lero

Gera frases de efeito sem significado real."""

import random

#Cada frase é composta por três partes aleatórias; aqui
# listas de possibilidades para cada uma das partes.

parte1 = [
	"O sistema em desenvolvimento",
	"O novo protocolo de comunicação",
	"O algoritmo otimizado"
]
parte2 = [
	"possui excelente desempenho",
	"oferece garantia de precisão acima da média",
	"preenhce uma lacuna significativa"
]
parte3 = [
	"nas aplicações a que se destina",
	"em relação às opções disponíveis no mercado",
	", provendo ampla vantagem competitiva a seus usuário"
]

#combina partes aleatoriamente
print (random.choice(parte1), random.choice(parte2), random.choice(parte3))
