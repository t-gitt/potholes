
from datetime import datetime
from django.conf import settings
from imageai.Detection.Custom import CustomObjectDetection
from urllib.parse import urljoin
import os.path


class PredictionService:

    def __init__(self, attachment, model_path):
        self.attachment = attachment
        self.model_path = model_path
    
    def handle(self):

        image_path = self.attachment.image.path

        detector = CustomObjectDetection()
        detector.setModelTypeAsYOLOv3()
        detector.setModelPath(self.model_path)
        detector.setJsonPath(settings.DETECTION_CONFIG_PATH)
        detector.loadModel()
        output_image_path = settings.STATIC_ROOT + "/images" + "/processed/" + str(self.attachment.uuid) + ".jpg"
        detections = detector.detectObjectsFromImage(
            minimum_percentage_probability=25,
            input_image=image_path,
            output_image_path=output_image_path
        )

        attachment = self.attachment
        attachment.detections = detections
        attachment.result_image = urljoin(os.path.dirname(attachment.image.url), "processed/" + str(attachment.uuid) + ".jpg").replace('images/', '')

        attachment.save()