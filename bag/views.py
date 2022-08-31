from django.shortcuts import render, redirect


def view_bag(request):
    '''
    A view to render the view bag page
    '''

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    '''
    A view to render quanity of a product in the bag page
    '''

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
