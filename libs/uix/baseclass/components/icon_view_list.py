from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.boxlayout import MDBoxLayout

KV = """
<IconViewItem>:
    size_hint_y: None
    height: dp(80)
    # md_bg_color: "transparent"
    padding: dp(10)
    MDIcon:
        id: icon
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        icon: root.icon
        theme_font_size: "Custom"
        font_size: dp(48)
        theme_text_color: "Custom"
        text_color: "orange" if root.icon == "star" else "grey"
"""

Builder.load_string(KV)

class IconViewItem(ButtonBehavior, MDBoxLayout):
    icon = StringProperty("star-outline")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_release=self.on_icon_pressed)

    def toggle_icon(self):
        self.icon = "star" if self.icon == "star-outline" else "star-outline"

    def on_icon_pressed(self, *args):
        self.toggle_icon()
