
from django.urls import path

from web import views

urlpatterns = [
    # 首页
    path('index/', views.index, name='index'),
    # path('share/', views.share, name='share'),
    path('list/', views.list1, name='list'),
    path('about/', views.about, name='about'),
    path('gbook/', views.gbook, name='gbook'),
    path('info/<int:id>', views.info, name='info'),
    path('infopic/', views.infopic, name='infopic'),
]
