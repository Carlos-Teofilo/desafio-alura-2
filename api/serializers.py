from rest_framework import serializers

from api.models import Receita, Despesa
from api import validators

class ReceitaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Receita
        fields = '__all__'
        read_only_fields = ['id']

    def validate(self, data):

        if not validators.descricao_already_exists_in_same_month(data):
            raise serializers.ValidationError("A descrição já existe no mesmo mês")
        
        return data

    def update(self, instance, validated_data):
        instance.descricao = validated_data.get('descricao', instance.descricao)
        instance.valor = validated_data.get('valor', instance.valor)
        instance.data = validated_data.get('data', instance.data)
        instance.save()
        
        return instance


class DespesaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Despesa
        fields = '__all__'
        read_only_fields = ['id']

    def validate(self, data):

        if not validators.descricao_already_exists_in_same_month(data):
            raise serializers.ValidationError("A descrição já existe no mesmo mês")
        
        return data

    def update(self, instance, validated_data):
        instance.descricao = validated_data.get('descricao', instance.descricao)
        instance.valor = validated_data.get('valor', instance.valor)
        instance.data = validated_data.get('data', instance.data)
        instance.save()

        return instance