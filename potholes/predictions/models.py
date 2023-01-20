import uuid
from django.db import models

class Case(models.Model):
    NEW = 1
    PREDICTED = 2
    REVIEWED = 3
    DELETED = 4

    status_choices = (
        (NEW, 'New'),
        (PREDICTED, 'Predicted'),
        (REVIEWED, 'Reviewed'),
        (DELETED, 'Deleted'),
    )

    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    prediction = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=254, blank=True, null=True, choices=status_choices)
    to_review = models.BooleanField(default=False)

    def __str__(self):
        return str(self.uuid)

    @property
    def result_image(self):
        return 'images/{}'.format(self.uuid)

    @property
    def image(self):
        attachment = self.attachments.all().first()
        if attachment and attachment.image:
            return attachment.image
        return ''

class CaseAttachment(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    case = models.ForeignKey('Case', related_name='attachments', on_delete=models.CASCADE, blank=False, default=None, null=True)
    image = models.ImageField(
                upload_to='images/',
                max_length=254,
                blank=True,
                null=True
            )

    def __str__(self):
        return str(self.uuid)