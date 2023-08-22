from rest_framework import serializers

from eventos.models import Categoria, Evento


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = [
            'id',
            'nome',
            'criado_em',
            'modificado_em',
        ]


class EventoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evento
        fields = [
            'id',
            'nome',
            'categoria',
            'data',
            'observacoes',
            'destaque',
            'criado_em',
            'modificado_em',
        ]
