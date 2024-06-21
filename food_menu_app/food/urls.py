from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
#     path('menu/', views.menu, name='menu'),
#     path('menu/<int:food_id>/', views.detail, name='detail'),
#     path('menu/<int:food_id>/results/', views.results, name='results'),
#     path('menu/<int:food_id>/vote/', views.vote, name='vote'),
]
