import flet as ft
from app.views.mostrar_datos import productos_view

def main(page: ft.Page):
    page.title = "Aplicación con estilos"
    page.scroll=ft.ScrollMode.ADAPTIVE
    page.add(productos_view(page))

if __name__ == "__main__":
    ft.run(main)