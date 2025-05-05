from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Min
from .models import Product, Store, Favorite
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect

def home(request):
    search_query = request.GET.get('search', '')
    store_id = request.GET.get('store')
    sort_by = request.GET.get('sort')
    
    # Only show products if there's a search query
    products = Product.objects.none()  # Empty queryset by default
    stores = Store.objects.all()
    product_prices = {}
    
    if search_query:
        products = Product.objects.all()
        if search_query:
            products = products.filter(name__icontains=search_query)
        
        if store_id:
            products = products.filter(store_id=store_id)
        
        if sort_by == 'price_asc':
            products = products.order_by('price')
        elif sort_by == 'price_desc':
            products = products.order_by('-price')
        
        # Get the cheapest price for each product
        for product in products:
            if product.name not in product_prices:
                product_prices[product.name] = Product.objects.filter(name=product.name).aggregate(min_price=Min('price'))['min_price']
    
    context = {
        'products': products,
        'stores': stores,
        'product_prices': product_prices,
        'search_query': search_query,
        'show_location_modal': request.user.is_authenticated and not request.session.get('location')
    }
    return render(request, 'grocery/home.html', context)

def save_location(request):
    if request.method == 'POST' and request.user.is_authenticated:
        location = request.POST.get('location')
        request.session['location'] = location
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'grocery/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'grocery/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'grocery/favorites.html', {'favorites': favorites})

@login_required
@require_POST
@csrf_protect
def toggle_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)
    
    if not created:
        favorite.delete()
        return JsonResponse({'status': 'removed'})
    return JsonResponse({'status': 'added'})

def filter_products(request):
    store_id = request.GET.get('store')
    sort_by = request.GET.get('sort')
    search_query = request.GET.get('search', '')
    
    products = Product.objects.all()
    
    if search_query:
        products = products.filter(name__icontains=search_query)
    
    if store_id:
        products = products.filter(store_id=store_id)
    
    if sort_by == 'price_asc':
        products = products.order_by('price')
    elif sort_by == 'price_desc':
        products = products.order_by('-price')
    
    # Get the cheapest price for each product
    product_prices = {}
    for product in products:
        if product.name not in product_prices:
            product_prices[product.name] = Product.objects.filter(name=product.name).aggregate(min_price=Min('price'))['min_price']
    
    context = {
        'products': products,
        'product_prices': product_prices,
    }
    return render(request, 'grocery/product_list.html', context)
