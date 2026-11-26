from inventario import Producto, calcular_total_inventario

def ejecutar_tienda():
    p1 = Producto("A01", "Laptop Gamer", 3500.0, 5)
    p2 = Producto("A02", "Mouse Inalámbrico", 80.0, 20)
    p3 = Producto("A03", "Teclado Mecánico", 220.0, 10)

    catalogo = [p1, p2, p3]

    print("--- INVENTARIO INICIAL ---")
    for item in catalogo:
        print(f"{item.codigo} - {item.nombre}: S/ {item.precio} (Stock: {item.stock})")

    p1.aplicar_descuento(10)
    venta_exitosa = p2.vender(3)

    if venta_exitosa == True:
        print("\nVenta realizada con éxito.")
    else:
        print("\nNo hay stock suficiente.")

    valor_total = calcular_total_inventario(catalogo)
    print(f"\nValor total del inventario: S/ {valor_total}")

if __name__ == "__main__":
    ejecutar_tienda()
