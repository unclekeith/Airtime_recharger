import logging

from kivy.animation import Animation
from kivy.clock import Clock  # noqa: F401
from kivy.utils import platform
from kivymd.uix.screen import MDScreen
from libs.applibs.generated_connection_manager import AuthRoutes, CoreRoutes


class WelcomeScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
    def on_enter(self):
        """Called when the screen is entered. Requests necessary permissions on Android."""
        if platform == "android":
            logging.info("Requesting Android permissions.")
            self.request_android_permissions()

    def move_login(self):
        if not self.ids.one.disabled:
            self.manager.push("login")

    def request_android_permissions(self):
        """
        Requests necessary Android permissions required to make a phone call.
        These permissions include external storage, camera, and call permissions.
        """
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
                    Permission.VIBRATE,
                    Permission.ACCESS_FINE_LOCATION,
                    Permission.ACCESS_COARSE_LOCATION,
                    Permission.POST_NOTIFICATIONS,
                    Permission.READ_CALENDAR,
                    Permission.USE_FINGERPRINT,
                ],
                callback,
            )
        except ImportError as e:
            logging.error(f"Android permissions module not found: {e}")
        except Exception as e:
            logging.error(f"Error while requesting permissions: {e}")
