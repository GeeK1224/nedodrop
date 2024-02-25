import flet as ft

class NedodropApp:
    def __init__(self, page:ft.Page):
        self.page = page
        self.appbar_items = [
            ft.PopupMenuItem(text='Login'),
            ft.PopupMenuItem(),
            ft.PopupMenuItem(text='Settings')
        ]
        self.appbar = ft.AppBar(

        )
        self.on_route_change = self.route_change
    
    def initialize(self):
        self.page.views.append(
            ft.View(
                "/",
                [
                    # there is should be standard layout
                    self.appbar,
                    self.layout
                ],
                padding=ft.padding.all(0),
            )
        )
        self.page.update()
        self.page.go("/")
    
    def login(self, e):
        pass

 
    def route_change(self, e):
        troute = ft.TemplateRoute(self.page.route)
        if troute.match("/"):
            if self.page.client_storage.get("device_name") is not None:
                self.layout.set_main_view()
            else:
                self.layout.set_registration_view()
        elif troute.match("/settings"):
            self.layout.set_settings_view()
        elif troute.match("/history"):
            self.layout.set_history_view()
        elif troute.match("/history/:device_name"):
            self.layout.set_history_view(troute.device_name)
        elif troute.match("/search_devices"):
            self.layout.set_search_devices_view()
        elif troute.match("share_files_view"):
            self.layout.set_share_files_view()
        self.page.update()
    
    def set_main_view(self):
        self.active_view = self.store
        self.page.update()
    
    def set_registration_view(self):
        self.active_view = self.layout.registration_view
        self.page.update()
        
    def set_settings_view(self):
        self.active_view = self.layout.registration_view
        self.page.update()
    
    def set_history_view(self):
        self.active_view = self.layout.registration_view
        self.page.update()

    def set_search_devices_view(self):
        self.active_view = self.layout.registration_view
        self.page.update()

    def set_share_files_view(self):
        self.active_view = self.layout.registration_view
        self.page.update()


if __name__ == "__main__":

    def main(page: ft.Page):

        page.title = "Nedodrop"
        page.padding = 0
        page.bgcolor = "#121212"
        page.theme_mode = 'dark'
        app = NedodropApp(page)
        page.add(app)
        page.update()

    ft.app(target=main)