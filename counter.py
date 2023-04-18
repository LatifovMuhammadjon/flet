import flet as ft
import logging


logging.basicConfig(level=logging.INFO)
def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    txt_number = ft.TextField(value=str(page.width), text_align=ft.TextAlign.CENTER, width=page.width, read_only=True)
    page.on_resize = page.update
    def minus_click(e):
        value = int(txt_number.value)
        txt_number.value = str(value - 1 if value > 0 else value)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click, ),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    

ft.app(target=main)