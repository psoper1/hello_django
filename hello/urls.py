from django.urls import path
from hello import views
from .views import ChampViewSet

urlpatterns = [
    path("", views.home, name="home"),
    path('champs/', ChampViewSet.as_view({'get': 'list'}), name='champ-list'),
    path('champs/<int:pk>/', ChampViewSet.as_view({'get': 'retrieve'}), name='champ-detail'),
    # Other URL patterns for your app...
]