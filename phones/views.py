from django.shortcuts import render, redirect

from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    
    sort = request.GET.get('sort')
    sort_value = Phone.objects.all()
    
    if sort == 'name': 
        sort_value = Phone.objects.order_by('name')
        
    if sort == 'min_price': 
        sort_value = Phone.objects.order_by('prise')
        
    if sort == 'max_price': 
        sort_value = Phone.objects.order_by('-prise')
    
    context = {
        'phones': sort_value
    }
    
    print(context)

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    
    filter_phone = Phone.objects.get(slug=slug)

    print(filter_phone)

    context = {
        'phone': filter_phone
    }
    return render(request, template, context)
