from typing import List, Dict

# Base de datos simulada para que si funcione y muestre 
productos = [
    {
        "id": 1,
        "nombre": "Laptop",
        "cantidad": 10,
        "ingreso": "2024-01-10",
        "min": 5,
        "max": 20
    },
    {
        "id": 2,
        "nombre": "Mouse",
        "cantidad": 30,
        "ingreso": "2024-01-11",
        "min": 10,
        "max": 50
    }
]


# LISTAR PRODUCTOS
def list_products() -> List[Dict]:
    return productos


# OBTENER PRODUCTO POR ID
def get_product(product_id: int) -> Dict | None:
    for p in productos:
        if p["id"] == product_id:
            return p
    return None


# CREAR PRODUCTO
def create_product(producto: Dict) -> Dict:
    nuevo_id = max(p["id"] for p in productos) + 1 if productos else 1
    producto["id"] = nuevo_id
    productos.append(producto)
    return producto


# ACTUALIZAR PRODUCTO
def update_product(product_id: int, datos: Dict) -> Dict | None:
    for p in productos:
        if p["id"] == product_id:
            p.update(datos)
            return p
    return None


# ELIMINAR PRODUCTO
def delete_product(product_id: int) -> bool:
    for p in productos:
        if p["id"] == product_id:
            productos.remove(p)
            return True
    return False