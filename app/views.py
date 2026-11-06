from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def blog_details(request):
    return render(request, 'blog_details.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def elements(request):
    return render(request, 'elements.html')


def main(request):
    return render(request, 'main.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def pricing(request):
    return render(request, 'pricing.html')
