from django.urls import path,include
from . import views
from .views import ChurchCreateView, ChurchDeleteView, ChurchDetailView, ChurchUpdateView
urlpatterns = [
    path('', views.home,name='home'),
    path('church/<int:pk>/', ChurchDetailView.as_view(), name='church-detail'),
    path('church/new/', ChurchCreateView.as_view(), name='church-create'),
    path('church/<int:pk>/update/', ChurchUpdateView.as_view(), name='church-update'),
    path('church/<int:pk>/delete/', ChurchDeleteView.as_view(), name='church-delete'),

]