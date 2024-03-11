import flet as ft
import items


def registration(page, device_name):
    return ft.View(
        "/registration",
        controls=[
            ft.Column(
                controls=[
                    ft.Image(src="./assets/icon.png", width=100, height=100, fit=ft.ImageFit.CONTAIN),
                    ft.Text("Hello, welcome to nedodrop", size=30),
                    device_name,
                    ft.ElevatedButton(text="Continue", width=150, height=45, color="#F5F5F5", on_click=lambda e: page.go("/")),
                ],
                alignment=ft.CrossAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                width=500,
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    )


def main(page, device_name):
    return ft.View(
        "/",
        controls=[
            ft.Row(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Image(src="./assets/icon.png", width=50, height=50, fit=ft.ImageFit.CONTAIN),
                            ft.Text(value=device_name),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.IconButton(icon=ft.icons.HISTORY, on_click=lambda e: page.go("/history")),
                            ft.IconButton(icon=ft.icons.SETTINGS, on_click=lambda e: page.go("/settings")),
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            ft.Row(
                controls=[
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(text="Send", icon=ft.icons.FILE_UPLOAD, width=150, height=45, color="#F5F5F5"),
                            ft.ElevatedButton(text="Receive", icon=ft.icons.FILE_DOWNLOAD, width=150, height=45, color="#F5F5F5")
                        ],
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            )
        ],
    )


def settings(device_name_field: ft.TextField, control_element, page):
    return ft.View(
        "/settings",
        controls=[
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda e: page.go("/")),
                            ft.Text(value="Settings", size=30),
                        ]
                    ),
                    device_name_field,
                    items.settings_element(element_text="Share contact info", control_element=control_element),
                ],
                width=500,
            ),
            ft.Column(
                controls=[
                    ft.ElevatedButton(text="Log out", width=500, height=45, color="#F5F5F5", on_click=lambda e: page.go('/registration')),
                ],
                alignment=ft.MainAxisAlignment.END,
                height=500,
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

def history(page):
    return ft.View(
        "/history",
        controls=[
            ft.Column(
              controls=[
                  ft.Row(
                      controls=[
                          ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda e: page.go("/")),
                          ft.Text(value="History", size=30),
                      ]
                  ),
                  items.history_item(device_name="sample name", date="sample date"),
                  items.history_item(device_name="sample name", date="sample date"),
                  items.history_item(device_name="sample name", date="sample date"),                  
              ],
              width=500,
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )