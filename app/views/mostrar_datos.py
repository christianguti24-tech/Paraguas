import flet as ft
from typing import Any
from app.services.transacciones_api_productos import list_products
from app.styles.estilos import Colors, Textos_estilos, Card

# from app.views.nuevo_editar import formulario_nuevo_editar_producto 

def productos_view(page: ft.Page) -> ft.Control:

    def inicio_nuevo_producto(_e):
        async def crear_nuevo_producto(data: dict):
            try:
                # Si estas funciones no están importadas arriba, también marcarán error al dar clic.
                # Por ahora, como vamos a desactivar el formulario, no causarán problema al iniciar.
                await create_product(data)
                await show_snackbar(page, "Éxito", "Producto creado.", bgcolor=Colors.SUCCESS)
            except ApiError as ex:
                await show_popup(page, "Error", api_error_to_text(ex))
            except Exception as ex:
                await show_snackbar(page, "Error", str(ex), bgcolor=Colors.DANGER)

        
    btn_nuevo = ft.Button("Nuevo producto", icon="add", on_click=inicio_nuevo_producto)

    productos = list_products()
    total_items = len(productos)

    # AQUÍ LE QUITÉ LOS # PARA QUE FUNCIONE BIEN EL TEXTO:
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
        #expand=True,
        spacing=30,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            btn_nuevo,
            total_text,
            ft.Container(content=tabla)
        ]
    )

    tarjeta = ft.Container(content=contenido, **Card.tarjeta)

    return tarjeta
