#!/bin/python3

"""

"""
class Cart:
    __total_cost: float
    __shopping_cart = []

    def add_to_cart(self, item: list[{str, str, int, float}]) -> None:
        self.__shopping_cart.append(item)

    def print_cart_items(self):
        for item in self.__shopping_cart:
            print(item)

    def remove_from_cart(self, item_no: str):
        for item in self.__shopping_cart:
            pass