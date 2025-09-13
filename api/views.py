from api.models import Receita, Despesa
from api.serializers import ReceitaSerializer, DespesaSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

class ReceitaViewSet(viewsets.ViewSet):

    queryset = Receita.objects.all()

    def create(self, request):
        serializer = ReceitaSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        receita = serializer.save()

        return Response(
            ReceitaSerializer(receita).data,
            status=status.HTTP_201_CREATED   
        )
    
    def update(self, request, pk):

        receita = get_object_or_404(self.queryset, pk=pk)

        serializer = ReceitaSerializer(receita, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status.HTTP_400_BAD_REQUEST
        )


    def list(self, request):
        serializer = ReceitaSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        receita = get_object_or_404(self.queryset, pk=pk)
        serializer = ReceitaSerializer(receita)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        receita = get_object_or_404(self.queryset, pk=pk)
        receita.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class DespesaViewSet(viewsets.ViewSet):

    queryset = Despesa.objects.all()

    def create(self, request):
        serializer = DespesaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.erros,
            status=HTTP_400_BAD_REQUEST
        )

    def list(self, request):
        serializer = DespesaSerializer(self.queryset, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
            )
    
    def retrieve(self, request, pk):
        despesa = get_object_or_404(self.queryset, pk=pk)
        serializer = DespesaSerializer(despesa)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def update(self, request, pk):
        despesa = get_object_or_404(self.queryset, pk=pk)
        serializer = DespesaSerializer(despesa, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk):
        despesa = get_object_or_404(self.queryset, pk=pk)
        despesa.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )