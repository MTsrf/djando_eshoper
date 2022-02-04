from itertools import product
from multiprocessing.pool import ThreadPool
from django.shortcuts import render
from . models import TrendyProducts



def index(request):
    product = TrendyProducts.objects.all()

    return render(request,'index.html',{'trpds':product})
# Create your views here.
