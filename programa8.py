def obtenerPrecioEnCentimos():
    precio = float(input("ingrese el precio del producto en euros con dos decimales: "))
    euro = int(precio)
    centimo = int((precio - euro)* 100)
    return euro, centimo
euro, centimo = obtenerPrecioEnCentimos()
print(f"el precio que introdujo es: {euro} euros y {centimo} centecimos")