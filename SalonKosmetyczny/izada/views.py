from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.mail import send_mail
from decouple import config
from django.contrib import messages
from django.conf import settings
from .forms import CommentForm


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

def BlogsinglePage(request, pk):
    blog = Blog.objects.get(pk=pk)
    template_name = 'blog_single.html'
    comments = blog.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.blog = blog
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()


    return render(request, template_name, {'blog': blog,
                                           'comments': comments,
                                            'new_comment': new_comment,
                                            'comment_form': comment_form})


def ContactPage(request):
    print("Metoda sie wywoluje")
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        emailpassedbytheuser = request.POST.get('emailpassedbytheuser')
        topic = request.POST.get('topic')
        message = request.POST.get('message')
        topicclientemail = 'Formularz Salon IZADA'

        sender_email = config('EMAIL_USERNAME')
        email = config('emailreceiver')
        finalmessage = (emailpassedbytheuser + name + message)
        
    
        print(f"Temat: {topic}")
        print(f"Wiadomosc: {finalmessage}")
        print(f"Kto wysyla: {sender_email}")
        print(f"Kto dostaje: {email}")
        send_mail(topic, f'{emailpassedbytheuser}\n {name}\n {message}', sender_email, [email])
        messages.success(request, 'Wiadomość została wysłana.')
        messages.error(request, 'Wiadomość  nie została wysłana.')


        send_mail(topicclientemail, f' Wiadomość o teści\n {message}\n została przesłana.\n Skontaktujemy się z tobą najszybciej jak to tylko możliwe!', sender_email, [emailpassedbytheuser])
        return render(request,'confirmation.html')
    else:
        return render(request, 'contact.html')
    

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

def ConfirmationPage(request):
    return render(request,'confirmation.html')