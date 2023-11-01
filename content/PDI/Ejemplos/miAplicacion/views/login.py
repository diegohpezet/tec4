import flet as ft
from flet_route import Params, Basket

def login(page:ft.Page, params: Params, basket: Basket):
    def checkLogin(e):
        if (userInput.value == "admin" and passInput.value == "1234"):
            msg.value = "Éxito al iniciar sesión"
            content.controls.append(ft.Image(src="success.png"))
            page.update()
        else: 
            msg.value = "Revisa tus credenciales"
            page.update()
    
    userInput = ft.TextField(hint_text="Usuario...")
    passInput = ft.TextField(hint_text="Contraseña...", password=True)
    loginBtn = ft.ElevatedButton("Iniciar sesión", on_click=checkLogin)
    goBackBtn = ft.ElevatedButton("Atrás", on_click=lambda _: page.go("/"))
    msg = ft.Text("")
    
    content = ft.Column([
        ft.Text("Solamente funciona con las credenciales admin y 1234"),
        userInput,
        passInput,
        loginBtn,
        goBackBtn,
        msg
    ])

    return content

