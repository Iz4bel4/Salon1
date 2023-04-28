from django.shortcuts import render, redirect


# Create your views here.

def AboutPage(request):
    return render(request,'about.html')

def BlogPage(request):
    return render(request,'blog.html')

def BlogsinglePage(request):
    return render(request,'blog-single.html')

def ContactPage(request):
    return render(request,'contact.html')

def IndexPage(request):
    return render(request,'index.html')

def ServicesPage(request):
    return render(request,'services.html')

def WorkPage(request):
    return render(request,'work.html')


