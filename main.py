# Total bill calculator with tax and service charge

initialAmount = 510
serviceCharge = initialAmount / 100 * 10
tax = initialAmount / 100 * 6
if serviceCharge >= 51:
    serviceCharge = 50
totalAmount = initialAmount + serviceCharge + tax
print(f'Subtotal: RM{initialAmount:.2f}')
print(f'Service charge: RM{serviceCharge:.2f}')
print(f'SST: RM{tax:.2f}')
print(f'Total sales: RM{totalAmount:.2f}')

