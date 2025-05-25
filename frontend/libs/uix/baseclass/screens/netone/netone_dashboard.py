from kivymd.uix.dialog import (
    MDDialog,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
)
from kivy.clock import Clock
from kivy.core.window import Window
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import MDDialog
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarSupportingText
from kivymd.uix.dialog import (
    MDDialogButtonContainer,
    MDDialogContentContainer,
)
import logging
from kivy.properties import StringProperty
from kivy.utils import platform
from libs.uix.baseclass.components.icon_view_list import IconViewItem

class NetoneDashboardScreen(MDScreen):
    phone_number = StringProperty("*379#")  # Default phone number

    def on_enter(self):
        econet_postal_code=self.manager.get_shared_data("cached_netone_postal_code")
        print(econet_postal_code)
        self.guided_tour()

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


    def show_tutorial_step(self):
        if self.tutorial_index < len(self.tutorial_steps):
            step = self.tutorial_steps[self.tutorial_index]

            def open_dialog(*args):
                if step["title"] == "Get Help":
                    help_card = self.ids.get("help_card")
                    if help_card:
                        # Position dialog above the help card, slightly offset
                        x, y = help_card.to_window(help_card.center_x, help_card.top)
                        dialog_width = min(dp(250), Window.width * 0.6)

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
                                "center_x": 0.6,
                                "y": (y / Window.height) + 0.03  # push slightly above
                            },
                            size_hint=(None, None),
                            width=dialog_width,
                            auto_dismiss=False,
                            adaptive_height=True,
                        )
                    else:
                        print("help_card not found")
                        return

                elif step["title"] == "Scan":
                    scan_card = self.ids.get("scan_card")
                    if scan_card:
                        # Position dialog above the scan card, slightly offset
                        x, y = scan_card.to_window(scan_card.center_x, scan_card.top)
                        dialog_width = min(dp(250), Window.width * 0.6)

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
                                "center_x": 0.6,
                                "y": (y / Window.height) + 0.03  # push slightly above
                            },
                            size_hint=(None, None),
                            width=dialog_width,
                            auto_dismiss=False,
                            adaptive_height=True,
                        )
                    else:
                        print("scan_card not found")
                        return

                elif step["title"] == "Rate Us":
                    rate_card = self.ids.get("rate_card")
                    if rate_card:
                        # Position dialog above the rate card, slightly offset
                        x, y = rate_card.to_window(rate_card.center_x, rate_card.top)
                        dialog_width = min(dp(250), Window.width * 0.6)

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
                                "center_x": 0.4,
                                "y": (y / Window.height) + 0.03  # push slightly above
                            },
                            size_hint=(None, None),
                            width=dialog_width,
                            auto_dismiss=False,
                            adaptive_height=True,
                        )
                    else:
                        print("rate_card not found")
                        return

                elif step["title"] == "Transaction History":
                    history_button = self.ids.get("history_button")
                    if history_button:
                        # Position dialog above the history_button, slightly offset
                        x, y = history_button.to_window(history_button.center_x, history_button.top)
                        dialog_width = min(dp(250), Window.width * 0.6)

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
                                "center_x": 0.6,
                                "y": (y / Window.height) + 0.03  # push slightly above
                            },
                            size_hint=(None, None),
                            width=dialog_width,
                            auto_dismiss=False,
                            adaptive_height=True,
                        )
                    else:
                        print("history_button not found")
                        return

                elif step["title"] == "Recharge":
                    dial_card = self.ids.get("dial_card")
                    if dial_card:
                        # Position dialog above the dial card, slightly offset
                        x, y = dial_card.to_window(dial_card.center_x, dial_card.top)
                        dialog_width = min(dp(250), Window.width * 0.6)

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
                                "center_x": 0.4,
                                "y": (y / Window.height) + 0.03  # push slightly above
                            },
                            size_hint=(None, None),
                            width=dialog_width,
                            auto_dismiss=False,
                            adaptive_height=True,
                        )
                    else:
                        print("dial_card not found")
                        return
                    
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

            # Delay slightly to ensure widgets are laid out
            Clock.schedule_once(open_dialog, 0.1)
        else:
            self.tutorial_index = 0

    def next_tutorial_step(self):
        self.tutorial_dialog.dismiss()
        self.tutorial_index += 1
        self.show_tutorial_step()

    def show_event_dialog(self):
        # Create instances of IconViewItem with different icons
        self.icon1 = IconViewItem()
        self.icon2 = IconViewItem()
        self.icon3 = IconViewItem()
        self.icon4 = IconViewItem()
        self.icon5 = IconViewItem()

        # Define the dialog, passing in the icon instances
        self.dialog = MDDialog(
            MDDialogContentContainer(
                self.icon1,
                self.icon2,
                self.icon3,
                self.icon4,
                self.icon5,
            ),
            MDDialogButtonContainer(
                Widget(),
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
        print("Icon changed")
        instance.icon = 'star-settings'

    def dummy_rate_us(self):
        MDSnackbar(
            MDSnackbarSupportingText(
                text="Thank you for rating us!",
            ),
            y=dp(24),
            orientation="vertical",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.9,
        ).open()
        self.dialog.dismiss()

    def fetch_history(self):
        self.manager.push("history")



########################################################### CHECK BALANCE #######################################################

    # def on_enter(self):
    #     """Called when the screen is entered. Requests necessary permissions on Android."""
        
    def request_android_permissions(self):
        """
        Requests necessary Android permissions required to make a phone call.
        These permissions include external storage, camera, and call permissions.
        """
        if platform == "android":
            logging.info("Requesting Android permissions.")
            self.request_android_permissions()

        try:
            from android.permissions import Permission, request_permissions

            # Callback function to handle the results of the permission request
            def callback(permissions, results):
                for permission, result in zip(permissions, results):
                    if result:
                        logging.info(f"Permission granted: {permission}")
                    else:
                        logging.warning(f"Permission denied: {permission}")
                        # Optionally, notify the user that certain features won't work

            # Request permissions necessary for phone calls
            request_permissions(
                [
                    Permission.WRITE_EXTERNAL_STORAGE,
                    Permission.READ_EXTERNAL_STORAGE,
                    Permission.CAMERA,
                    Permission.CALL_PHONE,  # Permission to make phone calls
                ],
                callback,
            )
        except ImportError as e:
            logging.error(f"Android permissions module not found: {e}")
        except Exception as e:
            logging.error(f"Error while requesting permissions: {e}")

    def make_phone_call(self, phone_number: str):
        """
        Initiates a phone call to the given number, assuming permissions have been granted.

        :param phone_number: The phone number to call.
        """
        if not phone_number or not self.validate_phone_number(phone_number):
            logging.warning(f"Invalid phone number provided: {phone_number}")
            # Optionally, show a message to the user about invalid number
            return

        try:
            from android.permissions import Permission, check_permission
            from jnius import autoclass

            # Check if CALL_PHONE permission is granted
            if not check_permission(Permission.CALL_PHONE):
                logging.warning("CALL_PHONE permission not granted")
                # Optionally, notify the user about the missing permission (e.g., through a dialog)
                return

            # Get the Android Intent and Uri classes
            Intent = autoclass("android.content.Intent")
            Uri = autoclass("android.net.Uri")

            # Create an intent to initiate a call
            intent = Intent(Intent.ACTION_CALL)
            uri = Uri.parse(f"tel:{phone_number}")
            intent.setData(uri)

            # Get the current Android activity and start the call intent
            PythonActivity = autoclass("org.kivy.android.PythonActivity")
            activity = PythonActivity.mActivity
            activity.startActivity(intent)

            logging.info(f"Initiating call to {phone_number}")

        except Exception as e:
            logging.error(f"Error while making the phone call: {e}")

    def validate_phone_number(self, phone_number: str) -> bool:
        """
        Validates the phone number format to ensure it is valid before making a call.

        :param phone_number: The phone number to validate.
        :return: True if the phone number is valid, False otherwise.
        """
        # Basic check for valid phone number (this can be enhanced with regex)
        if phone_number and phone_number.isdigit() and len(phone_number) >= 10:
            return True
        return False
