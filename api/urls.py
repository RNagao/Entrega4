from django.urls import path
from api.views import PostagemList, PostagemDetail, PontuacaoList, PontuacaoDetail, UsuarioList, UsuarioDetail, ComentarioList, ComentarioDetail, CurtidaList, CurtidaDetail, LoginView


urlpatterns = [
    path('usuario/', UsuarioList.as_view()),
    path('usuario/<int:pk>', UsuarioDetail.as_view()),
    path('postagem/', PostagemList.as_view()),
    path('usuario/postagem/<int:pk>', PostagemDetail.as_view()),
    path('pontuacao/', PontuacaoList.as_view()),
    path('usuario/pontuacao/<int:pk>', PontuacaoDetail.as_view()),
    path('comentario/', ComentarioList.as_view()),
    path('postagem/comentario/<int:pk>', ComentarioDetail.as_view()),
    path('curtida/', CurtidaList.as_view()),
    path('postagem/curtida/<int:pk>', CurtidaDetail.as_view()),
    path('login/', LoginView.as_view())
]
