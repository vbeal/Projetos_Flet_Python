import flet as ft

def main(page: ft.Page):
    
    page.bgcolor = ft.colors.BROWN_500

    layout = ft.ResponsiveRow(
        controls=[
            senario,
            game,
            teclado,
            senario,
        ]
    )
    
    page.update()

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")