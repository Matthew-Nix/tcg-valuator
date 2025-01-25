import flet as ft


def main(page: ft.Page):


    page.add(ft.Text(f"Initial route:  {page.route}"))

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("TCG Valuator"), bgcolor=ft.Colors.ON_SURFACE_VARIANT),
                    ft.ElevatedButton("Collection", on_click=lambda _: page.go("/collection")),
                    ft.ElevatedButton("Add Card", on_click=lambda _: page.go("/add_card")),
                    ft.ElevatedButton("Settings", on_click=lambda _: page.go("/settings")),
                ],
            )
        )
        if page.route == "/collection":
            page.views.append(
                ft.View(
                    "/collection",
                    [
                        ft.AppBar(title=ft.Text("Collection"), bgcolor=ft.Colors.ON_SURFACE_VARIANT),
                        ft.ElevatedButton("Home", on_click=lambda _: page.go("/")),
                        ft.ElevatedButton("Add Card", on_click=lambda _: page.go("/add_card")),
                        ft.ElevatedButton("Settings", on_click=lambda _: page.go("/settings")),
                    ],
                )    
                
            )

        if page.route == "/add_card":
            page.views.append(
                ft.View(
                    "/add_card",
                    [
                        ft.AppBar(title=ft.Text("Add Card"), bgcolor=ft.Colors.ON_SURFACE_VARIANT),
                        ft.ElevatedButton("Home", on_click=lambda _: page.go("/")),
                        ft.ElevatedButton("Collection", on_click=lambda _: page.go("/collection")),
                        ft.ElevatedButton("Settings", on_click=lambda _: page.go("/settings")),
                    ],
                )    
                
            )

        if page.route == "/settings":
            page.views.append(
                ft.View(
                    "/settings",
                    [
                        ft.AppBar(title=ft.Text("Setttings"), bgcolor=ft.Colors.ON_SURFACE_VARIANT),
                        ft.ElevatedButton("Home", on_click=lambda _: page.go("/")),
                        ft.ElevatedButton("Collection", on_click=lambda _: page.go("/collection")),
                        ft.ElevatedButton("Add Card", on_click=lambda _: page.go("/add_card")),
                    ],
                )    
                
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
ft.app(main, view=ft.AppView.WEB_BROWSER)


