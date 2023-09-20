"""
Przeliczanie rotacji maszyn do kręcenia stretchu
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, RIGHT, LEFT, CENTER


class Przeliczanierolek(toga.App):
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))
        
        style_l = Pack(padding=(0, 5), text_align=RIGHT, width=130)
        style_m = Pack(padding=(0, 5), text_align=CENTER, width=130)
        style_r = Pack(padding=(0, 5), text_align=LEFT, width=130)
        elements = [
            [
                toga.Label("", style=style_l),
                toga.Label("Stara wartość", style=style_m),
                toga.Label("Nowa wartość", style=style_r),
            ],
            [
                toga.Label("Waga gilzy", style=style_l),
                old_gilza_weight := toga.NumberInput(style=style_m),
                new_gilza_weight := toga.NumberInput(style=style_r),
            ],
            [
                toga.Label("Grubość folii", style=style_l),
                old_thickness := toga.NumberInput(style=style_m),
                new_thickness := toga.NumberInput(style=style_r),
            ],
            [
                toga.Label("Waga rolki", style=style_l),
                old_weight := toga.NumberInput(style=style_m),
                new_weight := toga.NumberInput(style=style_r),
            ],
            [
                toga.Label("Ustawienie", style=style_l),
                old_setting := toga.NumberInput(style=style_m),
                new_setting := toga.NumberInput(style=style_r),
            ],
        ]
        for row in elements:
            row_box = toga.Box(style=Pack(direction=ROW, padding=5))
            for item in row:
                row_box.add(item)
            main_box.add(row_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def button_press(self, ):
        print("Hello,", self.name_input.value)


def main():
    return Przeliczanierolek()
