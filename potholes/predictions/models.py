import uuid
from django.db import models
from django.conf import settings

class Case(models.Model):
    NEW = 1
    PREDICTED = 2
    REVIEWED = 3
    NO_POTHOLES = 4
    DELETED = 5
    FAILED = 6

    status_choices = (
        (NEW, 'New'),
        (PREDICTED, 'Predicted'),
        (REVIEWED, 'Reviewed'),
        (NO_POTHOLES, 'No Potholes'),
        (DELETED, 'Deleted'),
        (FAILED, 'Failed'),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    status = models.IntegerField(default=1, choices=status_choices)
    to_review = models.BooleanField(default=False)

    def __str__(self):
        return str(self.uuid)
    
    @property
    def status_display(self):
        return dict(Case.status_choices).get(self.status, 'Unknown')

    @property
    def results(self):
        return [{'image': attachment.image.url, 'result_image': attachment.result_image, 'detections': attachment.detections} for attachment in self.attachments.all()]

    @property
    def image(self):
        attachment = self.attachments.all().first()
        if attachment and attachment.image:
            return attachment.image
        return ''

class CaseAttachment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    case = models.ForeignKey('Case', related_name='attachments', on_delete=models.CASCADE, blank=False, default=None, null=True)
    image = models.ImageField(
                upload_to=settings.STATIC_ROOT+'images/img/',
                max_length=254,
                blank=True,
                null=True
            )
    detections = models.JSONField(default=dict, blank=True)
    result_image = models.URLField(max_length=200)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return str(self.uuid)
