from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q  # special object called Q to generate a search query
from .models import Product, Category

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:  # wether sort is in request.GET
            sortkey = request.GET['sort']  # if it is
            sort = sortkey
            if sortkey == 'name':  # whether sortkey is equal to name
                sortkey == 'lower_name'  # have renamed sortkey to lower_name. if it is will set it to lower_name which is the field will create with the annotation.
                products = products.annotate(lower_name=Lower('name'))  # now to actually do the annotation, we are using Lower function on the original name field here.
                
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':  # check whether it is descending
                    sortkey = f'-{sortkey}'  # have used minus using string formatting, which will reverse the order
            products = products.order_by(sortkey)  # to sort the products, we need to use the order by model method

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
