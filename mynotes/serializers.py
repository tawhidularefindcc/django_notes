from rest_framework import serializers

from . import models

class NoteSerielizer(serializers.ModelSerializer):
    class Meta:
        model = models.Note
        fields = '__all__'