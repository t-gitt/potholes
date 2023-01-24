from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import APIException
from predictions.models import Case, CaseAttachment
from predictions.services import PredictionService

class StatusSerializerField(serializers.Field):

    VALUE_MAP = dict(Case.status_choices)

    def to_representation(self, obj):
        return self.VALUE_MAP[obj]            

    def to_internal_value(self, data):
        try:
            return {k:v for v,k in self.VALUE_MAP.items()}[data]
        except KeyError:
            raise APIException("Invalid status. Status ({0}) is not one of the following: {1}".format(data, ', '.join(self.VALUE_MAP.values())))


class CaseSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True, write_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    status = StatusSerializerField(allow_null=True, default=1)
    case = serializers.UUIDField(write_only=True, allow_null=True, required=False)
    # status = serializers.IntegerField(allow_null=True, default=1, choices=Case.status_choices)
    to_review = serializers.BooleanField(allow_null=True, default=False)
    results = serializers.ReadOnlyField()

    class Meta:
        model = Case
        fields = [
            'uuid',
            'created_at',
            'updated_at',
            'status',
            'to_review',
            'results',

            'image',
            'case'
        ]
    
    def update(self, instance, validated_data):
        instance.to_review = validated_data.get('to_review', instance.to_review)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

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

        image = validated_data.pop('image')
        attachment = CaseAttachment.objects.create(image=image)
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