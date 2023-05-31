from django.urls import path
from hello import views
from .views import ChampListCreateView, ChampDetailAPIView

urlpatterns = [
    path("", views.home, name="home"),
    # path('champs/', ChampViewSet.as_view({'get': 'list'}), name='champ-list'),
    path('champs/', ChampListCreateView.as_view(), name='champ-list-create'),
    path('champs/<int:pk>/', ChampDetailAPIView.as_view(), name='champ-detail'),
    # Other URL patterns for your app...
]