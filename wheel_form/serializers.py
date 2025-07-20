# serializers.py

from rest_framework import serializers
from .models import WheelSpecification

class WheelSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecification
        fields = '__all__'
from rest_framework import serializers
# from .models import Wheel

class WheelFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecification
        fields = '__all__'

    def validate(self, data):
        if data.get('wheel_condition') == 'other' and not data.get('other_comment'):
            raise serializers.ValidationError({"other_comment": "This field is required when condition is 'other'."})
        return data
