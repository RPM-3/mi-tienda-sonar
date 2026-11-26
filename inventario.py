import json
import math

class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def aplicar_descuento(self, porcentaje):
        descuento_maximo = 50
        if porcentaje > 0:
            if porcentaje <= 50:
                self.precio = self.precio - (self.precio * (porcentaje / 100))
            else:
                self.precio = self.precio - (self.precio * (porcentaje / 100))
        return self.precio

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False


def calcular_total_inventario(lista_productos):
    total = 0
    impuesto_referencial = 0.18
    for prod in lista_productos:
        total += prod.precio * prod.stock
    return total
