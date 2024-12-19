import flet as ft

def main(page: ft.Page):
    page.title = "Editor de Markdown"
    page.window_width = 700
    page.window_height = 900

    def update_view(e):
        view.value = e.control.value
        view.update()

    # Nosso Editor
    editor = ft.TextField(
        multiline=True,
        min_lines=25,
        max_lines=25,
        color=ft.colors.BLACK,
        content_padding=ft.padding.all(30),
        border=ft.InputBorder.NONE,
        bgcolor=ft.colors.BLUE_GREY,
        on_change= update_view
    )


    ajuda = ft.Container(
        expand=True,
        padding=ft.padding.all(30),
        content=ft.Column(
            controls=[
                ft.Text(
                    value='Ajuda para Editor Markdown', 
                    weight=ft.FontWeight.BOLD, 
                    color=ft.colors.BLACK
                    ),
                ft.Text(
                    value='# H1', color=ft.colors.GREY_700
                    ),
                ft.Text(
                    value='## H2', color=ft.colors.GREY_700
                    ),
                ft.Text(
                    value='### H3', color=ft.colors.GREY_700
                    ),
                ft.Text(
                    value='#### H4', color=ft.colors.GREY_700
                    ),
                ft.Text(
                    value='##### H5', color=ft.colors.GREY_700
                    ),
                ft.Text(
                    value='###### H6', color=ft.colors.GREY_700
                    ),
                ft.Divider(color=ft.colors.GREY, height=40),


                ft.Text(
                    value='Para formatar estilos de texto, use as tags:', 
                    weight=ft.FontWeight.BOLD, 
                    color=ft.colors.BLACK
                    ),
                ft.Text(
                    value='**Texto em negrito**', color=ft.colors.GREY_700
                    ),
                ft.Text(
                    value='*Texto em italico*', color=ft.colors.GREY_700
                    ),
                ft.Text(
                    value='~~Texto em riscado~~', color=ft.colors.GREY_700
                    ),
                
                ft.Divider(color=ft.colors.GREY, height=40),


            ]
        )
    )
    

    view = ft.Markdown(
        value = editor.value,
        selectable =True,
        extension_set =  ft.MarkdownExtensionSet.GITHUB_WEB,
        code_theme='monokai-sublime',
        on_tap_link=lambda e: ft.launch_url(e.data),
    )

    layout = ft.Row(
        expand=True,
        vertical_alignment=ft.CrossAxisAlignment.STRETCH,
        controls=[
            ft.Container(
                expand=True,
                bgcolor=ft.colors.WHITE,
                content=ft.Column(
                    controls=[
                            editor,
                            ajuda,
                    ]
                )

            ),
            ft.Container(
                expand=True,
                bgcolor=ft.colors.BLACK,
                padding=ft.padding.all(30),
                content=view
            ),
        ],
    )

    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main)