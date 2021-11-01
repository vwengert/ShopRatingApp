from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Shop, Rating
from .forms import ShopForm, RatingForm

def index(request):
    """The landing page of the app"""
    return render(request, 'rating_app/index.html')

@login_required
def shops(request):
    """The page for creating and changing a shop"""
    shops = Shop.objects.filter(owner=request.user).order_by('name')
    context = {'shops': shops}
    return render(request, 'rating_app/shops.html', context)

@login_required
def shop(request, shop_id):
    """Showing only on shop"""
    try:
        shop = Shop.objects.get(id=shop_id)
        if shop.owner != request.user:
            raise Http404("Geschäft existiert nicht.")
        ratings = Rating.objects.select_related().filter(shop = shop_id)
        context = {'shop': shop, 'ratings': ratings}
    except Shop.DoesNotExist:
        raise Http404("Geschäft existiert nicht.")
    return render(request, 'rating_app/shop.html', context)

@login_required
def new_shop(request):
    """Add a new Shop to the database"""
    if request.method != 'POST':
        form = ShopForm()
    else:
        form = ShopForm(data=request.POST)
        if form.is_valid():
            newShop = form.save(commit=False)
            newShop.owner = request.user
            newShop.save()
            return redirect('rating_app:shops')

    context = {'form': form}
    return render(request, 'rating_app/new_shop.html', context)

@login_required
def new_rating(request, shop_id):
    """Add a new rating for a particular shop"""
    shop = Shop.objects.get(id=shop_id)
    if shop.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = RatingForm()
    else:
        form = RatingForm(data=request.POST)
        if form.is_valid():
            newRating = form.save(commit=False)
            newRating.shop = shop
            newRating.save()
            return redirect('rating_app:shop', shop_id=shop_id)
    context = {'shop': shop, 'form': form}
    return render(request, 'rating_app/new_rating.html', context)

@login_required
def edit_rating(request, rating_id):
    """Edit an existing rating."""
    rating = Rating.objects.get(id=rating_id)
    shop = rating.shop
    if shop.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = RatingForm(instance=rating)
    else:
        form = RatingForm(instance=rating, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('rating_app:shop', shop_id=shop.id)
    context = {'rating': rating, 'shop': shop, 'form': form}
    return render(request, 'rating_app/edit_rating.html', context)