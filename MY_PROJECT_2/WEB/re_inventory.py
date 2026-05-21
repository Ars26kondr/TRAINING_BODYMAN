class items:
    def __init__(self, name, height, width, symbol):
        self.name=name
        self.height=height
        self.width=width
        self.symbol=symbol
class inventory:
    def __init__(self, height, width):
        self.vault=[]
        for i in range(height):
            row=[]
            for a in range(width):
                row.append("*")
            self.vault.append(row)
    def show_inventory(self):
        for i in self.vault:
            print(i)
inv=inventory(3,5)
inv.show_inventory()
print("")
inv1=inventory(2,7)
inv1.show_inventory()