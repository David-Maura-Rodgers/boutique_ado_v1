from django.shortcuts import render


def index(request):
    '''
    A view to return the index page
    '''

    return render(request, 'home/index.html')


# /workspace/boutique_ado_v1/home/templates/index.html
