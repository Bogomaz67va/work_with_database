from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_list = list()
    sort = request.GET.get('sort')
    if sort == 'name':
        phone = Phone.objects.all().order_by(str(sort))
    elif sort == 'min_price':
        phone = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phone = Phone.objects.all().order_by('-price')
    else:
        phone = Phone.objects.all()
    for item in phone:
        phone_list.append(item)
    context = {'phones': phone_list}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
