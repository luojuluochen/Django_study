from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def polls_welcome_page2(request):
    return HttpResponse("Hello, world. You're at the polls index.")