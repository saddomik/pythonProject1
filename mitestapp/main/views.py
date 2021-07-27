from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm


def index(request):
    news = News.objects.all()

    return render(request, 'main/main.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        data = NewsForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('index')
        else:
            error = 'Ошибка'

    form = NewsForm()
    data = {'form': form}
    return render(request, 'main/create.html', data)
