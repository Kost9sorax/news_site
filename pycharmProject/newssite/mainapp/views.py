from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Articles
from .forms import ArticlesForm

@csrf_exempt
def index(request):
    news = Articles.objects.order_by('-date')
    context = {
        'news': news
    }
    return render(request, 'homepage/index.html', context)


def create(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img = form.instance
            return redirect("/", {'file': img})
        else:
            error = 'Форма заполнена некорректно'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'homepage/create.html', data)


def tag_list(request, tag):
    all_news_list = Articles.objects.all()
    return render(request, 'index.html', {'all_news_list': all_news_list, 'header': tag})