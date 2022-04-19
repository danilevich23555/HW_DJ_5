from rest_framework import serializers
from measurement.models import Measurement, Sensor




class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

    # def create(self, validated_data):
    #     profile_data = validated_data.pop('measurements')
    #     sensor = Sensor.objects.create(**validated_data)
    #     Measurement.objects.create(sensor=sensor, **profile_data)
    #     return sensor