from fastmcp import FastMCP
import sqlite3
from database import init_db, DB_NAME

# Inicializa la base de datos
init_db()

mcp = FastMCP("InventarioDB")

def get_connection():
    return sqlite3.connect(DB_NAME)

# --- PARTE 2: OPERACIONES CRUD ---

@mcp.tool()
def crear_producto(nombre: str, categoria: str, cantidad: int, precio: float) -> str:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO productos (nombre, categoria, cantidad, precio) VALUES (?, ?, ?, ?)",
        (nombre, categoria, cantidad, precio)
    )
    conn.commit()
    conn.close()
    return "Producto creado exitosamente"

@mcp.tool()
def consultar_producto(id: int) -> dict:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "id": row[0],
            "nombre": row[1],
            "categoria": row[2],
            "cantidad": row[3],
            "precio": row[4]
        }
    return {"error": "Producto no encontrado"}

@mcp.tool()
def actualizar_producto(id: int, cantidad: int) -> str:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (cantidad, id))
    conn.commit()
    conn.close()
    return "Producto actualizado correctamente"

@mcp.tool()
def eliminar_producto(id: int) -> str:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return "Producto eliminado correctamente"

@mcp.tool()
def listar_productos() -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "id": row[0],
            "nombre": row[1],
            "categoria": row[2],
            "cantidad": row[3],
            "precio": row[4]
        }
        for row in rows
    ]

# --- PARTE 3: HERRAMIENTAS COGNITIVAS Y ANALÍTICAS ---

@mcp.tool()
def calcular_valor_total_inventario() -> dict:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(cantidad * precio) FROM productos")
    total = cursor.fetchone()[0]
    conn.close()
    return {"valor_total_inventario": total if total else 0}

@mcp.tool()
def productos_agotados() -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad = 0")
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "id": row[0],
            "nombre": row[1],
            "categoria": row[2],
            "cantidad": row[3],
            "precio": row[4]
        }
        for row in rows
    ]

@mcp.tool()
def producto_mas_costoso() -> dict:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos ORDER BY precio DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "id": row[0],
            "nombre": row[1],
            "categoria": row[2],
            "cantidad": row[3],
            "precio": row[4]
        }
    return {"error": "No hay productos registrados"}

@mcp.tool()
def estadisticas_inventario() -> dict:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*), AVG(cantidad), AVG(precio), SUM(cantidad * precio) FROM productos")
    total_productos, promedio_cantidad, promedio_precio, valor_total = cursor.fetchone()
    conn.close()
    return {
        "total_productos": total_productos,
        "promedio_cantidad": promedio_cantidad,
        "promedio_precio": promedio_precio,
        "valor_total": valor_total if valor_total else 0
    }

if __name__ == "__main__":
    mcp.run()