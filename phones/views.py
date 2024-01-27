from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    sort_filter = {
        "name": ["name", True],
        "min_price": ["price", False],
        "max_price": ["price", True],
    }

    phones = [{
        "name": i.name,
        "image": i.image,
        "price": i.price,
        "release_date": i.release_date,
        "lte_exists": i.lte_exists,
        "slug": i.slug
    } for i in Phone.objects.all()
    ]

    sort_option = request.GET.get("sort", None)
    if sort_option:
        phones.sort(key=lambda x: x[sort_filter[sort_option][0]], reverse=sort_filter[sort_option][1])

    context = {"phones": phones, }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    for i in Phone.objects.filter(slug=slug):
        phone = {
            'name': i.name,
            'price': i.price,
            'image': i.image,
            'release_date': i.release_date,
            'lte_exists': i.lte_exists,
            'slug': i.slug
        }
        break

    context = {'phone': phone, }
    return render(request, template, context)
