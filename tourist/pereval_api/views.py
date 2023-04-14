from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Pereval_added
from .serializers import PerevalSerializer


class PerevalViewSet(ModelViewSet):
    queryset = Pereval_added.objects.all()
    serializer_class = PerevalSerializer


@api_view(['POST'])
def submit_data(request):
    serializer = PerevalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
