from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import APIException
from predictions.models import Case, CaseAttachment
from predictions.services import PredictionService

class CaseSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True, write_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    status = serializers.SerializerMethodField(
        'get_status',
        allow_null=True,
    )
    results = serializers.ReadOnlyField()
    class Meta:
        model = Case
        fields = [
            'uuid',
            'image',
            'status',
            'results',
            'created_at',
            'updated_at'
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

        try:
            prediction_service = PredictionService(attachment, settings.MODEL_PATH)
    
            prediction_service.handle()
        except APIException:
            case.status = Case.NO_POTHOLES
            case.save(update_fields=['status'])
            return case
        except Exception as exception:
            case.status = Case.FAILED
            case.save(update_fields=['status'])
            raise APIException(f"Prediction Failed {exception}")

        case.status = Case.PREDICTED
        case.save(update_fields=['status'])


        return case
    
    def get_status(self, obj):
        return obj.status_display