from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from . models import MassTimes, PriestMessage, Photo, ContactUsReturns, ParishHubTimes, CalendarItem, NewsletterPDF, SacramentContent
from django.contrib import messages
from .forms import ContactUsForm
import datetime
# Create your views here.

def index(request):

    def checkForComment(time, comment):
        if len(comment) == 0:
            return time

        else: 
            return str(time + " - " + comment)

    # query = MassTimes.objects.all()
    query = MassTimes.objects.filter(ChurchID=1).values()
    print("Query: \n", query)
    sacred_heart_mass_times = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
        'Sunday': []
    }
    for item in query:
        if item['Day'] == "Monday":
            sacred_heart_mass_times['Monday'].append((item['Time'], item['Comment']))
            print(sacred_heart_mass_times)
        
        if item['Day'] == "Tuesday":
            sacred_heart_mass_times['Tuesday'].append((item['Time'], item['Comment']))
            print(sacred_heart_mass_times)

        if item['Day'] == "Wednesday":
            sacred_heart_mass_times['Wednesday'].append((item['Time'], item['Comment']))
            print(sacred_heart_mass_times)

        if item['Day'] == "Thursday":
            sacred_heart_mass_times['Thursday'].append((item['Time'], item['Comment']))
            print(sacred_heart_mass_times)

        if item['Day'] == "Friday":
            sacred_heart_mass_times['Friday'].append((item['Time'], item['Comment']))
            print(sacred_heart_mass_times)

        if item['Day'] == "Saturday":
            sacred_heart_mass_times['Saturday'].append((item['Time'], item['Comment']))
            print(sacred_heart_mass_times)

        if item['Day'] == "Sunday":
            sacred_heart_mass_times['Sunday'].append((item['Time'], item['Comment']))
            print(sacred_heart_mass_times)

    day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for day in day_list:
        if len(sacred_heart_mass_times[day]) == 0:
            del sacred_heart_mass_times[day]

    # St Cuthbert's Mass Times
    query = MassTimes.objects.filter(ChurchID=2).values()
    print("Query: \n", query)
    st_cuthberts_mass_times = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
        'Sunday': []
    }
    for item in query:
        if item['Day'] == "Monday":
            st_cuthberts_mass_times['Monday'].append((item['Time'], item['Comment']))
            print(st_cuthberts_mass_times)
        
        if item['Day'] == "Tuesday":
            st_cuthberts_mass_times['Tuesday'].append((item['Time'], item['Comment']))
            print(st_cuthberts_mass_times)

        if item['Day'] == "Wednesday":
            st_cuthberts_mass_times['Wednesday'].append((item['Time'], item['Comment']))
            print(st_cuthberts_mass_times)

        if item['Day'] == "Thursday":
            st_cuthberts_mass_times['Thursday'].append((item['Time'], item['Comment']))
            print(st_cuthberts_mass_times)

        if item['Day'] == "Friday":
            st_cuthberts_mass_times['Friday'].append((item['Time'], item['Comment']))
            print(st_cuthberts_mass_times)

        if item['Day'] == "Saturday":
            st_cuthberts_mass_times['Saturday'].append((item['Time'], item['Comment']))
            print(st_cuthberts_mass_times)

        if item['Day'] == "Sunday":
            st_cuthberts_mass_times['Sunday'].append((item['Time'], item['Comment']))
            print(st_cuthberts_mass_times)

    day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for day in day_list:
        if len(st_cuthberts_mass_times[day]) == 0:
            del st_cuthberts_mass_times[day]

    print("\n\n Testing the Priest messages... \n")

    # posts = [
    #     {

    #     },
    #     {

    #     }
    # ]

    posts = []


    for pmessage in PriestMessage.objects.all():
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
        
        

    # all_photos = Photo.objects.filter(pmessage=)

    return render(request, 'general/index.html', {
        'sacred_heart_mass_times': sacred_heart_mass_times,
        'st_cuthberts_mass_times': st_cuthberts_mass_times,
        'priest_messages': posts
    })


def test(request):
    return render(request, 'general/test.html')

def contact_us(request):
    context = {}
    form = ContactUsForm()
    if request.method == 'POST':
        print("post method")

        form = ContactUsForm(request.POST)

        if form.is_valid():
            # print("Full Name: ", form.cleaned_data['full_name'])
            name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            member = form.cleaned_data['member']
            message = form.cleaned_data['message']

            if (len(name.split()) < 2):
                messages.error(request, "Please enter your full name")
                context['form'] = form
                return render(request, 'general/contact-us.html', context)
            
            ContactUsReturns.objects.create(
                Name=name,
                Email=email,
                Member=member,
                Message=message

            )
            messages.error(request, "Your Message has been sent")
            return redirect('contact-us')
            

    
    context['form'] = form
    return render(request, 'general/contact-us.html', context)


def parish_hub(request):
    hub_times = ParishHubTimes.objects.all()
    print(hub_times)

    return render(request, 'general/parish-hub.html', {
        'hub_times': hub_times
    })


def calendar(request):
    def add_years(start_date, years):
        try:
            return start_date.replace(year=start_date.year + years)
        except ValueError:
            # 👇️ preseve calendar day (if Feb 29th doesn't exist, set to 28th)
            return start_date.replace(year=start_date.year + years, day=28)
            
    calendar_dates = CalendarItem.objects.filter(
        Day__range=[datetime.datetime.now().strftime("%Y-%m-%d"), add_years(datetime.datetime.now(), 10).strftime("%Y-%m-%d")]
    )   
    
    return render(request, 'general/calendar.html', {
        'calendar_items': calendar_dates
    })

def newsletter(request):
    if request.method == 'POST':
        print("post")
        return FileResponse(NewsletterPDF.objects.get(id=1).newsletter_pdf, as_attachment=True)
    newsletter = NewsletterPDF.objects.get(id=1)
    print(newsletter.newsletter_pdf.url)
    newsletter_path = newsletter.newsletter_pdf.url
    return render(request, 'general/newsletter.html', {
        'newsletter_path': newsletter_path
    })

def baptism(request):
    if request.method == 'POST':
        print("baptism form")
    
    baptism = SacramentContent.objects.get(SacramentName='Baptism')
    print(baptism)
    return render(request, 'general/baptism.html', {
        'baptism': baptism
    })