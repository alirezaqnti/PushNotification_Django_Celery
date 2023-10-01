from django.shortcuts import render


def notif_page(request):
    return render(request,'notif_page.html')