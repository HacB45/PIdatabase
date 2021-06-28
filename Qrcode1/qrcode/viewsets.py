from rest_framework import viewsets
from qrcode import serializer
from qrcode import models
from rest_framework import generics
from rest_framework.decorators import api_view
from qrcode.models import Caso, Historico, Avarias, Informacao, Fotos
from rest_framework.response import Response
from django.http import JsonResponse

class CasoManutencaoViewSet(generics.ListCreateAPIView):
    serializer_class = serializer.CasoSerializer
    queryset= models.Caso.objects.all()
    

class HistoricoViewSet(generics.ListCreateAPIView):
    serializer_class = serializer.HistoricoSerializer
    queryset= models.Historico.objects.all()


class AvariasViewSet(generics.ListCreateAPIView):
    serializer_class = serializer.AvariasSerializer
    queryset= models.Avarias.objects.all()


class InformacaoViewSet(generics.ListCreateAPIView):
    serializer_class = serializer.InformacaoSerializer
    queryset= models.Informacao.objects.all()

class FotosViewSet(generics.ListCreateAPIView):
    serializer_class = serializer.FotosSerializer
    queryset= models.Fotos.objects.all()

@api_view(['GET'])
def user_detail(request, pk):

    try:
        avaria = Historico.objects.get(pk = pk)
    except Historico.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

   
    avaria.delete()
    return Response()



@api_view(['GET'])
def user_details(request, pk):

    try:
        avaria = Historico.objects.filter(idmaquina = pk).values()
        
    except Historico.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
   
    return JsonResponse({"list": list(avaria)})
    

@api_view(['GET'])
def user_detail2(request, pk):

    try:
        info = Fotos.objects.get(pk = pk)
    except Fotos.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

   
    info.delete()
    return Response()



@api_view(['GET'])
def user_details2(request, pk):

    try:
        info = Fotos.objects.filter(idmaquina = pk).values()
        
    except Fotos.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
   
    return JsonResponse({"list": list(info)})
