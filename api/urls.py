from django.urls import path
from api.views import PostagemList, PostagemDetail, PontuacaoList, PontuacaoDetail, UserCreate, LoginView

urlpatterns = [
    path('postagem/', PostagemList.as_view()),
    path('postagem/<int:pk>', PostagemDetail.as_view()),
    path('users/pontuacao/', PontuacaoList.as_view()),
    path('users/pontuacao/<int:pk>', PontuacaoDetail.as_view()),
    path('users/', UserCreate.as_view()),
    path('login/', LoginView.as_view())
]
