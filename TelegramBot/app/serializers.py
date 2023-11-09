from rest_framework import serializers
from .models import DailyMessages, ProgressBarStatus

class DailyMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyMessages
        fields = '__all__'

class ProgressBarStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProgressBarStatus
        fields = '__all__'