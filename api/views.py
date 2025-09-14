from api.models import Receita, Despesa
from api.serializers import ReceitaSerializer, DespesaSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

class ReceitaViewSet(viewsets.ModelViewSet):

    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer


class DespesaViewSet(viewsets.ModelViewSet):

    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
