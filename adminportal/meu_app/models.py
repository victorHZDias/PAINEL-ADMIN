# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings # Importe settings para acessar AUTH_USER_MODEL
from .encrypted_fields import EncryptedCharField # <--- Importe este campo
# --- Definição dos CHOICES para os ENUMs do Banco de Dados ---
# Mapeamento dos ENUMs do PostgreSQL para choices do Django

AREA_ATENDIMENTO_CHOICES = [
    ('SAC (sistema de atendimento ao cliente)', 'SAC (Sistema de Atendimento ao Cliente)'),
    ('vendas_telemarketing_ativo_receptivo', 'Vendas - Telemarketing Ativo/Receptivo'),
    ('suporte_tecnico_pos_venda', 'Suporte Técnico Pós-Vendas'),
    ('retencao_fidelizacao', 'Retenção e Fidelização'),
    ('pesquisa_satisfacao_cliente', 'Pesquisa de Satisfação do Cliente'),
    ('relacionamento_cliente_pos_vendas', 'Relacionamento com Cliente Pós-Vendas'),
]

DORES_CLIENTE_CHOICES = [
    ('alta_taxa_churn_clientes_insatisfeitos', 'Alta Taxa de Churn / Clientes Insatisfeitos'),
    ('falta_conformidade_legal_regulatoria', 'Falta de Conformidade Legal/Regulatória'),
    ('falhas_processos_procedimentos_internos', 'Falhas em Processos e Procedimentos Internos'),
    ('falta_padronizacao_atendimento', 'Falta de Padronização no Atendimento'),
    ('alto_tempo_medio_atendimento_tma_tpr', 'Alto Tempo Médio de Atendimento (TMA/TPR)'),
    ('Gaps de Treinamento e Desenvolvimento de Agentes', 'Gaps de Treinamento e Desenvolvimento de Agentes'),
]

EQUIPE_TAMANHO_CHOICES = [
    ('1_5', '1-5 Pessoas'),
    ('6_10', '6-10 Pessoas'),
    ('11_20', '11-20 Pessoas'),
    ('21_50', '21-50 Pessoas'),
    ('51_100', '51-100 Pessoas'),
    ('101_200', '101-200 Pessoas'),
    ('201_500', '201-500 Pessoas'),
    ('501_1000', '501-1000 Pessoas'),
    ('1001_2000', '1001-2000 Pessoas'),
    ('2001_5000', '2001-5000 Pessoas'),
    ('5001_mais', '5001+ Pessoas'),
]

FAIXA_FATURAMENTO_CHOICES = [
    ('r500_r1_000_000', 'Até R$ 1.000.000'),
    ('r1_000_000_r5_000_000', 'R$ 1.000.000 - R$ 5.000.000'),
    ('r5_000_000_r10_000_000', 'R$ 5.000.000 - R$ 10.000.000'),
    ('r10_000_000_r25_000_000', 'R$ 10.000.000 - R$ 25.000.000'),
    ('r25_000_000_r50_000_000', 'R$ 25.000.000 - R$ 50.000.000'),
    ('r50_000_000_r100_000_000', 'R$ 50.000.000 - R$ 100.000.000'),
    ('r100_000_000_r500_000_000', 'R$ 100.000.000 - R$ 500.000.000'),
    ('r500_000_000_mais', 'Acima de R$ 500.000.000'),
]

FUNCAO_USUARIO_CHOICES = [
    ('agente', 'Agente'),
    ('supervisor', 'Supervisor'),
    ('admin', 'Administrador'),
]

MOTIVO_CANCELAMENTO_CHOICES = [
    ('preco_servico_alto', 'Preço do Serviço Alto'),
    ('produto_servico_nao_atendeu_necessidade', 'Produto/Serviço Não Atendeu Necessidade'),
    ('encontrou_outra_solucao', 'Encontrou Outra Solução'),
    ('outros', 'Outros'),
]

