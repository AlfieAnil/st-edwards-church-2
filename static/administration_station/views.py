from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, NewsletterUploadForm
from django.contrib.auth.models import User, Group

from general.models import PriestMessage, Photo, NewsletterPDF

from datetime import datetime
import pytz

# Create your views here.
def loginPage(request):

    if request.method == 'POST':
        print("post method happening")
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('login')
        
        else:
            messages.info(request, "Wrong Username or Password")
            return redirect('login')

    else:
        context = {}
        return render(request, 'administration_station/login.html', context)



def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        print()
        print("post method happening")
        group = request.POST['administration-level']
        print(group)

        form = CreateUserForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was Created for ' + user)
            selected_group = Group.objects.get(name=group)
            selected_group.user_set.add(User.objects.get(username=user))
            return redirect('login')
        else:
            return render(request, 'administration_station/create_user.html', {
                'form': form
            })
    
    else:
        context = {'form': form}
        return render(request, 'administration_station/create_user.html', context)

    
def createPriestMessage(request):
    if request.method == 'POST':
        print("post method happening")
        data = request.POST
        print("Data: ", data)
        images = request.FILES.getlist('images')

        print("Title = " + data['Title'])
        print("Message = " + data['Message'])
        title = data['Title']
        message = data['Message']

        current = datetime.now().astimezone(pytz.timezone('Europe/London'))

        current_text = ""
        current_text = current_text.strftime("%d %B %Y, %H:%M")


        if len(title) != 0:
            priest_message = PriestMessage.objects.create(
                Title=title,
                Message=message,
                DateTime=current_text
            )

            # print("Priest Message: " + type(priest_message))
          
        for image in images:
            photo = Photo.objects.create(
                pmessage=priest_message,
                image=image
            )

    
    return render(request, 'administration_station/create-priest-message.html')


def NewsletterUpload(request):

    if request.method == 'POST':
        print("post")
        form = NewsletterUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print("Valid")
            file = form.cleaned_data.get('pdf_file')
            print("File: ", file.name)
            if not (file.name).endswith('.pdf'):
                print("Not a pdf")
            else:
                newsletter = NewsletterPDF.objects.get(id=1)
                newsletter.newsletter_pdf = file
                newsletter.save()

        

    form = NewsletterUploadForm()
    return render(request, 'administration_station/newsletter-upload.html', {
        'form': form
    })