import flet as ft

def main(page: ft.Page):
    page.title = "Contador"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 300
    page.window_height = 200

    # Vamos usar um TextField para o usuário 
    # poder alterar o valor inicial
    text_number = ft.TextField(
        value= '0',
        text_align=ft.TextAlign.CENTER,
        width=100,
        border_color=ft.colors.WHITE
    )

    def subtrai_click(e):
        text_number.value = str(int(text_number.value) - 1)
        text_number.update()

    def somar_click(e):
        text_number.value = str(int(text_number.value) + 1)
        text_number.update()

    titulo = ft.Text(value="Contador", size=30, color=ft.colors.WHITE)

    page.add(
        titulo,
        ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.REMOVE, on_click=subtrai_click),
                text_number,
                ft.IconButton(icon=ft.icons.ADD, on_click=somar_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.update()


ft.app(target=main)