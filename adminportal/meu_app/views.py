from django.shortcuts import render
from django.http import HttpResponse # Para a view tradicional
from rest_framework import viewsets # Para as views de API
from .serializers import PlanosSerializer,TranscribeRequestSerializer # Para as views de API
from .models import Planos # Para as views de API
from django.contrib.auth.decorators import login_required # Importe isso!
from rest_framework.permissions import IsAuthenticated # Importe esta linha!
from .minio_client import upload_audio_to_minio, get_minio_client # Importe as funções do MinIO
from rest_framework import status
from django.conf import settings
import requests
import time
import os
import io # Para lidar com arquivos em memória
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import get_credential # Importa a função de utilidades para obter credenciais

from .serializers import (
    AnaliseIaSerializer, AreasAtendimentoSerializer, AssinaturaSerializer, ClientesSerializer,
    ClientesPfSerializer, ClientesPjSerializer, DoresClienteSerializer, EquipesSerializer,
    FaixasFaturamentoSerializer, GatewaysPagamentoSerializer, PagamentoSerializer,
    PerguntasSerializer, PlanosSerializer, RespostasQuestionarioPfSerializer,
    RespostasQuestionarioPjSerializer, ServicosSerializer, TranscricoesSerializer, UsuariosSerializer
)
from .models import (
    AnaliseIa, AreasAtendimento, Assinatura, Clientes, ClientesPf, ClientesPj,
    DoresCliente, Equipes, FaixasFaturamento, GatewaysPagamento, Pagamento,
    Perguntas, Planos, RespostasQuestionarioPf, RespostasQuestionarioPj,
    Servicos, Transcricoes, Usuarios
)


def home_view(request):
    return render(request, 'meu_app/home.html') # <--- Mude para 'meu_app/home.html'

def sobre_view(request):
    return render(request, 'meu_app/sobre.html') 

class AnaliseIaViewSet(viewsets.ModelViewSet):
    queryset = AnaliseIa.objects.all()
    serializer_class = AnaliseIaSerializer
    permission_classes = [IsAuthenticated]

class AreasAtendimentoViewSet(viewsets.ModelViewSet):
    queryset = AreasAtendimento.objects.all()
    serializer_class = AreasAtendimentoSerializer
    permission_classes = [IsAuthenticated]

class AssinaturaViewSet(viewsets.ModelViewSet):
    queryset = Assinatura.objects.all()
    serializer_class = AssinaturaSerializer
    permission_classes = [IsAuthenticated]

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    permission_classes = [IsAuthenticated]

class ClientesPfViewSet(viewsets.ModelViewSet):
    queryset = ClientesPf.objects.all()
    serializer_class = ClientesPfSerializer
    permission_classes = [IsAuthenticated]

class ClientesPjViewSet(viewsets.ModelViewSet):
    queryset = ClientesPj.objects.all()
    serializer_class = ClientesPjSerializer
    permission_classes = [IsAuthenticated]

class DoresClienteViewSet(viewsets.ModelViewSet):
    queryset = DoresCliente.objects.all()
    serializer_class = DoresClienteSerializer
    permission_classes = [IsAuthenticated]

class EquipesViewSet(viewsets.ModelViewSet):
    queryset = Equipes.objects.all()
    serializer_class = EquipesSerializer
    permission_classes = [IsAuthenticated]

class FaixasFaturamentoViewSet(viewsets.ModelViewSet):
    queryset = FaixasFaturamento.objects.all()
    serializer_class = FaixasFaturamentoSerializer
    permission_classes = [IsAuthenticated]

class GatewaysPagamentoViewSet(viewsets.ModelViewSet):
    queryset = GatewaysPagamento.objects.all()
    serializer_class = GatewaysPagamentoSerializer
    permission_classes = [IsAuthenticated]

class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
    permission_classes = [IsAuthenticated]

class PerguntasViewSet(viewsets.ModelViewSet):
    queryset = Perguntas.objects.all()
    serializer_class = PerguntasSerializer
    permission_classes = [IsAuthenticated]

class PlanosViewSet(viewsets.ModelViewSet):
    queryset = Planos.objects.all()
    serializer_class = PlanosSerializer
    permission_classes = [IsAuthenticated]

class RespostasQuestionarioPfViewSet(viewsets.ModelViewSet):
    queryset = RespostasQuestionarioPf.objects.all()
    serializer_class = RespostasQuestionarioPfSerializer
    permission_classes = [IsAuthenticated]

class RespostasQuestionarioPjViewSet(viewsets.ModelViewSet):
    queryset = RespostasQuestionarioPj.objects.all()
    serializer_class = RespostasQuestionarioPjSerializer
    permission_classes = [IsAuthenticated]

class ServicosViewSet(viewsets.ModelViewSet):
    queryset = Servicos.objects.all()
    serializer_class = ServicosSerializer
    permission_classes = [IsAuthenticated]

class TranscricoesViewSet(viewsets.ModelViewSet):
    queryset = Transcricoes.objects.all()
    serializer_class = TranscricoesSerializer
    permission_classes = [IsAuthenticated]

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = [IsAuthenticated]

    
# NOVA VIEW: profile
@login_required # Garante que apenas usuários logados possam acessar
def profile(request):
    # Aqui você pode passar dados do usuário para o template, se estiver usando um
    context = {
        'user': request.user, # O objeto request.user contém informações do usuário logado
        'message': 'Bem-vindo ao seu perfil!'
    }
    # Se você usar um template, crie o arquivo HTML em templates/meu_app/profile.html
    # return render(request, 'meu_app/profile.html', context)

    # Por enquanto, para testar rapidamente, apenas retorne um HttpResponse
    return HttpResponse(f"<h1>Bem-vindo ao seu perfil, {request.user.username}!</h1><p>Esta é sua página de perfil.</p>")

