# PORTAL_ADMIN/adminportal/meu_app/serializers.py

from rest_framework import serializers
from .models import Planos # Importe seus modelos

from .models import (
    AnaliseIa, AreasAtendimento, Assinatura, Clientes, ClientesPf, ClientesPj,
    DoresCliente, Equipes, FaixasFaturamento, GatewaysPagamento, Pagamento,
    Perguntas, Planos, RespostasQuestionarioPf, RespostasQuestionarioPj,
    Servicos, Transcricoes, Usuarios
)

class AnaliseIaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnaliseIa
        fields = '__all__'

class AreasAtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreasAtendimento
        fields = '__all__'

class AssinaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assinatura
        fields = '__all__'

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class ClientesPfSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientesPf
        fields = '__all__'

class ClientesPjSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientesPj
        fields = '__all__'

class DoresClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoresCliente
        fields = '__all__'

class EquipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipes
        fields = '__all__'

class FaixasFaturamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaixasFaturamento
        fields = '__all__'

class GatewaysPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GatewaysPagamento
        fields = '__all__'

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'

class PerguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perguntas
        fields = '__all__'
        
class ServicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicos
        fields = '__all__'
        
class PlanosSerializer(serializers.ModelSerializer):
    # Para exibir os detalhes dos serviços, use um serializer aninhado
    servicos = ServicosSerializer(many=True, read_only=True)
    # Ou, se você só precisa dos IDs dos serviços para escrita
    # servicos = serializers.PrimaryKeyRelatedField(queryset=Servicos.objects.all(), many=True)

    class Meta:
        model = Planos
        fields = '__all__'

class RespostasQuestionarioPfSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespostasQuestionarioPf
        fields = '__all__'

class RespostasQuestionarioPjSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespostasQuestionarioPj
        fields = '__all__'

class TranscricoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transcricoes
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'
        
class TranscribeRequestSerializer(serializers.Serializer):
    audio_url = serializers.URLField(required=False, allow_null=True)
    audio_file = serializers.FileField(required=False, allow_null=True)

    def validate(self, data):
        if not data.get('audio_url') and not data.get('audio_file'):
            raise serializers.ValidationError("É necessário fornecer 'audio_url' ou 'audio_file'.")
        if data.get('audio_url') and data.get('audio_file'):
            raise serializers.ValidationError("Forneça apenas 'audio_url' ou 'audio_file', não ambos.")
        return data