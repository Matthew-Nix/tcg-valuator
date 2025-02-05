import flet
from flet import *
from app_layout import *
from sidebar import *

class Valuator(AppLayout):
    def __init__(self, page: Page):
        self.page = page
        self.appbar_items = [
            PopupMenuItem(text="Login"),
            PopupMenuItem(),  # divider
            PopupMenuItem(text="Settings")
        ]
        self.appbar = AppBar(
            leading=Icon(Icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=Text("Valuator",size=32, text_align="start"),
            center_title=False,
            toolbar_height=75,
            bgcolor=Colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                Container(
                    content=PopupMenuButton(
                        items=self.appbar_items
                    ),
                    margin=margin.only(left=50, right=25)
                )
            ],
        )
        self.page.appbar = self.appbar
        self.page.update()
        super().__init__(
            self,
            self.page,
        )

if __name__ == "__main__":
 
    def main(page: Page):
 
        page.title = "Flet Trello clone"
        page.padding = 0
        page.bgcolor = Colors.BLUE_GREY_200
        app = Valuator(page)
        page.add(app)
        page.update()
 
    flet.app(main, view=flet.WEB_BROWSER)