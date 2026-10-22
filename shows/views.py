from django.shortcuts import render


def shows_view(request):
    return render(request, 'shows/shows.html')


def showtime_view(request):
    return render(request, 'shows/showtime.html')
