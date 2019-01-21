
from django.urls import path, include

from user import views

urlpatterns = [
    # 后台管理首页
    # path('index/', views.index, name='index'),
    # 登录注册
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    # 文章、栏目操作相关
    # path('article/', views.article, name='article'),
    # path('category/', views.category, name='category'),
    # # path('add_article/', views.add_article, name='add_article'),
    # path('add_category/', views.add_category, name='add_category'),
    #
    # # 文章增删改
    # path('add_article/', views.add_article, name='add_article'),
    # path('up_article/', views.up_article, name='up_article'),
    # path('del_article/', views.del_article, name='del_article'),

]