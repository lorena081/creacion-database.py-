
import sqlite3
from server.py import (
    crear_producto, listar_productos, consultar_producto, 
    actualizar_producto, eliminar_producto, calcular_valor_total_inventario, 
    productos_agotados, producto_mas_costoso, estadisticas_inventario
)

print("============ INICIANDO LAS 9 PRUEBAS OBLIGATORIAS ============\n")

print("1. Creando productos de prueba...")
print(crear_producto("Labial Matte Trendy", "Cosméticos", 15, 12000.0))
print(crear_producto("Base Hidratante", "Cosméticos", 20, 25000.0))
print(crear_producto("Paleta de Sombras", "Cosméticos", 0, 45000.0)) # Agotado
print(crear_producto("Fijador de Maquillaje", "Cosméticos", 30, 18000.0))
print(crear_producto("Brocha Difuminadora", "Accesorios", 50, 8000.0))
print("-" * 50)

print("\n2. Consultando el producto con ID = 2:")
print(consultar_producto(2))
print("-" * 50)

print("\n3. Actualizando cantidad del producto ID = 1:")
print(actualizar_producto(1, 25))
print("-" * 50)

print("\n4. Lista de todos los productos en inventario:")
productos = listar_productos()
for p in productos:
    print(p)
print("-" * 50)

print("\n5. Eliminando el producto con ID = 5:")
print(eliminar_producto(5))
print("-" * 50)

print("\n6. Valor económico total acumulado:")
print(calcular_valor_total_inventario())
print("-" * 50)

print("\n7. Productos con stock en cero (Cantidad = 0):")
print(productos_agotados())
print("-" * 50)

print("\n8. Artículo con el precio unitario más alto:")
print(producto_mas_costoso())
print("-" * 50)


print("\n9. Reporte consolidado de estadísticas generales:")
print(estadisticas_inventario())
print("\n=================== PRUEBAS FINALIZADAS ===================")
