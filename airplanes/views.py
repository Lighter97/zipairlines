from rest_framework.decorators import api_view
from rest_framework.response import Response

from airplanes.serializers import FleetSerializer


@api_view(["POST"])
def calculate_fleet(request):
    serializer = FleetSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data)