SERVICOS_CHOICES = [
    ('transcricao_audio', 'Transcrição de Áudio'),
    ('entidades_nomeadas', 'Entidades Nomeadas'),
    ('topicos', 'Tópicos'),
    ('frases_chave', 'Frases Chave'),
    ('redacao_audio', 'Redação de Áudio'),
    ('analise_sentimento', 'Análise de Sentimento'),
    ('capitulos_automaticos', 'Capítulos Automáticos'),
    ('resumo_texto', 'Resumo de Texto'),
]

STATUS_GENERICO_CHOICES = [
    ('ativo', 'Ativo'),
    ('inativo', 'Inativo'),
    ('pendente', 'Pendente'),
]

STATUS_PAGAMENTO_CHOICES = [
    ('aprovado', 'Aprovado'),
    ('reprovado', 'Reprovado'),
    ('pendente', 'Pendente'),
]

TIPO_PAGAMENTO_CHOICES = [
    ('cartao_credito', 'Cartão de Crédito'),
    ('cartao_debito', 'Cartão de Débito'),
    ('pix', 'Pix'),
    ('boleto', 'Boleto'),
]

STATUS_ASSINATURA_CHOICES = [
    ('ativa', 'Ativa'),
    ('suspensa', 'Suspensa'),
    ('cancelada', 'Cancelada'),
    ('pendente', 'Pendente'),
    ('expirada', 'Expirada'),
    ('aguardando_pagamento', 'Aguardando Pagamento'),
]

TIPO_USO_CLIENTE_CHOICES = [
    ('pessoal', 'Pessoal'),
    ('profissional', 'Profissional'),
    ('academico', 'Acadêmico'),
]

# Novo choice para o tipo de plano (gratuito/pago)
TIPO_PLANO_CHOICES = [
    ('gratuito', 'Gratuito'),
    ('pago', 'Pago'),
]


class AnaliseIa(models.Model):
    id_analise = models.AutoField(primary_key=True)
    id_transcricao_fk = models.ForeignKey('Transcricoes', models.DO_NOTHING, db_column='id_transcricao_fk')
    id_servico_fk = models.ForeignKey('Servicos', models.DO_NOTHING, db_column='id_servico_fk')
    data_analise = models.DateTimeField(blank=True, null=True)
    resultado_analise = models.TextField(blank=True, null=True)
    entidades_nomeadas = models.TextField(blank=True, null=True)
    topicos = models.TextField(blank=True, null=True)
    frases_chave = models.TextField(blank=True, null=True)
    resumo_texto = models.TextField(blank=True, null=True)
    analise_sentimento = models.TextField(blank=True, null=True)
    capitulos_automaticos = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # Ajustado para auto_now_add
    updated_at = models.DateTimeField(auto_now=True)     # Ajustado para auto_now
    created_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by_fk', blank=True, null=True)
    updated_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='updated_by_fk', related_name='analiseia_updated_by_fk_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analise_ia'
        verbose_name = 'Análise de IA'
        verbose_name_plural = 'Análises de IA'

    def __str__(self):
        return f"Análise {self.id_analise} - Serviço: {self.id_servico_fk.nome_servico if self.id_servico_fk else 'N/A'}"


class AreasAtendimento(models.Model):
    id_area_atendimento = models.AutoField(primary_key=True)
    nome_area = models.CharField(
        unique=True,
        max_length=100,
        choices=AREA_ATENDIMENTO_CHOICES,
        help_text="Nome da área de atendimento."
    )
    descricao = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # Ajustado para auto_now_add
    updated_at = models.DateTimeField(auto_now=True)     # Ajustado para auto_now
    created_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by_fk', blank=True, null=True)
    updated_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='updated_by_fk', related_name='areasatendimento_updated_by_fk_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areas_atendimento'
        verbose_name = 'Área de Atendimento'
        verbose_name_plural = 'Áreas de Atendimento'

    def __str__(self):
        return self.get_nome_area_display()


