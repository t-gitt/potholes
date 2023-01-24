from rest_framework import viewsets
from predictions.models import Case
from .serializers import CaseSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated 


class CaseViewSet(viewsets.ModelViewSet):
    # to do
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = [TokenAuthentication,]
    serializer_class = CaseSerializer
    queryset = Case.objects.all().order_by('-created_at')

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset()).exclude(status=Case.NO_POTHOLES).exclude(status=Case.DELETED)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        instance = self.get_object()
        instance.status = Case.DELETED
        instance.save(update_fields=['status'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_object(self):
        """Retrieve object using uuid field instead of primary key"""
        lookup_field = 'uuid'
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        lookup = self.kwargs[lookup_url_kwarg]
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        filter_kwargs = {lookup_field: lookup}
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj
