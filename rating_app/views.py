from django.shortcuts import render
from django.http import Http404
from .models import Shop, ServiceFromEmployee, Service, Employee, Rating

def index(request):
    """The landing page of the app"""
    return render(request, 'rating_app/index.html')

def shops(request):
    """The page for creating and changing a shop"""
    shops = Shop.objects.order_by('name')
    context = {'shops': shops}
    return render(request, 'rating_app/shops.html', context)

def shop(request, shop_id):
    """Showing only on shop"""
    try:
        shop = Shop.objects.get(id=shop_id)
        employees = Employee.objects.filter(shopId=shop_id)
        context = {'shop': shop, 'employees': employees}
    except Shop.DoesNotExist:
        raise Http404("Geschäft existiert nicht.")
    return render(request, 'rating_app/shop.html', context)