from django.urls import path
from .views import AboutPage,BlogPage,BlogsinglePage,ContactPage,IndexPage,ServicesPage,WorkPage, ConfirmationPage 
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
 path('', IndexPage,name='index'),
 path('about/', AboutPage,name='about'),
 path('blog/<int:pk>/', BlogsinglePage, name='blog_single'),
 path('blog/', BlogPage,name='blog'),
 path('contact/', ContactPage,name='contact'),
 path('services/', ServicesPage,name='services'),
 path('work/', WorkPage,name='work'),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)