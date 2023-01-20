
from datetime import datetime
from django.conf import settings
from imageai.Detection.Custom import CustomObjectDetection
import os.path


class PredictionService:

    def __init__(self, prediction_case, model_path):
        self.prediction_case = prediction_case
        self.model_path = model_path
    
    def handle(self, image_path):

        detector = CustomObjectDetection()
        detector.setModelTypeAsYOLOv3()
        detector.setModelPath(self.model_path)
        detector.setJsonPath(settings.DETECTION_CONFIG_PATH)
        detector.loadModel()
        output_image_path = os.path.dirname(image_path) + "/" + str(self.prediction_case.uuid) + ".jpg"
        print('image_path', image_path)
        print('output_image_path', output_image_path)
        detections = detector.detectObjectsFromImage(minimum_percentage_probability=25,
                                                    input_image=image_path,
                                                    output_image_path=output_image_path)
        
        print("No of potholes detected: " + str(len(detections)))
        for detection in detections:
            print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
        return output_image_path
    
        