from django.shortcuts import render


def shows_view(request):
    return render(request, 'shows.html')
