from Item import Item

class VendingMachine:
    # Class represents vending machine logic

    def __init__(self) -> None:
        # Initialize vending machine with items and notes
        self.items = [Item('Coke', 25), Item('Pepsi', 35), Item('Soda', 45)]
        self.notes = [1, 5, 10, 20, 50, 100]
        self.item_selected = None
        self.amount_inserted = 0

    def __str__(self) -> str:  
        return "Items Available: \n"+'\n'.join([str(item) for item in self.items])
    
    def select_item(self, item_index: int):
        # Select item to purchase
        self.item_selected = item_index
        return self.item_selected.price <= self.amount_inserted

    def dispense_item(self):
        # Dispense item and return change
        item = self.item_selected
        change = self.calculate_change()
        return (item,change)

    def insert_note(self, note: int):
        # Insert note into vending machine
        item = self.item_selected
        self.amount_inserted = note + self.amount_inserted
        if item is not None and self.amount_inserted >= item.price:
            print(f'{item.name} dispensed')
            return True
        return False
    
    def calculate_change(self):
        # Calculate change to return
        item = self.item_selected   
        amount = self.amount_inserted - item.price
        change = []
        for note in self.notes[::-1]:
            combo = [note,amount//note]
            amount = amount%note
            change.append(combo)
            if amount == 0:
                break
        self.amount_inserted = 0
        return change



