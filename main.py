Customer = str(input("Enter customer name: "))
Product = str(input("Enter product name: "))
price = float(input("Enter price per unit (KZT): "))
quantity = int(input("Enter quantity: "))

subtotal = price * quantity

if subtotal > 5000:
    discount = subtotal * 0.10
    total = subtotal - discount
else:
    discount = 0
    total = subtotal

print("=" * 30)
print("        SHOP RECEIPT")
print("=" * 30)
print(f"Customer: {Customer}")
print(f"Product: {Product}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print("-" * 30)
print(f"Subtotal: {subtotal}")
print(f"Discount: {discount}")
print(f"Total: {total}")
print("=" * 30)

print("Discount applied:", subtotal > 5000)
print("Paid more than 3000:", total > 3000)