# Suas funções de transcrição da AssemblyAI, adaptadas para usar a chave do settings
def submit_transcription_job(audio_url):
    """Submete um job de transcrição para a AssemblyAI com uma URL de áudio."""
    endpoint = "https://api.assemblyai.com/v2/transcript"
    assemblyai_api_key = get_credential("ASSEMBLYAI_API_KEY")
    if not assemblyai_api_key:
        # Em produção, você pode querer um tratamento de erro mais robusto aqui
        raise ValueError("Chave da API AssemblyAI não encontrada ou não configurada no banco de dados.")

    headers = {"Authorization": assemblyai_api_key}
    payload = {
        "audio_url": audio_url,
        "language_code": "pt", # Português
        "speaker_labels": True,
        "speakers_expected": 2, # Assumindo 2 falantes para labels
        "format_text": True
    }
    try:
        response = requests.post(endpoint, headers=headers, json=payload)
        response.raise_for_status() # Lança exceção para erros HTTP
        return response.json()["id"]
    except requests.exceptions.RequestException as e:
        print(f"Erro ao submeter job AssemblyAI: {e}")
        raise # Relança o erro para ser capturado pela view da API

def get_transcription_result(transcript_id):
    """Busca o resultado de uma transcrição da AssemblyAI."""
    endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
    
    assemblyai_api_key = get_credential("ASSEMBLYAI_API_KEY")
    if not assemblyai_api_key:
        # Em produção, você pode querer um tratamento de erro mais robusto aqui
        raise ValueError("Chave da API AssemblyAI não encontrada ou não configurada no banco de dados.")

    headers = {"Authorization": assemblyai_api_key}
    # Em uma API, você geralmente não faz um loop síncrono esperando.
    # Em vez disso, você submeteria e o frontend faria polling, ou usaria webhooks.
    # Para simplicidade de teste inicial, vamos fazer um polling limitado.
    # Em produção, considere um sistema de filas (Celery) para jobs de longa duração.
    max_attempts = 30 # Tentar por 30 * 3 segundos = 90 segundos
    attempts = 0
    while attempts < max_attempts:
        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
            data = response.json()
            if data["status"] == "completed":
                return data
            elif data["status"] == "failed":
                raise Exception("Falha na transcrição pela AssemblyAI.")
            elif data["status"] == "error": # Adicionado tratamento para status 'error'
                raise Exception(f"Erro na transcrição AssemblyAI: {data.get('error')}")

            time.sleep(3)
            attempts += 1
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar transcrição AssemblyAI: {e}")
            raise # Relança o erro
    raise Exception("Tempo limite excedido para buscar transcrição.")


class TranscribeAudioAPIView(APIView):
    """
    API para transcrever áudios.
    Recebe 'audio_url' ou 'audio_file'.
    Armazena 'audio_file' no MinIO e usa sua URL para transcrição.
    """
    def post(self, request, *args, **kwargs):
        serializer = TranscribeRequestSerializer(data=request.data)
        if serializer.is_valid():
            audio_url = serializer.validated_data.get('audio_url')
            audio_file = serializer.validated_data.get('audio_file')

            if audio_file:
                # Gerar um nome de arquivo único para o MinIO
                from uuid import uuid4
                file_ext = os.path.splitext(audio_file.name)[1]
                unique_filename = f"{uuid4()}{file_ext}"

                # Ler o conteúdo do arquivo para um BytesIO
                file_content = io.BytesIO(audio_file.read())

                # Fazer upload para o MinIO
                minio_audio_url = upload_audio_to_minio(
                    file_content,
                    unique_filename,
                    content_type=audio_file.content_type # Usar o tipo de conteúdo do arquivo enviado
                )

                if not minio_audio_url:
                    return Response({"error": "Falha ao fazer upload do arquivo para o MinIO."},
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                audio_url = minio_audio_url
            elif not audio_url:
                return Response({"error": "Nenhum áudio fornecido para transcrição."},
                                status=status.HTTP_400_BAD_REQUEST)

            try:
                # 1. Submeter o job de transcrição
                transcript_id = submit_transcription_job(audio_url)

                # 2. (Opcional) Guardar o transcript_id e a URL do áudio no seu banco de dados
                # Se você tiver um modelo 'Transcricoes' para isso
                # from .models import Transcricao
                # Transcricao.objects.create(
                #     audio_url=audio_url,
                #     transcript_id=transcript_id,
                #     status='processing'
                # )

                # 3. Buscar o resultado (para teste inicial)
                # Em produção, você faria um polling no frontend ou usaria webhooks.
                transcription_data = get_transcription_result(transcript_id)

                if transcription_data:
                    return Response({
                        "transcript_id": transcript_id,
                        "audio_url_minio": audio_url, # URL do áudio no MinIO (presigned)
                        "transcription_status": transcription_data["status"],
                        "text": transcription_data["text"],
                        "words": transcription_data["words"],
                        "segments": transcription_data.get("words_json", {}).get("segments"), # Ou de outro campo
                        "speaker_labels": transcription_data.get("utterances") # Se speaker_labels estiver True
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Falha ao obter o resultado da transcrição."},
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Para testes com microfone, você precisaria de um frontend que capture o áudio
    # e o envie como um "audio_file" (blob) para esta API.