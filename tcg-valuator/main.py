import flet
from app_layout import AppLayout
from board import Board
from board_list import BoardList
from data_store import DataStore
from flet import *
from memory_store import InMemoryStore
from user import User


class TrelloApp(AppLayout):
    def __init__(self, page: Page, store: DataStore):
        self.page = page
        self.store: DataStore = store
        self.page.update()
        super().__init__(
            self,
            self.page,
            self.store,
            tight=True,
            expand=True,
            vertical_alignment="start",
        )

    def initialize(self):
        self.page.update()

    def login(self, e):
        user_name = TextField(label="User name")
        password = TextField(label="Password", password=True)

    def route_change(self, e):
        troute = TemplateRoute(self.page.route)
        if troute.match("/"):
            self.page.go("/boards")
        elif troute.match("/board/:id"):
            if int(troute.id) > len(self.store.get_boards()):
                self.page.go("/")
                return
            self.set_board_view(int(troute.id))
        elif troute.match("/boards"):
            self.set_all_boards_view()
        elif troute.match("/members"):
            self.set_members_view()
        self.page.update()

    def add_board(self, e):
        dialog_text = TextField(
            label="New Board Name", on_submit=close_dlg, on_change=textfield_change
        )
        create_button = ElevatedButton(
            text="Create", bgcolor=colors.BLUE_200, on_click=close_dlg, disabled=True
        )

    def create_new_board(self, board_name):
        new_board = Board(self, self.store, board_name, self.page)
        self.store.add_board(new_board)
        self.hydrate_all_boards_view()

    def delete_board(self, e):
        self.store.remove_board(e.control.data)
        self.set_all_boards_view()


def main(page: Page):

    page.title = "TCG Valuator"
    page.padding = 0
    page.theme = flet.Theme(font_family="Verdana") 
    page.theme.page_transitions.windows = "cupertino"
    page.fonts = {"Pacifico": "Pacifico-Regular.ttf"}
    page.bgcolor = Colors.BLUE_GREY_200
    app = TrelloApp(page, InMemoryStore())
    page.add(app)
    page.update()
    app.initialize()

flet.app(target=main, assets_dir="../assets")
