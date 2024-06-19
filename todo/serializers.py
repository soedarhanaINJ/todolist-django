from rest_framework import serializers
from .models import appTodo

class AppTodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = appTodo
        fields = ('id', 'title', 'detail', 'created_at', 'completed' )