from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render


from django.urls import reverse

from app.models import Article, Category, MessageBook


def index(request):
    act1 = True
    if request.method == 'GET':
        arts = Article.objects.all()
        count = len(arts)
        user_id = request.session.get('user_id')
        is_read_messages = MessageBook.objects.filter(user_id=user_id, is_read=0).all()
        message = MessageBook.objects.filter(user_id=user_id).all()
        message_num = len(is_read_messages)
        messages_num = len(message)
        return render(request, 'index.html', {'count': count, 'message_num': message_num,
                                              'messages_num': messages_num, 'act1': act1})


# 栏目
# def category(request):
#     if request.method == 'GET':
#         return render(request, 'category.html')


# 添加栏目
def category(request):
    act2 = True
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        cats = Category.objects.all()
        count = len(cats)
        is_read_messages = MessageBook.objects.filter(user_id=user_id, is_read=0).all()
        message_num = len(is_read_messages)
        return render(request, 'category.html', {'cats': cats, 'count': count,
                                                 'message_num': message_num, 'act2': act2})
    if request.method == 'POST':
        c_name = request.POST.get('name')
        alias = request.POST.get('alias')
        p_node = request.POST.get('fid')
        c_keyword = request.POST.get('keywords')
        c_desc = request.POST.get('describe')
        Category.objects.create(c_name=c_name,
                                alias=alias,
                                p_node=p_node,
                                c_keyword=c_keyword,
                                c_desc=c_desc)
        return HttpResponseRedirect(reverse('app:category'))


# 栏目
def up_category(request, id):
    act2 = True
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        cat = Category.objects.filter(pk=id).first()
        is_read_messages = MessageBook.objects.filter(user_id=user_id, is_read=0).all()
        message_num = len(is_read_messages)
        return render(request, 'update_category.html', {'cat': cat, 'message_num': message_num,
                                                        'act2': act2})
    if request.method == 'POST':
        c_name = request.POST.get('name')
        alias = request.POST.get('alias')
        p_node = request.POST.get('fid')
        c_keyword = request.POST.get('keywords')
        c_desc = request.POST.get('describe')
        Category.objects.create(c_name=c_name,
                                alias=alias,
                                p_node=p_node,
                                c_keyword=c_keyword,
                                c_desc=c_desc)
        return HttpResponseRedirect(reverse('app:category'))


# 删除栏目
def del_category(request, id):
    if request.method == 'GET':
        Category.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('app:category'))


# 文章
def article(request):
    act3 = True
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        page = int(request.GET.get('page', 1))
        arts = Article.objects.all()
        count = len(arts)
        pg = Paginator(arts, 10)
        arts = pg.page(page)
        is_read_messages = MessageBook.objects.filter(user_id=user_id, is_read=0).all()
        message_num = len(is_read_messages)
        return render(request, 'article.html', {'arts': arts, 'count': count,
                                                'message_num': message_num, 'act3': act3})


# 添加文章
def add_article(request):
    act3 = True
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        cats = Category.objects.all()
        is_read_messages = MessageBook.objects.filter(user_id=user_id, is_read=0).all()
        message_num = len(is_read_messages)
        return render(request, 'add_article.html', {'cats': cats, 'message_num': message_num,
                                                    'act3': act3})
    if request.method == 'POST':
        title = request.POST.get('title')
        icon = request.FILES.get('titlepic')
        content = request.POST.get('content')
        cate = request.POST.get('category')
        a_keyword = request.POST.get('keywords')
        tag = request.POST.get('tags')
        a_desc = request.POST.get('describe')
        Article.objects.create(title=title,
                               icon=icon,
                               content=content,
                               cate_id=cate,
                               a_keyword=a_keyword,
                               tag=tag,
                               a_desc=a_desc)
        return HttpResponseRedirect(reverse('app:article'))


def up_article(request, id):
    act3 = True
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        art = Article.objects.filter(pk=id).first()
        cats = Category.objects.all()
        is_read_messages = MessageBook.objects.filter(user_id=user_id, is_read=0).all()
        message_num = len(is_read_messages)
        return render(request, 'update_article.html', {'art': art, 'cats': cats,
                                                       'message_num': message_num, 'act3': act3})
    if request.method == 'POST':
        art = Article.objects.filter(pk=id).first()
        art.title = request.POST.get('title')
        art.icon = request.FILES.get('titlepic')
        art.content = request.POST.get('content')
        art.cate = request.POST.get('category')
        art.a_keyword = request.POST.get('keywords')
        art.tag = request.POST.get('tags')
        art.a_desc = request.POST.get('describe')
        art.is_open = request.POST.get('visibility')
        art.save()
        return HttpResponseRedirect(reverse('app:article'))


def del_article(request, id):
    if request.method == 'GET':
        Article.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('app:article'))


# 留言
def message(request):
    act4 = True
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        page = int(request.GET.get('page', 1))
        messages = MessageBook.objects.filter(user_id=user_id).all()
        is_read_messages = MessageBook.objects.filter(user_id=user_id, is_read=0).all()
        count = len(messages)
        message_num = len(is_read_messages)
        pg = Paginator(messages, 10)
        messages = pg.page(page)
        return render(request, 'message_book.html', {'messages': messages, 'count': count,
                                                     'message_num': message_num, 'act4': act4})


def del_message(request, id):
    if request.method == 'GET':
        MessageBook.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('app:message'))


def read(request, id):
    if request.method == 'GET':
        message = MessageBook.objects.filter(pk=id).first()
        message.is_read = 1
        message.save()
        return HttpResponseRedirect(reverse('app:message'))

