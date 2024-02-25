import flet as ft

def main(page: ft.Page):
    def registration_button(e):
        if not registration_device_name.value:
            registration_device_name.error_text = "Please enter device name"
            page.update()
        else:
            page.client_storage.set("device_name", registration_device_name.value)
            page.clean()
            page.go("/main")
    
    def edit_name_button(e):
        if not settings_device_name.value:
            settings_device_name.error_text = "Please enter device name"
            page.update()
        else:
            page.client_storage.set("device_name", settings_device_name.value)
            page.clean()
            page.go('/main')

    def pick_files_result(e: ft.FilePickerResultEvent):
        files = map(lambda f: f.name, e.files) if e.files else None
        print(files)
    
    def delete_picked_file(e):
        pass

    files = []
    registration_device_name = ft.TextField(label='Device Name', width=400)
    settings_device_name = ft.TextField(label='Device Name', width=400, value=page.client_storage.get("device_name"))
    image_reg = ft.Image(src="icon.png", width=100, height=100)
    image_icon = ft.Image(src="icon.png", width=40, height=40)

    contact_sharing = ft.Switch(label="Do you want to use contact sharing?")
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()
    selected_file_object = ft.Row(
        [
            selected_files,
            ft.IconButton(ft.icons.DELETE, on_click=delete_picked_file)
        ]
    )

class AppLayout(ft.Row):
    def __init__(self, app, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.page = page

        self._active_view: ft.Control = ft.Column(
            controls=[
                ft.Text("Active View")
            ], alignment="center", horizontal_alignment="center"
        )
        self.registration_view = ft.Column(
                                    controls=[
                                        image_reg,
                                        ft.Text('Hello, welcome to nedodrop', size=30, font_family='Inter'),
                                        registration_device_name,
                                        ft.IconButton(
                                            icon=ft.icons.NAVIGATE_NEXT,
                                            bgcolor='#d4d4d4',
                                            icon_color='#121212',
                                            icon_size=30,
                                            tooltip='Next',
                                            on_click=registration_button
                                        )
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                )
        self.main_view = ft.Column(
                            controls=[
                                ft.Row(
                                    [
                                        ft.Row(
                                            [
                                                image_icon,
                                                ft.Text(page.client_storage.get("device_name"), size=20),
                                            ], alignment=ft.MainAxisAlignment.START
                                        ),
                                        ft.Row(
                                            [
                                                ft.IconButton(ft.icons.HISTORY, on_click=lambda _: page.go('/history')),
                                                ft.IconButton(ft.icons.SETTINGS, on_click=lambda _: page.go('/settings'))
                                            ], alignment=ft.MainAxisAlignment.END
                                        ),
                                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),
                                ft.Row(
                                    [
                                        ft.ElevatedButton(
                                            "Send",
                                            icon=ft.icons.SEND,
                                            height=50,
                                            width=200,
                                            on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=True),
                                        ),
                                        ft.ElevatedButton(
                                            "Receive",
                                            icon=ft.icons.GET_APP,
                                            height=50,
                                            width=200,
                                            # on_click=,
                                        ),
                                    ], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.START
                                ),
                            ]
                        )
        self.settings_view = ft.Column(
                                [
                                    ft.AppBar(title=ft.Text("Settings"), bgcolor="#1a1c1e"),
                                    ft.Column(
                                        width=400,
                                        controls=[
                                            ft.Text("Change device name"),
                                            settings_device_name,
                                            ft.ElevatedButton(
                                                text="Save",
                                                bgcolor='#d4d4d4',
                                                color="#121212",
                                                on_click=edit_name_button
                                            ),
                                            contact_sharing,
                                        ], horizontal_alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                    )
                                ]
                            )
        self.history_view = ft.Column(
                            controls=[
                                ft.AppBar(title=ft.Text("History"), bgcolor="#1a1c1e"),
                                ft.Card(
                                    content=ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.ListTile(
                                                    leading=ft.Icon(ft.icons.DEVICES),
                                                    title=ft.Text("DEVICE_NAME"),
                                                    subtitle=ft.Text("2024/01/26"),
                                                ),
                                                ft.Row(
                                                    [ft.TextButton("See files"), ft.TextButton("Delete")],
                                                    alignment=ft.MainAxisAlignment.END,
                                                ),
                                            ]
                                        ),
                                        width=400,
                                        padding=10,
                                    )
                                )
                            ]
                        )
        self.search_devices_view = ft.Column(controls=[])
        self.share_files_view = ft.Column(controls=[])
        self.controls = [self.active_view]
    
    @property
    def active_view(self):
        return self._active_view
    
    @active_view.setter
    def active_view(self, view):
        self._active_view = view
        self.update()