class Assinatura(models.Model):
    id_assinatura = models.AutoField(primary_key=True)
    id_cliente_fk = models.ForeignKey('Clientes', models.DO_NOTHING, db_column='id_cliente_fk')
    id_plano_fk = models.ForeignKey('Planos', models.DO_NOTHING, db_column='id_plano_fk')
    renovacao_automatica = models.BooleanField(blank=True, null=True)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=30,
        choices=STATUS_ASSINATURA_CHOICES,
        help_text="Status atual da assinatura."
    )
    data_status_atualizacao = models.DateTimeField(blank=True, null=True)
    politica_cancelamento = models.TextField(blank=True, null=True)
    motivo_cancelamento = models.CharField(
        max_length=50,
        choices=MOTIVO_CANCELAMENTO_CHOICES,
        blank=True,
        null=True,
        help_text="Motivo do cancelamento da assinatura."
    )
    created_at = models.DateTimeField(auto_now_add=True) # Ajustado para auto_now_add
    updated_at = models.DateTimeField(auto_now=True)     # Ajustado para auto_now
    created_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by_fk', blank=True, null=True)
    updated_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='updated_by_fk', related_name='assinatura_updated_by_fk_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assinatura'
        verbose_name = 'Assinatura'
        verbose_name_plural = 'Assinaturas'

    def __str__(self):
        cliente_nome = 'N/A'
        if self.id_cliente_fk:
            try:
                cliente_nome = self.id_cliente_fk.clientespf.nome
            except: # Usar um except mais específico como ClientesPf.DoesNotExist
                try:
                    cliente_nome = self.id_cliente_fk.clientespj.razao_social
                except: # Usar um except mais específico como ClientesPj.DoesNotExist
                    pass
        plano_nome = self.id_plano_fk.nome_plano if self.id_plano_fk else 'N/A'
        return f"Assinatura {self.id_assinatura} - Cliente: {cliente_nome} - Plano: {plano_nome}"

    # Lógica para garantir uso único de plano gratuito por cliente (exemplo)
    # Isso seria melhor implementado em um serializer ou view para validação
    # def clean(self):
    #     from django.core.exceptions import ValidationError
    #     if self.id_plano_fk and self.id_plano_fk.tipo_plano == 'gratuito':
    #         if Assinatura.objects.filter(id_cliente_fk=self.id_cliente_fk, id_plano_fk__tipo_plano='gratuito').exists():
    #             raise ValidationError("Este cliente já utilizou um plano gratuito.")


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'

    def __str__(self):
        return self.name


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)

    def __str__(self):
        return f"{self.group.name} - {self.permission.codename}"


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

    def __str__(self):
        return f"{self.content_type.app_label}.{self.model} | {self.name}"


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

    def __str__(self):
        return self.username


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)

    def __str__(self):
        return f"{self.user.username} - {self.group.name}"


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

    def __str__(self):
        return f"{self.user.username} - {self.permission.codename}"


class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True) # Ajustado para auto_now_add
    updated_at = models.DateTimeField(auto_now=True)     # Ajustado para auto_now
    created_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by_fk', blank=True, null=True)
    updated_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='updated_by_fk', related_name='clientes_updated_by_fk_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        try:
            return self.clientespf.nome
        except: # Usar um except mais específico como ClientesPf.DoesNotExist
            pass
        try:
            return self.clientespj.razao_social
        except: # Usar um except mais específico como ClientesPj.DoesNotExist
            pass
        return f"Cliente {self.id_cliente}"


