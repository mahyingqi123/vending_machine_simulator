class Item:
    # Class represents item to be sold
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'{self.name} - RM{self.price}'

