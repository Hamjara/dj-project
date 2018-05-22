from django.shortcuts import render
from goods.models import Goods

# Create your views here.
def home(request):
    goods = Goods.objects.filter(is_active=True)
    return render(request, 'main/home.html', locals())