from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from app.models import Article, Category, MessageBook
from web.forms import MessageForm


def index(request):
    if request.method == 'GET':
        cats = Category.objects.all()
        page = int(request.GET.get('page', 1))
        arts = Article.objects.all()
        pg = Paginator(arts, 10)
        arts = pg.page(page)
        name = request.session.get('user_id')
        if not name:
            name = False
        return render(request, 'index_web.html', {'arts': arts, 'cats': cats,
                                                  'name': name})


def share(request):
    return render(request, 'share_web.html')


def list1(request):
    if request.method == 'GET':
        cats = Category.objects.all()
        page = int(request.GET.get('page', 1))
        arts = Article.objects.all()
        pg = Paginator(arts, 10)
        arts = pg.page(page)
        return render(request, 'list_web.html', {'arts': arts, 'cats': cats})


def about(request):
    return render(request, 'about_web.html')


def gbook(request):
    if request.method == 'GET':
        user_id = 1
        messages = MessageBook.objects.filter(user_id=user_id).all()
        page = int(request.GET.get('page', 1))
        pg = Paginator(messages[::-1], 5)
        messages = pg.page(page)
        return render(request, 'gbook_web.html', {'messages': messages})
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['lytext']
            user_id = 1
            MessageBook.objects.create(name=name, email=email,
                                       content=content, user_id=user_id)
            return HttpResponseRedirect(reverse('web:index'))
        else:
            errors = form.errors
            user_id = 1
            messages = MessageBook.objects.filter(user_id=user_id).all()
            return render(request, 'gbook_web.html', {'errors': errors, 'messages': messages})


def info(request, id):
    if request.method == 'GET':
        art = Article.objects.filter(pk=id).first()
        cats = Category.objects.all()
    return render(request, 'info_web.html', {'art': art, 'cats': cats})


def infopic(request):
    return render(request, 'infopic_web.html')