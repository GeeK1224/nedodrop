import flet as ft
import views


if __name__ == "__main__":

    def main(page: ft.Page):

        page.title = "Nedodrop"
        page.padding = 0
        page.bgcolor = "#121212"
        page.theme_mode = 'dark'

        using_personal_data = ft.Switch("", value=False)
        device_name_field = ft.TextField(label="Device name", value=page.client_storage.get("device_name"))
        
        def route_change(e):
            page.views.clear()
            page.views.append(
                views.main(device_name="nedogeek", page=page)
            )
            if page.route == "/registration":
                page.views.append(
                    views.registration(page=page, device_name=device_name_field)
                )
            if page.route == "/history":
                page.views.append(
                    views.history(page)
                )
            if page.route == "/settings":
                page.views.append(
                    views.settings(device_name_field=device_name_field, control_element=using_personal_data, page=page)
                )
            page.update()

        def view_pop(e):
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

        page.add(

        )
        page.on_route_change = route_change
        page.on_view_pop = view_pop
        page.go(page.route)

        page.update()

    ft.app(target=main)
