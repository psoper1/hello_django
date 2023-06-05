from django.urls import path
from hello import views
from .views import ChampListCreateView, ChampDetailAPIView, LaneListCreateView, LaneDetailAPIView

urlpatterns = [
    path("", views.home, name="home"),
    # path('champs/', ChampViewSet.as_view({'get': 'list'}), name='champ-list'),
    path('champs/', ChampListCreateView.as_view(), name='champ-list-create'),
    path('champs/<int:pk>/', ChampDetailAPIView.as_view(), name='champ-detail'),
    path('lanes/', LaneListCreateView.as_view(), name='lane-list-create'),
    path('lanes/<int:pk>/', LaneDetailAPIView.as_view(), name='lane-detail'),
    # Other URL patterns for your app...
]