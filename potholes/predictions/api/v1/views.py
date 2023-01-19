from rest_framework import viewsets
from predictions.models import Case
from .serializers import CaseSerializer

class CaseViewSet(viewsets.ModelViewSet):
    serializer_class = CaseSerializer
    queryset = Case.objects.all()