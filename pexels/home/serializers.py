from rest_framework import serializers
from home.models import *

class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = File
        fields = ('file', 'timestamp')