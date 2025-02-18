import requests
from io import BytesIO
from PyQt6.QtCore import QThread, pyqtSignal, QObject
from PyQt6.QtGui import QImage

class AITools(QObject):
    api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"

    def __init__(self, api_key):
        super().__init__()
        self.api_key = api_key
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

class AIWorker(QThread):
    progress = pyqtSignal(int)
    result = pyqtSignal(QImage)
    error = pyqtSignal(str)

    def __init__(self, api_key, prompt):
        super().__init__()
        self.api_key = api_key
        self.prompt = prompt

    def run(self):
        try:
            response = requests.post(
                AITools.api_url,
                headers={"Authorization": f"Bearer {self.api_key}"},
                json={"inputs": self.prompt},
                stream=True
            )

            if response.status_code == 200:
                image_data = BytesIO(response.content)
                image = QImage.fromData(image_data.getvalue())
                self.result.emit(image)
            else:
                self.error.emit(f"API Error: {response.text}")

        except Exception as e:
            self.error.emit(str(e))