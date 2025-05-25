import logging
from kivy.properties import BooleanProperty, StringProperty
from kivy.utils import platform
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from jnius import autoclass

class EconetDialScreen(MDScreen):
    phone_number = StringProperty("+263717794958")  # Default phone number
    hide_scratch = BooleanProperty(True)  # default to hidden

    def on_enter(self):
        """Called when the screen is entered. Requests necessary permissions on Android."""
        if platform == "android":
            self.request_android_permissions()

    def request_android_permissions(self):
        """Request Android runtime permissions."""
        try:
            from android.permissions import Permission, request_permissions

            def callback(permissions, results):
                for permission, result in zip(permissions, results):
                    status = "granted" if result else "denied"
                    logging.info(f"Permission {permission}: {status}")
                    if not result:
                        toast(f"Permission denied: {permission}")

            request_permissions(
                [
                    Permission.WRITE_EXTERNAL_STORAGE,
                    Permission.READ_EXTERNAL_STORAGE,
                    Permission.CAMERA,
                    Permission.CALL_PHONE,
                ],
                callback
            )
        except Exception as e:
            logging.error(f"Permission error: {e}")

    def numbers(self):
        """Concatenate code and scratch number, update phone_number, and call it."""
        code = self.manager.get_shared_data("cached_econet_postal_code") or "*121*"
        scratch = self.ids.scratch_number.text.strip()
        if not scratch.isdigit():
            toast("Invalid scratch number")
            return

        formatted_number = f"{code}{scratch}#"
        self.phone_number = formatted_number
        self.make_phone_call(self.phone_number)

    def make_phone_call(self, phone_number: str):
        """Initiates a phone call if valid and permissions are granted."""
        if not phone_number or not self.validate_phone_number(phone_number):
            toast("Invalid phone number")
            return

        try:
            from android.permissions import Permission, check_permission
            if not check_permission(Permission.CALL_PHONE):
                toast("CALL_PHONE permission not granted")
                return

            Intent = autoclass("android.content.Intent")
            Uri = autoclass("android.net.Uri")
            PythonActivity = autoclass("org.kivy.android.PythonActivity")

            intent = Intent(Intent.ACTION_CALL)
            intent.setData(Uri.parse(f"tel:{phone_number}"))
            activity = PythonActivity.mActivity
            activity.startActivity(intent)

        except Exception as e:
            logging.error(f"Failed to make call: {e}")
            toast("Error making call")

    def validate_phone_number(self, phone_number: str) -> bool:
        """Basic validation for dial code format."""
        return phone_number and phone_number.startswith("*") and phone_number.endswith("#")
