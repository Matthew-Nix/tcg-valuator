import flet
from app_layout import AppLayout
from board import Board
from board_list import BoardList
from data_store import DataStore
from memory_store import InMemoryStore
from user import User
from flet import *

class Valuator(AppLayout):
    def __init__(self, page: Page, store: DataStore):
        self.page = page
        self.store: DataStore = store


    def initialize(self):
        self.page.update()

    #def login

    def route_change(self, e):
        troute = TemplateRoute(self.page.route)

        #if else for each route/page app can go to
        self.page.update()

    #def add_board

    #def testfield_change

    #def create_new_board

    #def delete_board

def main(page: Page):

    page.title = "MTG Valuator"
    page.padding = 0
    page.theme = flet.Theme(font_family="Verdana")
    page.theme.page_transitions.windows = "cupertino"
    page.fonts = {"Pacifico": "Pacifico-Regular.ttf"}
    page.bgcolor = colors.BLUE_GREY_200
    app = Valuator(page, InMemoryStore())
    page.add(app)
    page.update()
    app.initialize()

flet.app(target=main, assets_dir="../assets")


