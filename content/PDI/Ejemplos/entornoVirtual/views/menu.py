import flet as ft
from flet_route import Params, Basket

def menu(page:ft.Page, params: Params, basket: Basket):
    content = ft.Column([
        ft.ElevatedButton("Iniciar sesión"),
        ft.ElevatedButton("Registrarse")
    ])

    return content

