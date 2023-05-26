from django.shortcuts import render, redirect
from .models import *



# Create your views here.
    #shortdescription = ShortAboutUs.objects.first()
    #return render(request,'base.html', {'shortdescription': shortdescription})
def AboutPage(request):
    description = Aboutus.objects.first()
    return render(request,'about.html', {'description': description})

def BlogPage(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
     }

    return render(request, 'blog.html', context)

def BlogsinglePage(request):
    return render(request,'blog-single.html')

def ContactPage(request):
    return render(request,'contact.html')

def IndexPage(request):
    return render(request,'index.html')

def ServicesPage(request):
    treatment_offers = Offer.objects.filter(type=OfferType.Treatment)
    makeup_offers = Offer.objects.filter(type=OfferType.Make_up)
    manicure_offers = Offer.objects.filter(type=OfferType.Manicure)
    return render(request,'services.html', {'treatment_offers': treatment_offers, 'makeup_offers': makeup_offers, 'manicure_offers': manicure_offers})

def WorkPage(request):
    pictures = WorkPictures.objects.all
    return render(request,'work.html', {'pictures': pictures})