class ClientesPf(models.Model):
    id_cliente_fk = models.OneToOneField('Clientes', models.DO_NOTHING, db_column='id_cliente_fk', primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    cpf = models.CharField(unique=True, max_length=14, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    id_area_atendimento_fk = models.ForeignKey(AreasAtendimento, models.DO_NOTHING, db_column='id_area_atendimento_fk', blank=True, null=True)
    id_equipe_fk = models.ForeignKey('Equipes', models.DO_NOTHING, db_column='id_equipe_fk', blank=True, null=True)
    id_uso_fk = models.CharField(
        max_length=20,
        choices=TIPO_USO_CLIENTE_CHOICES,
        blank=True,
        null=True,
        help_text="Tipo de uso do cliente (Pessoal, Profissional, Acadêmico)."
    )
    # created_at não é necessário aqui, pois a data de criação do cliente está em Clientes
    updated_at = models.DateTimeField(auto_now=True) # Ajustado para auto_now
    created_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by_fk', blank=True, null=True)
    updated_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='updated_by_fk', related_name='clientespf_updated_by_fk_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes_pf'
        verbose_name = 'Cliente Pessoa Física'
        verbose_name_plural = 'Clientes Pessoa Física'

    def __str__(self):
        return self.nome


class ClientesPj(models.Model):
    id_cliente_fk = models.OneToOneField('Clientes', models.DO_NOTHING, db_column='id_cliente_fk', primary_key=True)
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255, blank=True, null=True)
    cnpj = models.CharField(unique=True, max_length=18)
    email_empresa = models.CharField(unique=True, max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    id_area_atendimento_fk = models.ForeignKey(AreasAtendimento, models.DO_NOTHING, db_column='id_area_atendimento_fk', blank=True, null=True)
    id_faixa_faturamento_fk = models.ForeignKey('FaixasFaturamento', models.DO_NOTHING, db_column='id_faixa_faturamento_fk', blank=True, null=True)
    id_equipe_fk = models.ForeignKey('Equipes', models.DO_NOTHING, db_column='id_equipe_fk', blank=True, null=True)
    # created_at não é necessário aqui, pois a data de criação do cliente está em Clientes
    updated_at = models.DateTimeField(auto_now=True) # Ajustado para auto_now
    created_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by_fk', blank=True, null=True)
    updated_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='updated_by_fk', related_name='clientespj_updated_by_fk_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes_pj'
        verbose_name = 'Cliente Pessoa Jurídica'
        verbose_name_plural = 'Clientes Pessoa Jurídica'

    def __str__(self):
        return self.razao_social


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'

    def __str__(self):
        return f"Log {self.id} - {self.user.username if self.user else 'N/A'}"


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)

    def __str__(self):
        # Corrigido para usar os atributos corretos
        return f"{self.app_label}.{self.model}"


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

    def __str__(self):
        return f"Migração {self.app}.{self.name}"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

    def __str__(self):
        return self.session_key


class DoresCliente(models.Model):
    id_dor = models.AutoField(primary_key=True)
    descricao_dor = models.CharField(
        unique=True,
        max_length=255,
        choices=DORES_CLIENTE_CHOICES,
        help_text="Descrição da dor do cliente."
    )
    created_at = models.DateTimeField(auto_now_add=True) # Ajustado para auto_now_add
    updated_at = models.DateTimeField(auto_now=True)     # Ajustado para auto_now
    created_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by_fk', blank=True, null=True)
    updated_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='updated_by_fk', related_name='dorescliente_updated_by_fk_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dores_cliente'
        verbose_name = 'Dor do Cliente'
        verbose_name_plural = 'Dores do Cliente'

    def __str__(self):
        return self.get_descricao_dor_display()


class Equipes(models.Model):
    id_equipe = models.AutoField(primary_key=True)
    faixa_tamanho = models.CharField(
        unique=True,
        max_length=50,
        choices=EQUIPE_TAMANHO_CHOICES,
        help_text="Faixa de tamanho da equipe."
    )
    created_at = models.DateTimeField(auto_now_add=True) # Ajustado para auto_now_add
    updated_at = models.DateTimeField(auto_now=True)     # Ajustado para auto_now
    created_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by_fk', blank=True, null=True)
    updated_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='updated_by_fk', related_name='equipes_updated_by_fk_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipes'
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    def __str__(self):
        return self.get_faixa_tamanho_display()


class FaixasFaturamento(models.Model):
    id_faixa_faturamento = models.AutoField(primary_key=True)
    descricao_faixa = models.CharField(
        unique=True,
        max_length=100,
        # choices=FAIXA_FATURAMENTO_CHOICES, # Adicionado choices - Descomente se quiser usar choices para este campo
        help_text="Descrição da faixa de faturamento."
    )
    valor_minimo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    valor_maximo = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # Ajustado para auto_now_add
    updated_at = models.DateTimeField(auto_now=True)     # Ajustado para auto_now
    created_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by_fk', blank=True, null=True)
    updated_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='updated_by_fk', related_name='faixasfaturamento_updated_by_fk_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faixas_faturamento'
        verbose_name = 'Faixa de Faturamento'
        verbose_name_plural = 'Faixas de Faturamento'

    def __str__(self):
        # Se você descomentar 'choices=FAIXA_FATURAMENTO_CHOICES', use get_descricao_faixa_display()
        # Caso contrário, retorne a descrição_faixa diretamente
        return self.descricao_faixa


class GatewaysPagamento(models.Model):
    id_gateway = models.AutoField(primary_key=True)
    nome_gateway = models.CharField(unique=True, max_length=100)
    url_api = models.TextField(blank=True, null=True)
    credenciais_api = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # Ajustado para auto_now_add
    updated_at = models.DateTimeField(auto_now=True)     # Ajustado para auto_now
    created_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by_fk', blank=True, null=True)
    updated_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='updated_by_fk', related_name='gatewayspagamento_updated_by_fk_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gateways_pagamento'
        verbose_name = 'Gateway de Pagamento'
        verbose_name_plural = 'Gateways de Pagamento'

    def __str__(self):
        return self.nome_gateway


class Pagamento(models.Model):
    id_pagamento = models.AutoField(primary_key=True)
    id_assinatura_fk = models.ForeignKey(Assinatura, models.DO_NOTHING, db_column='id_assinatura_fk')
    status_pagamento = models.CharField(
        max_length=20,
        choices=STATUS_PAGAMENTO_CHOICES,
        help_text="Status do pagamento."
    )
    tipo_pagamento = models.CharField(
        max_length=20,
        choices=TIPO_PAGAMENTO_CHOICES,
        help_text="Tipo de pagamento (Cartão de Crédito, Pix, Boleto, etc.)."
    )
    data_pagamento = models.DateField()
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    id_gateway_fk = models.ForeignKey(GatewaysPagamento, models.DO_NOTHING, db_column='id_gateway_fk', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # Ajustado para auto_now_add
    updated_at = models.DateTimeField(auto_now=True)     # Ajustado para auto_now
    created_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by_fk', blank=True, null=True)
    updated_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='updated_by_fk', related_name='pagamento_updated_by_fk_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagamento'
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'

    def __str__(self):
        return f"Pagamento {self.id_pagamento} - Status: {self.get_status_pagamento_display()}"


class Perguntas(models.Model):
    id_pergunta = models.AutoField(primary_key=True)
    texto_pergunta = models.TextField()
    tipo_resposta = models.CharField(max_length=50)
    opcoes_selecao = models.TextField(blank=True, null=True)
    ativa = models.BooleanField(blank=True, null=True)
    ordem_exibicao = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # Ajustado para auto_now_add
    updated_at = models.DateTimeField(auto_now=True)     # Ajustado para auto_now
    created_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by_fk', blank=True, null=True)
    updated_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='updated_by_fk', related_name='perguntas_updated_by_fk_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perguntas'
        verbose_name = 'Pergunta'
        verbose_name_plural = 'Perguntas'

    def __str__(self):
        return self.texto_pergunta[:50] + "..." if len(self.texto_pergunta) > 50 else self.texto_pergunta


# Novo modelo para a tabela intermediária (PlanoServico)
class PlanoServico(models.Model):
    plano = models.ForeignKey('Planos', on_delete=models.CASCADE)
    servico = models.ForeignKey('Servicos', on_delete=models.CASCADE)
    # Adicionado campo para o limite de uso
    limite_uso = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Limite de uso para este serviço dentro do plano (ex: minutos, requisições)."
    )
    created_at = models.DateTimeField(auto_now_add=True) # Ajustado para auto_now_add
    updated_at = models.DateTimeField(auto_now=True)     # Ajustado para auto_now

    class Meta:
        db_table = 'plano_servicos' # Nome da tabela de junção existente
        unique_together = (('plano', 'servico'),) # Garante que a combinação seja única
        # managed = True por padrão, não precisa especificar

    def __str__(self):
        # Corrigido para usar os atributos corretos (plano e servico)
        return f"Plano: {self.plano.nome_plano if self.plano else 'N/A'} - Serviço: {self.servico.nome_servico if self.servico else 'N/A'}"


class Planos(models.Model):
    id_plano = models.AutoField(primary_key=True)
    # Usa o modelo intermediário explícito
    servicos = models.ManyToManyField(
        'Servicos',
        through='PlanoServico', # Indica o modelo intermediário
        related_name='planos_associados',
        help_text="Serviços incluídos neste plano."
    )

    nome_plano = models.CharField(unique=True, max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    preco_mensal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    duracao_meses = models.IntegerField(blank=True, null=True)
    codigo_plano = models.CharField(unique=True, max_length=50, blank=True, null=True)
    permite_cadastro_usuarios_pj = models.BooleanField(blank=True, null=True)
    # Adicionado campo para diferenciar planos gratuitos/pagos
    tipo_plano = models.CharField(
        max_length=20,
        choices=TIPO_PLANO_CHOICES,
        default='pago',
        help_text="Tipo de plano (Gratuito ou Pago)."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by_fk', blank=True, null=True)
    updated_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='updated_by_fk', related_name='planos_updated_by_fk_set', blank=True, null=True)

    class Meta:
        # REMOVIDO: managed = False para permitir que o Django gerencie o ManyToManyField
        db_table = 'planos'
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'

    def __str__(self):
        return self.nome_plano

class RespostasQuestionarioPf(models.Model):
    id_resposta_pf = models.AutoField(primary_key=True)
    id_cliente_fk = models.ForeignKey('ClientesPf', models.DO_NOTHING, db_column='id_cliente_fk')
    id_pergunta_fk = models.ForeignKey(Perguntas, models.DO_NOTHING, db_column='id_pergunta_fk')
    resposta = models.TextField(blank=True, null=True)
    data_resposta = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # Ajustado para auto_now_add
    updated_at = models.DateTimeField(auto_now=True)     # Ajustado para auto_now
    created_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by_fk', blank=True, null=True)
    updated_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='updated_by_fk', related_name='respostasquestionariopf_updated_by_fk_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'respostas_questionario_pf'
        unique_together = (('id_cliente_fk', 'id_pergunta_fk', 'data_resposta'),)
        verbose_name = 'Resposta Questionário PF'
        verbose_name_plural = 'Respostas Questionários PF'

    def __str__(self):
        return f"Resposta PF {self.id_resposta_pf} - Cliente: {self.id_cliente_fk.nome if self.id_cliente_fk else 'N/A'}"


class RespostasQuestionarioPj(models.Model):
    id_resposta_pj = models.AutoField(primary_key=True)
    id_cliente_fk = models.ForeignKey('ClientesPj', models.DO_NOTHING, db_column='id_cliente_fk')
    id_pergunta_fk = models.ForeignKey(Perguntas, models.DO_NOTHING, db_column='id_pergunta_fk')
    resposta = models.TextField(blank=True, null=True)
    data_resposta = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # Ajustado para auto_now_add
    updated_at = models.DateTimeField(auto_now=True)     # Ajustado para auto_now
    created_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by_fk', blank=True, null=True)
    updated_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='updated_by_fk', related_name='respostasquestionariopj_updated_by_fk_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'respostas_questionario_pj'
        unique_together = (('id_cliente_fk', 'id_pergunta_fk', 'data_resposta'),)
        verbose_name = 'Resposta Questionário PJ'
        verbose_name_plural = 'Respostas Questionários PJ'

    def __str__(self):
        return f"Resposta PJ {self.id_resposta_pj} - Cliente: {self.id_cliente_fk.razao_social if self.id_cliente_fk else 'N/A'}"


class Servicos(models.Model):
    id_servico = models.AutoField(primary_key=True)
    nome_servico = models.CharField(
        unique=True,
        max_length=100,
        # choices=SERVICOS_CHOICES, # Adicionado choices - Descomente se quiser usar choices para este campo
        help_text="Nome do serviço oferecido."
    )
    descricao = models.TextField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # Ajustado para auto_now_add
    updated_at = models.DateTimeField(auto_now=True)     # Ajustado para auto_now
    created_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by_fk', blank=True, null=True)
    updated_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='updated_by_fk', related_name='servicos_updated_by_fk_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicos'
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        # Se você descomentar 'choices=SERVICOS_CHOICES', use get_nome_servico_display()
        # Caso contrário, retorne nome_servico diretamente
        return self.nome_servico


class Transcricoes(models.Model):
    id_transcricao = models.AutoField(primary_key=True)
    id_assinatura_fk = models.ForeignKey(Assinatura, models.DO_NOTHING, db_column='id_assinatura_fk')
    duracao_segundos = models.IntegerField(blank=True, null=True)
    custo_minutos = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    data_transcricao = models.DateTimeField(blank=True, null=True)
    url_audio_original = models.TextField(blank=True, null=True)
    url_transcricao_texto = models.TextField(blank=True, null=True)
    id_servico_fk = models.ForeignKey(Servicos, models.DO_NOTHING, db_column='id_servico_fk')
    created_at = models.DateTimeField(auto_now_add=True) # Ajustado para auto_now_add
    updated_at = models.DateTimeField(auto_now=True)     # Ajustado para auto_now
    created_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by_fk', blank=True, null=True)
    updated_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='updated_by_fk', related_name='transcricoes_updated_by_fk_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transcricoes'
        verbose_name = 'Transcrição'
        verbose_name_plural = 'Transcrições'

    def __str__(self):
        return f"Transcrição {self.id_transcricao} - Assinatura: {self.id_assinatura_fk.id_assinatura if self.id_assinatura_fk else 'N/A'}"


class Usuarios(models.Model):
    id_user = models.AutoField(primary_key=True)
    id_cliente_fk = models.ForeignKey('Clientes', models.DO_NOTHING, db_column='id_cliente_fk', blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    senha_hash = models.CharField(max_length=255)
    nome = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    id_funcao_fk = models.CharField(
        max_length=20,
        choices=FUNCAO_USUARIO_CHOICES,
        blank=True,
        null=True,
        help_text="Função do usuário no sistema."
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_GENERICO_CHOICES,
        blank=True,
        null=True,
        help_text="Status do usuário (Ativo, Inativo, Pendente)."
    )
    created_at = models.DateTimeField(auto_now_add=True) # Ajustado para auto_now_add
    updated_at = models.DateTimeField(auto_now=True)     # Ajustado para auto_now
    created_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='created_by_fk', blank=True, null=True)
    updated_by_fk = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='updated_by_fk', related_name='usuarios_updated_by_fk_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome if self.nome else self.email

class Credential(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome da Credencial")
    # Use o campo que você acabou de criar
    value = EncryptedCharField(max_length=255, verbose_name="Valor")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Credencial"
        verbose_name_plural = "Credenciais"
        ordering = ['name']

    def __str__(self):
        return self.name