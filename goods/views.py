from django.shortcuts import render
from goods.models import *


def good(request, good_id):
    good = Goods.objects.get(id=good_id)
    return render(request, 'goods/good.html', locals())
