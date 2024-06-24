from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:item_id>/', views.detail, name='detail'),
    # path('add/', views.create_item, name='create_item'),
    # path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
    path('', views.IndexClassView.as_view(), name='index'),
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    path('add/', views.CreateItem.as_view(), name='create_item'),
    path('update/<int:pk>/', views.UpdateItem.as_view(), name='update_item'),
]
