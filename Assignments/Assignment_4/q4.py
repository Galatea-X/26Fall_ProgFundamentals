item_name = "Phone"
unit_price = 1799.99
quantity = 2
tax_rate = 0.05
subtotal = unit_price * quantity
tax_amount = subtotal * tax_rate
total_price = subtotal + tax_amount
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax Amount: ${tax_amount:.2f}")
print(f"Total Price: ${total_price:.2f}")
