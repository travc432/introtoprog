# Type code for classes here
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        # def __mul__(self):
        # print_item_cost = (self.item_quantity * self.item_price)
        # return '{} {} @ ${} = ${}' .format(self_item_name, self.item_quantity, self.item_price, print_item_cost)

    def print_item_cost(self):
        print_cost = (self.item_quantity * self.item_price)
        print(('{} {} @ ${} = ${}') .format(self.item_name, self.item_quantity, self.item_price, print_cost))


def main():
    print('Item 1')
    name = input('Enter the item name:\n')
    price = int(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n\n'))
    item1 = ItemToPurchase(name, price, quantity)

    print('Item 2')
    name = input('Enter the item name:\n')
    price = int(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n\n'))
    item2 = ItemToPurchase(name, price, quantity)

    print('TOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    print('Total: {}' .format((item1.print_item_cost(print_item_cost(print_cost)) + item2.print_item_cost(print_cost))))

if __name__ == "__main__":

    main()

# Type main section of code here