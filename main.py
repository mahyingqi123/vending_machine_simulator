from VendingMachine import VendingMachine
import tkinter as tk


if __name__ == '__main__':
    vending_machine = VendingMachine()
    def dispense_item():
        # dispense item when amount inserted is enough
        item, change = vending_machine.dispense_item()
        item_dispensed_slot.config(text=item.name)
        change = '\n'.join([f'RM{note} - {count}' for note, count in change if count > 0])
        change_slot.config(text=change)
        amount_inserted.config(text=0)
        remaining_amount.config(text=0)
    
    def select_item(item):
        # select item to purchase
        item_dispensed_slot.config(text="")
        change_slot.config(text="")
        item_dispensed = vending_machine.select_item(item)
        item_selected.config(text=item.name)
        remaining_amount.config(text=item.price - vending_machine.amount_inserted)
        if item_dispensed:
            dispense_item()

    def insert_note(note):
        # insert note into vending machine
        print(type(note), note)
        item_dispensed = vending_machine.insert_note(note)
        amount_inserted.config(text=vending_machine.amount_inserted)
        if vending_machine.item_selected is not None:
            remaining_amount.config(text=vending_machine.item_selected.price - vending_machine.amount_inserted)
        if item_dispensed:
            dispense_item()
    
    # basic UI stuff
    ui = tk.Tk()
    ui.title('Vending Machine')
    ui.geometry('300x700')
    items_title = tk.Label(ui, text='Items Available:')
    items_title.pack()
    for item in vending_machine.items:
        item_label = tk.Button(ui, text=str(item), command=lambda item = item:select_item(item))
        item_label.pack()
    
    notes_title = tk.Label(ui, text='Insert Notes:')
    notes_title.pack(pady=10)
    for note in vending_machine.notes:
        note_button = tk.Button(ui, text=f'Insert RM{note}', command=lambda note=note: insert_note(note))
        note_button.pack()
    
    item_selected_title = tk.Label(ui, text='Selected Item:')
    item_selected_title.pack(pady=10)
    item_selected = tk.Label(ui, text="None")
    item_selected.pack()

    amount_inserted_title = tk.Label(ui, text='Amount Inserted:')
    amount_inserted_title.pack(pady=10)
    amount_inserted = tk.Label(ui, text="0")
    amount_inserted.pack()
    remaining_amount_title = tk.Label(ui, text='Remaining Amount:')
    remaining_amount_title.pack(pady=10)
    remaining_amount = tk.Label(ui, text="0")
    remaining_amount.pack()

    item_dispensed_title = tk.Label(ui, text='Item Dispensed:')
    item_dispensed_title.pack(pady=10)
    item_dispensed_slot = tk.Label(ui, text="")
    item_dispensed_slot.pack()
    change_title = tk.Label(ui, text='Change:')
    change_title.pack(pady=10)
    change_slot = tk.Label(ui, text="")
    change_slot.pack()

    ui.mainloop()