from rest_framework import serializers
from qrcode import models

class CasoSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Caso
        fields='__all__'

class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Historico
        fields='__all__'

class AvariasSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Avarias
        fields='__all__'

class InformacaoSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,use_url=True)
    doc=serializers.FileField(max_length=None,use_url=True)
    video=serializers.FileField(max_length=None,use_url=True)
    class Meta:
        model= models.Informacao
        fields='__all__'

class FotosSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model= models.Fotos
        fields='__all__'