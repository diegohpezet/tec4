import flet as ft
from flet_route import Params, Basket

def menu(page:ft.Page, params: Params, basket: Basket):
    content = ft.Column([
        ft.ElevatedButton("Iniciar sesión", on_click=lambda _: page.go("/login")),
        ft.ElevatedButton("Registrarse", on_click=lambda _: page.go("/register"))
    ])

    return content

