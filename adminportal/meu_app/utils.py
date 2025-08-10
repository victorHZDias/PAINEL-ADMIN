# meu_app/utils.py
from meu_app.models import Credential # Ou 'from .models import Credential' se estiver no mesmo nível
from django.core.cache import cache
from django.conf import settings # Para usar settings.DEBUG ou outras configurações

def get_credential(name, default=None):
    """
    Busca uma credencial do banco de dados, usando cache para performance.
    """
    cache_key = f'credential_{name}'
    value = cache.get(cache_key)

    if value is None:
        try:
            credential = Credential.objects.get(name=name)
            value = credential.value
            # Cache a credencial por um tempo (ex: 1 hora = 3600 segundos)
            # O tempo de cache pode ser ajustado conforme a frequência de mudança das credenciais.
            cache.set(cache_key, value, 3600)
        except Credential.DoesNotExist:
            value = default
            if settings.DEBUG: # Apenas para depuração em desenvolvimento
                print(f"ATENÇÃO DEBUG: Credencial '{name}' não encontrada no banco de dados.")
            # Em produção, você pode querer logar um erro mais sério ou levantar uma exceção
            # se a credencial for crítica e não tiver um valor padrão.
        except Exception as e:
            # Capture outras exceções, como problemas de conexão com o DB ou criptografia
            if settings.DEBUG:
                print(f"ATENÇÃO DEBUG: Erro ao obter credencial '{name}' do DB: {e}")
            value = default
            # Em produção, considere levantar ImproperlyConfigured ou logar um erro crítico
            # from django.core.exceptions import ImproperlyConfigured
            # raise ImproperlyConfigured(f"Failed to load critical credential '{name}': {e}")
    return value