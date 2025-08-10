# PORTAL_ADMIN/adminportal/meu_app/admin.py

from django.contrib import admin
from .models import (
    AnaliseIa, AreasAtendimento, Assinatura, Clientes, ClientesPf, ClientesPj,
    DoresCliente, Equipes, FaixasFaturamento, GatewaysPagamento, Pagamento,
    Perguntas, PlanoServico, Planos, RespostasQuestionarioPf, RespostasQuestionarioPj,
    Servicos, Transcricoes, Usuarios,Credential
)


@admin.register(Credential)
class CredentialAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'updated_at')
    search_fields = ('name', 'description')
    fields = ('name', 'value', 'description')
    
# --- Classes ModelAdmin para cada modelo ---

@admin.register(AnaliseIa)
class AnaliseIaAdmin(admin.ModelAdmin):
    list_display = ('id_analise', 'id_transcricao_fk', 'id_servico_fk', 'data_analise', 'created_by_fk')
    search_fields = ('resultado_analise',)
    list_filter = ('data_analise', 'id_servico_fk')

@admin.register(AreasAtendimento)
class AreasAtendimentoAdmin(admin.ModelAdmin):
    list_display = ('nome_area', 'id_area_atendimento', 'descricao', 'created_by_fk') # nome_area primeiro
    search_fields = ('nome_area', 'descricao',)
    list_filter = ('nome_area',)

@admin.register(Assinatura)
class AssinaturaAdmin(admin.ModelAdmin):
    list_display = ('id_assinatura', 'id_cliente_fk', 'id_plano_fk', 'data_inicio', 'data_fim', 'status', 'valor_total')
    search_fields = ('status', 'motivo_cancelamento',)
    list_filter = ('status', 'renovacao_automatica', 'id_plano_fk',)

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'created_at', 'created_by_fk')
    search_fields = () # Sem campos de texto diretos para busca
    list_filter = ('created_at',)

@admin.register(ClientesPf)
class ClientesPfAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id_cliente_fk', 'email', 'cpf', 'id_area_atendimento_fk', 'id_equipe_fk') # nome primeiro
    search_fields = ('nome', 'email', 'cpf', 'telefone',)
    list_filter = ('genero', 'id_area_atendimento_fk', 'id_equipe_fk', 'id_uso_fk',)

@admin.register(ClientesPj)
class ClientesPjAdmin(admin.ModelAdmin):
    list_display = ('razao_social', 'id_cliente_fk', 'cnpj', 'email_empresa', 'id_area_atendimento_fk', 'id_equipe_fk') # razao_social primeiro
    search_fields = ('razao_social', 'cnpj', 'email_empresa',)
    list_filter = ('id_area_atendimento_fk', 'id_faixa_faturamento_fk', 'id_equipe_fk',)

@admin.register(DoresCliente)
class DoresClienteAdmin(admin.ModelAdmin):
    list_display = ('descricao_dor', 'id_dor', 'created_by_fk') # descricao_dor primeiro
    search_fields = ('descricao_dor',)
    list_filter = ('descricao_dor',)

@admin.register(Equipes)
class EquipesAdmin(admin.ModelAdmin):
    # Ajustado para que 'faixa_tamanho' seja o primeiro item, pois é o que __str__ retorna
    list_display = ('faixa_tamanho', 'id_equipe', 'created_by_fk')
    search_fields = ('faixa_tamanho',)
    list_filter = ('faixa_tamanho',)

@admin.register(FaixasFaturamento)
class FaixasFaturamentoAdmin(admin.ModelAdmin):
    list_display = ('descricao_faixa', 'id_faixa_faturamento', 'valor_minimo', 'valor_maximo', 'created_by_fk') # descricao_faixa primeiro
    search_fields = ('descricao_faixa',)
    list_filter = ('descricao_faixa',)

@admin.register(GatewaysPagamento)
class GatewaysPagamentoAdmin(admin.ModelAdmin):
    list_display = ('nome_gateway', 'id_gateway', 'url_api', 'created_by_fk') # nome_gateway primeiro
    search_fields = ('nome_gateway', 'url_api',)
    list_filter = ('nome_gateway',)

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('id_pagamento', 'id_assinatura_fk', 'status_pagamento', 'tipo_pagamento', 'data_pagamento', 'valor_pago', 'id_gateway_fk')
    search_fields = ('status_pagamento', 'tipo_pagamento',)
    list_filter = ('status_pagamento', 'tipo_pagamento', 'data_pagamento', 'id_gateway_fk',)

@admin.register(Perguntas)
class PerguntasAdmin(admin.ModelAdmin):
    list_display = ('texto_pergunta', 'id_pergunta', 'tipo_resposta', 'ativa', 'ordem_exibicao') # texto_pergunta primeiro
    search_fields = ('texto_pergunta',)
    list_filter = ('tipo_resposta', 'ativa',)

@admin.register(PlanoServico)
class PlanoServicoAdmin(admin.ModelAdmin):
    # Use os nomes dos campos ForeignKey: 'plano' e 'servico'
    # Se 'limite_uso' for adicionado ao modelo, inclua-o aqui.
    list_display = ('plano', 'servico', 'limite_uso') # Adicione 'limite_uso' se ele existir no modelo
    list_filter = ('plano', 'servico') # Use 'plano' e 'servico' para filtrar
    search_fields = ('plano__nome_plano', 'servico__nome_servico') # Exemplo de busca

@admin.register(Planos)
class PlanosAdmin(admin.ModelAdmin):
    list_display = ('nome_plano', 'id_plano', 'preco', 'duracao_meses', 'codigo_plano', 'permite_cadastro_usuarios_pj') # nome_plano primeiro
    search_fields = ('nome_plano', 'codigo_plano',)
    list_filter = ('permite_cadastro_usuarios_pj',)

@admin.register(RespostasQuestionarioPf)
class RespostasQuestionarioPfAdmin(admin.ModelAdmin):
    list_display = ('id_resposta_pf', 'id_cliente_fk', 'id_pergunta_fk', 'data_resposta')
    search_fields = ('resposta',)
    list_filter = ('id_pergunta_fk', 'data_resposta',)

@admin.register(RespostasQuestionarioPj)
class RespostasQuestionarioPjAdmin(admin.ModelAdmin):
    list_display = ('id_resposta_pj', 'id_cliente_fk', 'id_pergunta_fk', 'data_resposta')
    search_fields = ('resposta',)
    list_filter = ('id_pergunta_fk', 'data_resposta',)

@admin.register(Servicos)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('nome_servico', 'id_servico', 'ativo', 'created_by_fk') # nome_servico primeiro
    search_fields = ('nome_servico', 'descricao',)
    list_filter = ('ativo', 'nome_servico',)

@admin.register(Transcricoes)
class TranscricoesAdmin(admin.ModelAdmin):
    list_display = ('id_transcricao', 'id_assinatura_fk', 'id_servico_fk', 'data_transcricao', 'duracao_segundos', 'custo_minutos')
    search_fields = ('url_audio_original', 'url_transcricao_texto',)
    list_filter = ('data_transcricao', 'id_servico_fk',)

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'id_user', 'email', 'telefone', 'id_funcao_fk', 'status') # nome primeiro
    search_fields = ('email', 'nome', 'telefone',)
    list_filter = ('id_funcao_fk', 'status',)
