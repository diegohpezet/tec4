import flet as ft
from flet_route import Routing, Params, Basket
from config.rutas import app_routes

def main(page: ft.Page):
    page.title="App"
    page.window_width = 400
    page.window_height = 800

    Routing(
        page= page, 
        app_routes=app_routes
    )
    page.go("/")

ft.app(target=main, assets_dir="./assets")