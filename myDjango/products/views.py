from django.shortcuts import render
from django.http import HttpResponse
from products.models import Products

# Create your views here.
def product_list_create(request):
    try :
        
        if request.method == 'POST':
            name = request.POST.get('name')
            description = request.POST.get('description')
            price = request.POST.get('price')
            stock = request.POST.get('stock')

            product = Products(name=name, description=description, price=price, stock=stock)
            product.save()

            return HttpResponse({'message': "success", 'data': product})
        else:
            return HttpResponse({'message': "fail", 'error': 'Invalid request method'})
    except Exception as e:
        return HttpResponse({'message': "fail", 'error': str(e)})