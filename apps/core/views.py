from django.shortcuts import render


def home_view(request):
    """
    Página inicial do AllePics.
    """
    return render(request, 'core/home.html')