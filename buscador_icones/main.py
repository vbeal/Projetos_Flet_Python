import flet as ft

def icon_container(icone: str):
    return ft.Container(
        padding=ft.padding.all(20),
        bgcolor=ft.colors.WHITE10,
        border_radius=ft.border_radius.all(10),
        alignment=ft.alignment.center,
        height=100,
        width=100,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(
                    name=icone,
                    color=ft.colors.WHITE,
                    size=30
                ),
                ft.Text(
                    value=icone,
                    color=ft.colors.WHITE,
                )
            ]
        )
    )

def main(page: ft.Page):

    def buscar(e):
        value = e.control.value.upper()

        icons_grid.controls = []

        for icone in dir(ft.icons):
            if value.lower() in icone.lower():
                icons_grid.controls.append(icon_container(icone=icone))

        icons_grid.update()

    searchbar = ft.TextField(
        prefix_icon=ft.icons.SEARCH,
        border_color=ft.colors.WHITE,
        hint_text='Digite algo para buscar...',
        on_submit=buscar
    )

    icons_grid = ft.GridView(
        expand=True, # Ocupar todo o espaço disponível da minha aplicação
        max_extent=200,
        controls=[],
        child_aspect_ratio=1.0,
    )

    layout = ft.Column(
        expand=True,
        controls=[
            searchbar,
            icons_grid,
        ]
    )

    page.add(layout)


if __name__ == "__main__":
    ft.app(target=main)