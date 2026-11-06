
from django.urls import path
from app.views import (
    index,
    about,
    blog_details,
    blog,
    contact,
    elements,
    main,
    portfolio,
    pricing,
)

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog_details/', blog_details, name='blog_details'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('elements/', elements, name='elements'),
    path('main/', main, name='main'),
    path('portfolio/', portfolio, name='portfolio'),
    path('pricing/', pricing, name='pricing'),
]
