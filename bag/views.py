from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))  # need to convert it into integer,since it will come from the template as a string.
    redirect_url = request.POST.get('redirect_url')  # redirect_url is to the redirect once the process is finished
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    # print(request.session['bag'])
    return redirect(redirect_url)
