from django.shortcuts import render

def handler404(request, exception):
    return render(request, 'trackerapp/errors/404.html', status=404)
