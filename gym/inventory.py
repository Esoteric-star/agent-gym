"""Tiny stock inventory."""


class Inventory:
    def __init__(self):
        self._stock = {}

    def add(self, sku, qty):
        if qty <= 0:
            raise ValueError("qty must be positive")
        self._stock[sku] = self._stock.get(sku, 0) + qty

    def remove(self, sku, qty):
        if qty <= 0:
            raise ValueError("qty must be positive")
        if sku not in self._stock:
            raise KeyError(f"unknown sku: {sku}")
        if qty > self._stock[sku]:
            raise ValueError("qty exceeds stock")
        self._stock[sku] -= qty
        if self._stock[sku] == 0:
            del self._stock[sku]

    def count(self, sku):
        return self._stock.get(sku, 0)

    def skus(self):
        return sorted(self._stock.keys())
