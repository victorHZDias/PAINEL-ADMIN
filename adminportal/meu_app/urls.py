from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views # Importa todas as views do seu views.py

# Crie um router e registre nossas viewsets com ele.
router = DefaultRouter()
router.register(r'analise-ia', views.AnaliseIaViewSet)
router.register(r'areas-atendimento', views.AreasAtendimentoViewSet)
router.register(r'assinaturas', views.AssinaturaViewSet)
router.register(r'clientes', views.ClientesViewSet)
router.register(r'clientes-pf', views.ClientesPfViewSet)
router.register(r'clientes-pj', views.ClientesPjViewSet)
router.register(r'dores-cliente', views.DoresClienteViewSet)
router.register(r'equipes', views.EquipesViewSet)
router.register(r'faixas-faturamento', views.FaixasFaturamentoViewSet)
router.register(r'gateways-pagamento', views.GatewaysPagamentoViewSet)
router.register(r'pagamentos', views.PagamentoViewSet)
router.register(r'perguntas', views.PerguntasViewSet)
router.register(r'planos', views.PlanosViewSet) # Já existia, mas aqui para consistência
router.register(r'respostas-questionario-pf', views.RespostasQuestionarioPfViewSet)
router.register(r'respostas-questionario-pj', views.RespostasQuestionarioPjViewSet)
router.register(r'servicos', views.ServicosViewSet)
router.register(r'transcricoes', views.TranscricoesViewSet)
router.register(r'usuarios', views.UsuariosViewSet)

urlpatterns = [
    path('', views.home_view, name='home'), # Acessível em /
    path('sobre/', views.sobre_view, name='sobre'), # Acessível em /sobre/
    path('profile/', views.profile, name='profile'), # Acessível em /profile/
    path('transcribe/', views.TranscribeAudioAPIView.as_view(), name='transcribe_audio'),

]