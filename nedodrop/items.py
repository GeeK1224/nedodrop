import flet as ft

class File:
    def __init__(self, file, filename, file_size):
        self.file = file
        self.filename = filename
        self.file_size = file_size
        self.image_fomrmats = ["jpg", "jpeg","jpe", "png", "gif", "bmp", "tif", "tiff", "raw", "arw", "cr2", "nef", "webp", "svg", "jp2", "j2k", "jpf", "jpx","heif", "heic"]
        self.audio_formats = ["mp3", "wav", "flac", "aac", "ogg", "m4a", "wma", "aiff", "ape", "mp4"]
        self.video_formats = ["mp4", "avi", "mkv", "mov", "wmv", "flv", "m4v", "webm", "3gp", "mpeg"]

        if self.filename.split(".")[-1] in self.audio_formats:
            self.filetype = "audio"
        elif self.filename.split(".")[-1] in self.video_formats:
            self.filetype = "video"
        elif self.filename.split(".")[-1] in self.image_fomrmats:
            self.filetype = "image"
        else:
            self.filetype = "file"

def settings_element(element_text: str, control_element):
    return ft.Row(
        controls=[
            ft.Text(element_text),
            control_element,
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

def file_item(file: File):
    if file.filetype == "image":
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.IMAGE),
                            title=ft.Text(file.filename),
                            subtitle=ft.Text(file.file_size)
                        ),
                        ft.Row(
                            ft.TextButton("Open"),
                            ft.TextButton("Delete")
                        )
                    ]
                )
            )
        )


def history_item(device_name, date):
    return ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.DEVICES),
                                title=ft.Text(device_name),
                                subtitle=ft.Text(date),
                            ),
                            ft.Row(
                                [
                                    ft.TextButton("See files"),
                                    ft.TextButton("Delete"),
                                ],
                                alignment=ft.MainAxisAlignment.END,
                            ),
                        ]
                    ),
                    width=400,
                    padding=10,
                )
            )