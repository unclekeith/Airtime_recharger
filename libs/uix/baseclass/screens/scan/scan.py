import cv2
import numpy as np
from pyzbar.pyzbar import decode
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.screen import MDScreen
import cv2
import pytesseract

class BarcodeScannerScreen(MDScreen):

# Configure to recognize digits only
    config = r'--oem 3 --psm 6 outputbase digits'

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to grayscale (improves OCR accuracy)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Extract numbers
        numbers = pytesseract.image_to_string(gray, config=config)
        print("Detected numbers:", numbers)

        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()








import cv2
import numpy as np
import pytesseract
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel


class BarcodeScannerScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # OCR config to extract digits only
        self.config = r'--oem 3 --psm 6 outputbase digits'

        # Set up camera
        self.capture = cv2.VideoCapture(0)

        # UI elements
        self.image = Image()
        self.label = MDLabel(text="Detected: ", halign="center", theme_text_color="Custom", text_color=(1, 1, 1, 1))
        
        self.add_widget(self.image)
        self.add_widget(self.label)

        # Schedule camera updates
        Clock.schedule_interval(self.update, 1.0 / 30.0)

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # Convert to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # OCR to get digits only
            text = pytesseract.image_to_string(gray, config=self.config)
            numbers = ''.join(filter(str.isdigit, text))
            if numbers:
                print("Detected numbers:", numbers)
                self.label.text = f"Detected: {numbers}"

            # Convert image to Kivy texture
            buf = cv2.flip(frame, 0).tobytes()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.image.texture = texture

    def on_stop(self):
        self.capture.release()


class ScannerApp(MDApp):
    def build(self):
        return BarcodeScannerScreen()


if __name__ == '__main__':
    ScannerApp().run()
