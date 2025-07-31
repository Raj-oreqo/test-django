from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from products.models import Products

def home(request):
    # template = loader.get_template('home.html')
    # return HttpResponse(template.render())
    # return HttpResponse("Hello, world! This is the home page.") 
    productList = Products.objects.all()
    context = {'productList': productList, 
               'fruits': ['Apple', 'Banana', 'Cherry'],   
            }
    return render(request, 'home.html', context)    
    
