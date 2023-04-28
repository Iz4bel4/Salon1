from django.urls import path
from .views import AboutPage,BlogPage,BlogsinglePage,ContactPage,IndexPage,ServicesPage,WorkPage

urlpatterns = [
 path('', IndexPage,name='index'),
 path('about/', AboutPage,name='about'),
 path('blog/', BlogPage,name='blog'),
 path('blog-single/', BlogsinglePage,name='blog-single'),
 path('contact/', ContactPage,name='contact'),
 path('services/', ServicesPage,name='services'),
 path('work/', WorkPage,name='work'),
]