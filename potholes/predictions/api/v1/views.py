from rest_framework import viewsets
from predictions.models import Case
from .serializers import CaseSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated  # <-- Here


class CaseViewSet(viewsets.ModelViewSet):
    # to do
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = [TokenAuthentication,]
    serializer_class = CaseSerializer
    queryset = Case.objects.all().exclude(status=Case.NO_POTHOLES)
