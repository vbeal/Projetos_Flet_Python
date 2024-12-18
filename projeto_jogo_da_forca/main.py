import flet as ft
import random
import string

'''
**********************************
Breakpoint      Dimensão da tela
**********************************
xs              < 576px
sm              >= 576px
md              >= 768px
lg              >= 992px
xl              >= 1200px
xxl             >= 1400px
**********************************
'''

def letter_to_guess(letter):
    return ft.Container(
                bgcolor=ft.colors.AMBER_500,
                height=50,
                width=50,
                border_radius=ft.border_radius.all(5),
                content=ft.Text(
                    value=letter, 
                    color=ft.colors.WHITE,
                    size=30,
                    text_align=ft.TextAlign.CENTER,
                    weight=ft.FontWeight.BOLD
                ),
            )

def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = ft.colors.BROWN_500
    
    palavras_disponiveis = ['python','flet','programador','aventureiro']
    palavra_secreta = random.choice(palavras_disponiveis).upper()

    def validate_letter(e):
        for pos, letter in enumerate(palavra_secreta):
            if e.control.content.value == letter:
                palavra.controls[pos] = letter_to_guess(letter=letter)
                palavra.update()

        if e.control.content.value not in palavra_secreta:
            vitima.data += 1
            
            if vitima.data > 7:
                page.dialog = ft.AlertDialog(title=ft.Text('Você perdeu! :('), open=True)
                page.update()

            errors = vitima.data
            vitima.src = f'images/vitima_{errors}.png'
            vitima.update()


        e.control.disabled = True
        e.control.gradient = ft.LinearGradient(colors=[ft.colors.GREY])
        e.control.update()
    

    vitima = ft.Image(
        data= 0, # id da imagem
        src="images/vitima_0.png",
        repeat=ft.ImageRepeat.NO_REPEAT,
        height=300,
    )


    palavra = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        wrap=True,
        controls=[letter_to_guess('_') for letter in palavra_secreta]
    )

    game = ft.Container(
        col={"xs": 12,  "lg": 6},
        padding=ft.padding.all(50),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                vitima,
                palavra,

            ]
        )
    )
    
    

    teclado = ft.Container(
        col={"xs": 12,  "lg": 6},
        image_src= "images/fundo_teclado.png",
        image_repeat= ft.ImageRepeat.NO_REPEAT, # Não repetir imagem
        image_fit= ft.ImageFit.FILL, # Preencher o container
        padding= ft.padding.only(top=150, left=80, right=80, bottom=50),
        content= ft.Row(
            wrap=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    height=50,
                    width=50,
                    border_radius= ft.border_radius.all(5),
                    content= ft.Text(
                        value=letra,
                        color=ft.colors.WHITE,
                        size=30,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD
                    ),
                    #bgcolor=ft.colors.ORANGE
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[
                            ft.colors.AMBER,
                            ft.colors.DEEP_ORANGE
                        ]
                    ),
                    on_click=validate_letter,
                ) 
            for letra in string.ascii_uppercase]

        )

    )
    


    



    senario = ft.Image(col=12, src="images/senario.png")

    layout = ft.ResponsiveRow(
        columns=12,
        controls=[
            senario,
            game,
            teclado,
            senario,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        
    )
    
    page.add(layout)

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")