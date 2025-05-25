from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.tooltip import MDTooltipRich


class CustomTooltip(MDTooltipRich):
    pass


class HistoryScreen(MDScreen):
    pass  # No need to define build() in this screen


class MainApp(MDApp):  # Make sure this class is named MainApp (or your app's name)
    def build(self):
        self.theme_cls.theme_style = "Light"
        return HistoryScreen()

    def show_tooltip(self, widget):
        tooltip = CustomTooltip()
        tooltip.open(widget)


if __name__ == "__main__":
    MainApp().run()  # Ensure you are running MainApp
