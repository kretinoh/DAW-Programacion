"""
@author kretinoh
 20 meses
"""
pago = 10
total = 0

for mes in range(1, 21):
    print(f"Este mes paga {pago}")
    total += pago
    pago *= 2

print(f"Pagará en total {total} €")
