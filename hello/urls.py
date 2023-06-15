from django.urls import path
from hello import views
from .views import ChampListCreateView, ChampDetailAPIView, LaneListCreateView, LaneDetailAPIView, get_riot_api_key

urlpatterns = [
    path("", views.home, name="home"),
    path('champs/', ChampListCreateView.as_view(), name='champ-list-create'),
    path('champs/<int:pk>/', ChampDetailAPIView.as_view(), name='champ-detail'),
    path('lanes/', LaneListCreateView.as_view(), name='lane-list-create'),
    path('lanes/<int:pk>/', LaneDetailAPIView.as_view(), name='lane-detail'),
    path('api/get_riot_api_key/', get_riot_api_key, name='get_riot_api_key'),
]