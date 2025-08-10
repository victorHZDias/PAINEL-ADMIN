# mysite.urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

# Importe o router do seu app
from meu_app.urls import router # <--- Importe o router aqui

admin.site.site_header = 'Administração Quality Excellence'
admin.site.site_title = "Área de Administração"
admin.site.index_title = "Bem-vindo ao Painel de Controle"

urlpatterns = [
    path('admin/', admin.site.urls), # Admin sempre primeiro

    # URLs para suas páginas HTML (home, sobre, profile etc.)
    # Isso significa que:
    # / -> home_view
    # /sobre/ -> sobre_view
    # /profile/ -> profile
    path('', include('meu_app.urls')),

    # URLs para sua API REST (todas as ViewSets)
    # Isso significa que:
    # /api/analise-ia/
    # /api/clientes/
    # etc.
    path('api/', include(router.urls)), # <--- Inclua o router aqui para sua API

    # Opcional: URL para o navegador da API do DRF e login/logout da API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Não inclua 'accounts/' novamente a menos que você tenha um motivo muito específico
    # path('accounts/', include('meu_app.urls')), # <--- Provavelmente remova esta linha para evitar duplicação
]

# Configuração de arquivos estáticos e de mídia para desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# APENAS PARA DEBUG=FALSE EM DESENVOLVIMENTO (NUNCA PRODUÇÃO)
else:
    urlpatterns += [
        path(settings.STATIC_URL[1:] + '<path:path>', serve, {'document_root': settings.STATIC_ROOT}),
        path(settings.MEDIA_URL[1:] + '<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    ]