from flet_route import path
from views.menu import menu

app_routes = [
    path(url="/", clear=True, view = menu)
]