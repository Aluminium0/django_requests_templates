from django.shortcuts import get_object_or_404, render

from .models import Phone


SORTING = {
    'name': 'name',
    'min_price': 'price',
    'max_price': '-price',
}


def catalog_view(request):
    sort = request.GET.get('sort')
    ordering = SORTING.get(sort, 'id')
    phones = Phone.objects.all().order_by(ordering)
    context = {
        'phones': phones,
    }
    return render(request, 'phones/catalog.html', context)


def phone_detail_view(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        'phone': phone,
    }
    return render(request, 'phones/phone.html', context)
