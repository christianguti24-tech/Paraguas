import flet as ft
from typing import Any
from app.services.transacciones_api_productos import list_products
from app.styles.estilos import Colors, Textos_estilos


def productos_view(page: ft.Page) -> ft.Control:

    productos = list_products()

    total_items = len(productos)

    total_text = ft.Text(
        f"Total de productos: {total_items}",
        style=Textos_estilos.H4
    )

    # Encabezados
    columnas = [
        ft.DataColumn(label=ft.Text("Nombre", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Cantidad", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Ingreso", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Min", style=Textos_estilos.H4)),
        ft.DataColumn(label=ft.Text("Max", style=Textos_estilos.H4)),
    ]

    # Filas
    data = []

    for p in productos:
        data.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(p["nombre"]))),
                    ft.DataCell(ft.Text(str(p["cantidad"]))),
                    ft.DataCell(ft.Text(str(p["ingreso"]))),
                    ft.DataCell(ft.Text(str(p["min"]))),
                    ft.DataCell(ft.Text(str(p["max"]))),
                ]
            )
        )

    tabla = ft.DataTable(
        columns=columnas,
        rows=data,
        width=900,
        heading_row_height=60,
        heading_row_color=Colors.BG,
        data_row_max_height=60,
        data_row_min_height=48
    )

    contenido = ft.Column(
        [
            total_text,
            tabla
        ]
    )

    return contenido