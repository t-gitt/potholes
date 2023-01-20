from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import APIException
from predictions.models import Case, CaseAttachment
from predictions.services import PredictionService

class CaseSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True, write_only=True)
    results = serializers.ReadOnlyField()
    class Meta:
        model = Case
        fields = [
            'uuid',
            'image',
            'results'
        ]

    def create(self, validated_data):
        case_uuid = None
        if 'case' in validated_data:
            case_uuid = validated_data.pop('case')
        if not case_uuid:
            case = Case.objects.create()
        else:
            try:
                case = Case.objects.get(uuid=case_uuid)
            except Case.DoesNotExist:
                raise APIException('Case Not Found')

        attachment = CaseAttachment.objects.create(**validated_data)
        case.attachments.add(attachment)
        case.save()

        prediction_service = PredictionService(attachment, settings.MODEL_PATH)

        prediction_service.handle()

        return case