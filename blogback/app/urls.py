from django.urls import path, include

from app import views

urlpatterns = [
    # 后台首页(报告)
    path('index/', views.index, name='index'),
    # 文章、栏目
    path('article/', views.article, name='article'),
    path('category/', views.category, name='category'),


    # 文章增删改
    path('add_article/', views.add_article, name='add_article'),
    path('up_article/<int:id>/', views.up_article, name='up_article'),
    path('del_article/<int:id>/', views.del_article, name='del_article'),

    # 栏目增删改
    # path('add_category/', views.add_category, name='add_category'),
    path('up_category/<int:id>/', views.up_category, name='up_category'),
    path('del_category/<int:id>/', views.del_category, name='del_category'),
    # 留言相关操作
    path('message/', views.message, name='message'),
    path('del_message/<int:id>/', views.del_message, name='del_message'),
    path('read/<int:id>/', views.read, name='read'),

]