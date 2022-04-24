from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, CreateAPIView, get_object_or_404, ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer
# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


class smart_house_api_id(RetrieveAPIView, RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class smart_house_api(APIView):

    def get(self, request):
        sensor = Sensor.objects.all()
        ser = SensorDetailSerializer(sensor, many=True)
        return Response(ser.data)



    def post(self, request):
        post_new = Sensor.objects.create(
            name = request.data['name'],
            description = request.data['description']
        )
        ser = SensorDetailSerializer(post_new)
        return Response(ser.data)

class Measurements_api(CreateAPIView, ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def perform_create(self, serializer):
        sensor = get_object_or_404(Sensor, id=self.request.data.get('sensor'))
        serializer.save(sensor=sensor)
        return Response(serializer.data)