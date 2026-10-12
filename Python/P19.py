"""
While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 1000. If quantity and price per item are input through the keyboard, write a program to calculate the total expenses.
"""

qty = int(input('Enter value of quantity: '))
price = float(input('Enter value of price: '))

discount = 0
if qty > 1000:
    discount = 0.1 * qty * price

total_exp = (qty * price ) - discount
print(f'Total expenses: {total_exp}')