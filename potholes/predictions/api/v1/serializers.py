from django.conf import settings
from rest_framework import serializers
from predictions.models import Case, CaseAttachment
# from predictions.services import PredictionService

class CaseSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='attachments.image', max_length=None, use_url=True)
    class Meta:
        model = Case
        fields = [
            'image',
        ]

    def create(self, validated_data):
        attachments = validated_data.pop('attachments')

        case = Case.objects.create(**validated_data)
        if attachments:
            attachments_list = []
            for attachment, image in attachments.items():
                attachment = CaseAttachment.objects.create(image=image)
                attachments_list.append(attachment)
            if attachments_list:
                case.attachments.set(attachments_list)
        

        # prediction_service = PredictionService(case, settings.MODEL_PATH)

        return case
