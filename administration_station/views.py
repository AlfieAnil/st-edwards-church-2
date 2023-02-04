from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, NewsletterUploadForm, SacramentEdit, EditPostForm
from django.contrib.auth.models import User, Group

from general.models import PriestMessage, Photo, NewsletterPDF, ContactUsReturns, SacramentContent, BaptismForm, ChildClass
from ckeditor.fields import RichTextField
from datetime import datetime
import pytz
from .decorators import unauthenticated_user, allowed_users, allowed_users_parish_home
from django.contrib.auth import get_user_model

from django.views.generic import UpdateView
# Create your views here.

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        print("post method happening")
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('parish-admin-home')
        
        else:
            messages.info(request, "Wrong Username or Password")
            return redirect('login')

    else:
        context = {}
        # return redirect('parish-admin-home')
        return render(request, 'administration_station/login.html', context)


@allowed_users(allowed_roles=['Administrator'])
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

@allowed_users(allowed_roles=['Administrator'])
def createPriestMessage(request):
    if request.method == 'POST':
        if request.POST['action_type'] == 'create':
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
            current_text = current.strftime("%d %B %Y, %H:%M")


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
        
        elif request.POST['action_type'] == 'delete':
            post_del_id = request.POST['post_delete_id']
            print(post_del_id)

            PriestMessage.objects.filter(PostID=post_del_id).delete()
            return redirect('manage-priest-message')

    posts = []


    for pmessage in PriestMessage.objects.all().order_by('-PostID'):
        print("Id: ", pmessage.PostID)
        print(pmessage.Title)
        all_photos = Photo.objects.filter(pmessage=pmessage)
        print(all_photos)
        photos_list = []
        for photo in all_photos:
            photos_list.append(photo.image.url)
        post_dictionary = {
            'value': pmessage.PostID,
            'Title': pmessage.Title,
            'Message': pmessage.Message,
            'Images': photos_list,
            'PhotoValue': len(photos_list),
            'DateTime': pmessage.DateTime
        }

        posts.append(post_dictionary)

    return render(request, 'administration_station/create-priest-message.html', {
        'priest_messages': posts
    })

@allowed_users(allowed_roles=['Administrator', 'Editor'])
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

@allowed_users(allowed_roles=['Administrator', 'Editor', 'Viewer'])
def contact_us_responses(request):
    if request.method == 'POST':
        print("post")
        print(request.POST)
        response_id = request.POST['contact_response_id']
        print(response_id)

        ContactUsReturns.objects.filter(ContactID=response_id).delete()

        return redirect('contact-us-responses')

    contact_us_returns = ContactUsReturns.objects.all().order_by('-ContactID')
    return render(request, 'administration_station/contact-us.html', {
        'contact_us': contact_us_returns
    })

@allowed_users(allowed_roles=['Administrator'])
def baptism_edit(request):
    baptism = SacramentContent.objects.get(id=1)
    if request.method == 'POST':
        form = SacramentEdit(request.POST, instance=baptism)
        if form.is_valid():
            form.save()
            return redirect('home')

    
    # print(baptism[0]['SacramentDescription'])
    form = SacramentEdit(instance=baptism)
    return render(request, 'administration_station/baptism.html', {
        'form': form
    })

@allowed_users(allowed_roles=['Administrator'])
def reconciliation(request):
    reconciliation = SacramentContent.objects.get(id=8)

    if request.method == 'POST':
        form = SacramentEdit(request.POST, instance=reconciliation)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = SacramentEdit(instance=reconciliation)
    return render(request, 'administration_station/reconciliation.html', {
        'form': form
    })

@allowed_users(allowed_roles=['Administrator'])
def anointing_sick(request):
    anointing_of_sick = SacramentContent.objects.get(id=3)

    if request.method == 'POST':
        form = SacramentEdit(request.POST, instance=anointing_of_sick)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = SacramentEdit(instance=anointing_of_sick)
    return render(request, 'administration_station/anointing_of_sick.html', {
        'form': form
    })

@allowed_users(allowed_roles=['Administrator'])
def confirmation(request):
    confirmation = SacramentContent.objects.get(id=4)

    if request.method == 'POST':
        form = SacramentEdit(request.POST, instance=confirmation)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = SacramentEdit(instance=confirmation)
    return render(request, 'administration_station/confirmation.html', {
        'form': form
    })

