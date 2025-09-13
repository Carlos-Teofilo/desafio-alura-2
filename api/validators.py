from api.models import Receita, Despesa
from datetime import datetime


def descricao_field_is_valid(value) -> bool:
    return bool(value.strip())


def descricao_already_exists_in_same_month(data) -> bool:

    value_descricao = data.get('descricao') 
    value_data = data.get('data')

    receitas = Receita.objects.filter(
        descricao__iexact=value_descricao,
        data__month=value_data.month,
        )
    
    return not len(receitas) > 0
