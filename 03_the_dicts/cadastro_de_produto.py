#!/usr/bin/env python3
"""Cadastro de produto"""
__version__ = "0.1.0"

from pprint import pprint

produto = {
    "nome": "Caneta",
    "cores": ["azul", "branco"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8,
    },
    "em_estoque": True,
    "codigo": 45678,
    "codebar": None,
}

cliente = {"nome": "jhon"}

compra = {"cliente": cliente, "produto": produto, "quantidade": 3}

# pprint(compra)

total_compra = compra["quantidade"] * compra["produto"]["preco"]

# Extract values for better readability
cliente_nome = compra["cliente"]["nome"]
produto_nome = compra["produto"]["nome"]
quantidade = compra["quantidade"]

print(
    f"O cliente {cliente_nome}"
    f" comprou {quantidade} unidades de {produto_nome}"
    f" e pagou o total de {total_compra}"
)
