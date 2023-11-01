from flet_route import path
from views.menu import menu
from views.login import login

app_routes = [
    path(url="/", clear=True, view = menu),
    path(url="/login", clear=True, view=login)
]