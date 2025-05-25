from kivymd.uix.dialog import (
    MDDialog,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
    MDDialogContentContainer,
)
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarSupportingText
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.utils import platform
from kivy.uix.widget import Widget
import logging
from libs.uix.baseclass.components.icon_view_list import IconViewItem


class EconetDashboardScreen(MDScreen):
    phone_number = StringProperty("*125#")

    def on_enter(self):
        if not hasattr(self, 'tour_done') or not self.tour_done:
            self.guided_tour()
            self.tour_done = True

    def guided_tour(self):
        self.tutorial_index = 0
        self.tutorial_steps = [
            {"title": "Welcome", "text": "Welcome to the dashboard!"},
            {"title": "Recharge", "text": "Use the dial button to top-up your airtime ."},
            {"title": "Scan", "text": "Use your camera to capture the numbers and top-up your airtime ."},
            {"title": "Rate Us", "text": "How did you like the application? send your feedback."},
            {"title": "Transaction History", "text": "View all your recent activities in the history section."},
            {"title": "Get Help", "text": "Access support from the menu for any assistance."},
        ]
        self.show_tutorial_step()

    def highlight_card(self, widget):
        if widget:
            widget.original_md_bg_color = getattr(widget, "md_bg_color", None)
            widget.md_bg_color = (1, 0.75, 0.2, 1)  # yellow

    def remove_highlight(self, widget):
        if widget and hasattr(widget, "original_md_bg_color"):
            widget.md_bg_color = widget.original_md_bg_color

    def show_tutorial_step(self):
        if self.tutorial_index < len(self.tutorial_steps):
            step = self.tutorial_steps[self.tutorial_index]
            card_id_map = {
                "Get Help": "help_card",
                "Scan": "scan_card",
                "Rate Us": "rate_card",
                "Transaction History": "history_button",
                "Recharge": "dial_card"
            }

            self.current_highlighted_card = None
            card_id = card_id_map.get(step["title"], None)
            card_widget = self.ids.get(card_id) if card_id else None

            def open_dialog(*args):
                if card_widget:
                    self.highlight_card(card_widget)
                    self.current_highlighted_card = card_widget

                    x, y = card_widget.to_window(card_widget.center_x, card_widget.top)
                    dialog_width = min(dp(250), Window.width * 0.6)
                    center_x = 0.6 if step["title"] not in ["Rate Us", "Recharge"] else 0.4

                    self.tutorial_dialog = MDDialog(
                        MDDialogHeadlineText(text=step["title"]),
                        MDDialogSupportingText(text=step["text"]),
                        MDDialogButtonContainer(
                            MDButton(
                                MDButtonText(text="Next"),
                                on_release=lambda x: self.next_tutorial_step(),
                            )
                        ),
                        pos_hint={
                            "center_x": center_x,
                            "y": (y / Window.height) + 0.03
                        },
                        size_hint=(None, None),
                        width=dialog_width,
                        auto_dismiss=False,
                        adaptive_height=True,
                    )
                else:
                    self.tutorial_dialog = MDDialog(
                        MDDialogHeadlineText(text=step["title"]),
                        MDDialogSupportingText(text=step["text"]),
                        MDDialogButtonContainer(
                            MDButton(
                                MDButtonText(text="Next"),
                                on_release=lambda x: self.next_tutorial_step(),
                            )
                        ),
                        size_hint_x=0.85,
                        adaptive_height=True,
                    )

                self.tutorial_dialog.open()

            Clock.schedule_once(open_dialog, 0.1)
        else:
            self.tutorial_index = 0

    def next_tutorial_step(self):
        if self.current_highlighted_card:
            self.remove_highlight(self.current_highlighted_card)
            self.current_highlighted_card = None

        self.tutorial_dialog.dismiss()
        self.tutorial_index += 1
        self.show_tutorial_step()

    def show_event_dialog(self):
        self.icon1 = IconViewItem()
        self.icon2 = IconViewItem()
        self.icon3 = IconViewItem()
        self.icon4 = IconViewItem()
        self.icon5 = IconViewItem()

        # Dialog definition
        self.dialog = MDDialog(
            MDDialogContentContainer(
                self.icon1,
                self.icon2,
                self.icon3,
                self.icon4,
                self.icon5,
            ),
            MDDialogButtonContainer(
                MDButton(
                    MDButtonText(text="Cancel"),
                    style="text",
                    on_release=lambda x: self.dialog.dismiss(),
                ),
                MDButton(
                    MDButtonText(text="Continue"),
                    style="text",
                    on_release=lambda x: self.dummy_rate_us(),
                ),
                spacing="8dp",
            ),
            size_hint_x=0.9,
            adaptive_height=True,
        )
        self.dialog.open()



    def change_icon(self, instance):
        instance.icon = 'star-settings'

    def dummy_rate_us(self):
        MDSnackbar(
            MDSnackbarSupportingText(text="Thank you for rating us!"),
            y=dp(24),
            orientation="vertical",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.9,
        ).open()
        self.dialog.dismiss()

    def fetch_history(self):
        self.manager.push("history")

    def request_android_permissions(self):
        if platform == "android":
            try:
                from android.permissions import Permission, request_permissions

                def callback(permissions, results):
                    for permission, result in zip(permissions, results):
                        if result:
                            logging.info(f"Permission granted: {permission}")
                        else:
                            logging.warning(f"Permission denied: {permission}")

                request_permissions(
                    [
                        Permission.WRITE_EXTERNAL_STORAGE,
                        Permission.READ_EXTERNAL_STORAGE,
                        Permission.CAMERA,
                        Permission.CALL_PHONE,
                    ],
                    callback,
                )
            except ImportError as e:
                logging.error(f"Android permissions module not found: {e}")
            except Exception as e:
                logging.error(f"Error while requesting permissions: {e}")

    def make_phone_call(self, phone_number: str):
        if not phone_number or not self.validate_phone_number(phone_number):
            logging.warning(f"Invalid phone number: {phone_number}")
            return

        try:
            from android.permissions import Permission, check_permission
            from jnius import autoclass

            if not check_permission(Permission.CALL_PHONE):
                logging.warning("CALL_PHONE permission not granted")
                return

            Intent = autoclass("android.content.Intent")
            Uri = autoclass("android.net.Uri")

            intent = Intent(Intent.ACTION_CALL)
            uri = Uri.parse(f"tel:{phone_number}")
            intent.setData(uri)

            PythonActivity = autoclass("org.kivy.android.PythonActivity")
            activity = PythonActivity.mActivity
            activity.startActivity(intent)

            logging.info(f"Initiating call to {phone_number}")

        except Exception as e:
            logging.error(f"Error while making the phone call: {e}")

    def validate_phone_number(self, phone_number: str) -> bool:
        return phone_number.isdigit() and len(phone_number) >= 10
