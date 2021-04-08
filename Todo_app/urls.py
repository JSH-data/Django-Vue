from django.urls import path
from . import views

app_name = 'Todo_app'

urlpatterns = [
    path('vonly/', views.TodoVueOnlyTV.as_view(), name='vonly'),
    path('create/', views.TodoCV.as_view(), name='create'),
    path('list/', views.TodoLV.as_view(), name='list'),
    path('<int:pk>/delete/', views.TodoDelV.as_view(), name='delete'), # <int:pk> path converter는 숫자를 인자로 받아서 view에 넘겨줍니다. 
    path('mixin/', views.TodoMOMCV.as_view(), name='mixin'),
    path('<int:pk>/delete2/', views.TodoDelv2.as_view(), name='delete2')
]
