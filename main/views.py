from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306210203',
        'name': 'Muhammad Ghathaf Fariz Abiyyu',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)