from rest_framework import viewsets
from predictions.models import Case
from .serializers import CaseSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated  # <-- Here


class CaseViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)             # <-- And here
    authentication_classes = [TokenAuthentication,]
    serializer_class = CaseSerializer
    queryset = Case.objects.all()