@allowed_users(allowed_roles=['Administrator'])
def holy_communion(request):
    holy_comm = SacramentContent.objects.get(id=5)

    if request.method == 'POST':
        form = SacramentEdit(request.POST, instance=holy_comm)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = SacramentEdit(instance=holy_comm)
    return render(request, 'administration_station/holy-communion.html', {
        'form': form
    })

@allowed_users(allowed_roles=['Administrator'])
def holy_orders(request):
    holy_order = SacramentContent.objects.get(id=6)

    if request.method == 'POST':
        form = SacramentEdit(request.POST, instance=holy_order)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = SacramentEdit(instance=holy_order)
    return render(request, 'administration_station/holy-orders.html', {
        'form': form
    })

@allowed_users(allowed_roles=['Administrator'])
def marriage(request):
    wedding = SacramentContent.objects.get(id=7)

    if request.method == 'POST':
        form = SacramentEdit(request.POST, instance=wedding)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = SacramentEdit(instance=wedding)
    return render(request, 'administration_station/marriage.html', {
        'form': form
    })

@allowed_users(allowed_roles=['Administrator'])
def funeral(request):
    current = SacramentContent.objects.get(id=2)

    if request.method == 'POST':
        form = SacramentEdit(request.POST, instance=current)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = SacramentEdit(instance=current)
    return render(request, 'administration_station/funeral.html', {
        'form': form
    })

@allowed_users(allowed_roles=['Administrator'])
def edit_post(request, postid):
    if request.method == 'POST':
        print('in post')
        print("request_type = ", request.POST['submit_type'])

        if request.POST['submit_type'] == 'delete-photo':
            delete_id = request.POST['photo-delete']

            Photo.objects.get(id=delete_id).delete()

            title = request.POST['Title']
            message = request.POST['Message']
            
            form = EditPostForm(initial={'Title': title, 'Message': message})
            all_photos = Photo.objects.filter(pmessage=PriestMessage.objects.get(PostID=postid))

            return render(request, 'administration_station/edit-post.html', {
                'form': form,
                'all_photos': all_photos
            })
            

        else:
            title = request.POST['Title']
            message = request.POST['Message']

            images = request.FILES.getlist('images')

            for image in images:
                photo = Photo.objects.create(
                    pmessage=PriestMessage.objects.get(PostID=postid),
                    image=image
                )
            
            post = PriestMessage.objects.get(PostID=postid)
            post.Title = title
            post.Message = message
            post.save()

            return redirect('manage-priest-message')
            
            
            



    print("post id is: ", postid)
    cur_post = PriestMessage.objects.get(PostID=postid)
    form = EditPostForm(instance=cur_post)

    all_photos = Photo.objects.filter(pmessage=cur_post)

    print(all_photos)

    return render(request, 'administration_station/edit-post.html', {
        'form': form,
        'all_photos': all_photos
    })

def logout_user(request):
    logout(request)

    return redirect('home')

@allowed_users_parish_home(allowed_roles=['Administrator', 'Editor', 'Viewer'])
def parish_admin_home(request):
    group = request.user.groups.all()[0]

    return render(request, 'administration_station/administration_home.html', {
        'group': group
    })

@allowed_users(allowed_roles=['Administrator', 'Editor', 'Viewer'])
def baptism_form_returns(request):

    if request.method == 'POST':
        print("request post: ", request.POST['baptism_form_id'])

        baptism_delete = BaptismForm.objects.get(id=request.POST['baptism_form_id'])
        baptism_delete.delete()
        redirect('baptism-form-responses')

    baptism_forms = BaptismForm.objects.all().order_by('-id')
    print(baptism_forms)
    return render(request, 'administration_station/baptism-form-responses.html', {
        'baptism_responses': baptism_forms
    })

@allowed_users(allowed_roles=['Administrator'])
def manage_users(request):

    if request.method == 'POST':
        print('post')
        print(request.POST['user-id'])

        user_delete = User.objects.get(id=request.POST['user-id'])
        user_delete.delete()
        redirect('manage-users')

    Userx = get_user_model()
    users = Userx.objects.filter(groups__name='Editor') | User.objects.filter(groups__name='Viewer')
    print("Printing all Users")
    print(users)
    return render(request, 'administration_station/manage-users.html', {
        'users': users
    })

def display_baptism_info(request, baptismid):
    baptism = BaptismForm.objects.get(id=baptismid)
    children = ChildClass.objects.filter(family_entry=baptism)

    print(children)

    return render(request, 'administration_station/baptism_form_info.html', {
        'baptism': baptism,
        'children': children
    })