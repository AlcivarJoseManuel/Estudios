from rest_framework import serializers
from .models import Programmer


class ProgrammerSerializer (serializers.ModelSerializer):   
    class Meta:
        model = Programmer
        # fields = ('fullname', 'nickname') para selecionar ciertos campos pero daria un problema ya que se necesita una primary key
        fields = '__all__'
