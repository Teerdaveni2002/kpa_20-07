from rest_framework import serializers
from .models import BogieDetails, BogieChecksheet, BMBCChecksheet, BogieFormSubmission


class BogieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieDetails
        fields = '__all__'


class BogieChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieChecksheet
        fields = '__all__'


class BMBCChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BMBCChecksheet
        fields = '__all__'


class BogieFormSubmissionSerializer(serializers.ModelSerializer):
    bogie_checksheet = BogieChecksheetSerializer()
    bmbc_checksheet = BMBCChecksheetSerializer()

    class Meta:
        model = BogieFormSubmission
        fields = '__all__'

    def create(self, validated_data):
        bogie_checksheet_data = validated_data.pop('bogie_checksheet')
        bmbc_checksheet_data = validated_data.pop('bmbc_checksheet')

        bogie_checksheet = BogieChecksheet.objects.create(**bogie_checksheet_data)
        bmbc_checksheet = BMBCChecksheet.objects.create(**bmbc_checksheet_data)

        return BogieFormSubmission.objects.create(
            bogie_checksheet=bogie_checksheet,
            bmbc_checksheet=bmbc_checksheet,
            **validated_data
        )
