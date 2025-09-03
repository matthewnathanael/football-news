from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406496265',
        'name': 'Matthew Nathanael Sendiko',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)