from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from . models import MassTimes, PriestMessage, Photo, ContactUsReturns, ParishHubTimes, CalendarItem, NewsletterPDF, SacramentContent, Clergy, Schools, ChildClass, BaptismForm
from django.contrib import messages
from .forms import ContactUsForm, baptismsForm
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
    ).order_by('Day', 'Time')   
    
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
    baptism_form = baptismsForm()
    if request.method == 'POST':
        print("baptism form")
        other_children_dictionary = {}
        baptism = SacramentContent.objects.get(SacramentName='Baptism')
        details = request.POST
        truth_values = True
        print("number of children "+details['children-number'])

        # Have to create the form submission first
        practicing_church_time = details['practicing_church_time']
        child_surname = details['child_surname']
        child_dob = details.get('child_dob', False)
        child_baptism_name = details['child_baptism_name']
        address = details['address']
        postcode = details['postcode']
        telephone_number = details['telephone_number']
        email = details['email']
        father_name = details['father_name']
        father_dob = details.get('father_dob', False)
        father_religion = details['father_religion']
        father_baptised_in_parish = details['father_baptised_in_parish']
        if father_baptised_in_parish == "Yes":
            father_baptised_in_parish = "Y"
        else:
            father_baptised_in_parish = "N"

        # father_date_baptism = details['father_date_baptism']
        father_date_baptism = details.get('father_date_baptism', False)
        father_baptism_church = details['father_baptism_church']
        father_date_confirmation = details.get('father_date_confirmation', False)
        father_confirmation_church = details['father_confirmation_church']
        mother_name = details['mother_name']
        mother_dob = details.get('mother_dob', False)
        mother_religion = details['mother_religion']
        mother_baptised_in_parish = details['mother_baptised_in_parish']
        if mother_baptised_in_parish == "Yes":
            mother_baptised_in_parish = "Y"
        else:
            mother_baptised_in_parish = "N"
        mother_date_baptism = details.get('mother_date_baptism', False)
        mother_baptism_church = details['mother_baptism_church']
        mother_date_confirmation = details.get('mother_date_confirmation', False)
        mother_confirmation_church = details['mother_confirmation_church']
        mother_maidan_name = details['mother_maidan_name']
        parents_marital_status = details['parents_marital_status']
        godparent_name_1 = details['godparent_name_1']
        godparent_religion_1 = "Catholic"
        godparent_address_1 = details['godparent_address_1']
        godparent_postcode_1 = details['godparent_postcode_1']
        godparent_telephone_1 = details['godparent_telephone_1']
        godparent_dob_1 = details.get('godparent_dob_1', False)
        godparent_baptism_church_1 = details['godparent_baptism_church_1']
        godparent_confirmation_date_1 = details.get('godparent_confirmation_date_1', False)
        godparent_confirmation_church_1 = details['godparent_confirmation_church_1']
        godparent_practicing_1 = details['godparent_practicing_1']
        
        godparent_name_2 = details['godparent_name_2']
        godparent_religion_2 = "Catholic"
        godparent_address_2 = details['godparent_address_2']
        godparent_postcode_2 = details['godparent_postcode_2']
        godparent_telephone_2 = details['godparent_telephone_2']
        godparent_dob_2 = details.get('godparent_dob_2')
        godparent_baptism_church_2 = details['godparent_baptism_church_2']
        godparent_confirmation_date_2 = details.get('godparent_confirmation_date_2', False)
        godparent_confirmation_church_2 = details['godparent_confirmation_church_2']
        godparent_practicing_2 = details['godparent_practicing_2']

        cw_name = details['cw_name']
        cw_gender = details['cw_gender']
        if cw_gender == "Male":
            cw_gender = "M"
        else:
            cw_gender = "F"

        cw_religion = details['cw_religion']
        cw_practicing = details['cw_practicing']

        cw_name_2 = details['cw_name_2']
        cw_gender_2 = details['cw_gender_2']
        if cw_gender_2 == "Male":
            cw_gender_2 = "M"
        else:
            cw_gender_2 = "F"

        cw_religion_2 = details['cw_religion_2']
        cw_practicing_2 = details['cw_practicing_2']

        first_child = details['first_child']
        if first_child == "Yes":
            first_child = "Y"
        else:
            first_child = "N"

        course_attended = details['course_attended']
        if course_attended == "Yes":
            course_attended = "Y"
        else:
            course_attended = "N"
        course_church = details['course_church']

        print(child_dob, father_dob, father_date_baptism)

        created_baptism = BaptismForm.objects.create(
            practicing_church_time=practicing_church_time,
            child_surname=child_surname,
            child_dob=child_dob,
            child_baptism_name=child_baptism_name,
            address=address,
            postcode=postcode,
            telephone_number=telephone_number,
            email=email,
            father_name=father_name,
            father_dob=father_dob,
            father_religion=father_religion,
            father_baptised_in_parish=father_baptised_in_parish,
            father_date_baptism=father_date_baptism,
            father_baptism_church=father_baptism_church,
            father_date_confirmation=father_date_confirmation,
            father_confirmation_church=father_confirmation_church,
            mother_name=mother_name,
            mother_dob=mother_dob,
            mother_religion=mother_religion,
            mother_baptised_in_parish=mother_baptised_in_parish,
            mother_date_baptism=mother_date_baptism,
            mother_baptism_church=mother_baptism_church,
            mother_date_confirmation=mother_date_confirmation,
            mother_confirmation_church=mother_confirmation_church,
            mother_maidan_name=mother_maidan_name,
            parents_marital_status=parents_marital_status,
            godparent_name_1=godparent_name_1,
            godparent_religion_1=godparent_religion_1,
            godparent_address_1=godparent_address_1,
            godparent_postcode_1=godparent_postcode_1,
            godparent_telephone_1=godparent_telephone_1,
            godparent_dob_1=godparent_dob_1,
            godparent_baptism_church_1=godparent_baptism_church_1,
            godparent_confirmation_date_1=godparent_confirmation_date_1,
            godparent_confirmation_church_1=godparent_confirmation_church_1,
            godparent_practicing_1=godparent_practicing_1,
            godparent_name_2=godparent_name_2,
            godparent_religion_2=godparent_religion_2,
            godparent_address_2=godparent_address_2,
            godparent_postcode_2=godparent_postcode_2,
            godparent_telephone_2=godparent_telephone_2,
            godparent_dob_2=godparent_dob_2,
            godparent_baptism_church_2=godparent_baptism_church_2,
            godparent_confirmation_date_2=godparent_confirmation_date_2,
            godparent_confirmation_church_2=godparent_confirmation_church_2,
            godparent_practicing_2=godparent_practicing_2,
            cw_name=cw_name,
            cw_gender=cw_gender,
            cw_religion=cw_religion,
            cw_practicing=cw_practicing,
            cw_name_2=cw_name_2,
            cw_gender_2=cw_gender_2,
            cw_religion_2=cw_religion_2,
            cw_practicing_2=cw_practicing_2,
            first_child=first_child,
            course_attended=course_attended,
            course_church=course_church
        )



        if details['first_child'] == "No":
            print("Instance: ", isinstance(details['children-number'], int))
            number_of_other_children = details['children-number']
            
            for i in range(int(number_of_other_children)):
                temp = []

                temp.append(details.get("child-name-{}".format(i+1), False))
                temp.append(details.get("child-dob-{}".format(i+1), False))
                print("baptism date: " + details.get("child-baptism-{}".format(i+1), False))
                if details.get("child-baptism-{}".format(i+1), False) == "" or details.get("child-baptism-{}".format(i+1), False) == None:
                    temp.append("0000/00/00")
                else:
                    temp.append(details.get("child-baptism-{}".format(i+1), False))

                temp.append(details.get("child-school-{}".format(i+1), False))
                print("Temp: ", temp)
                other_children_dictionary["child-{}".format(i+1)] = temp

                ChildClass.objects.create(
                    family_entry = created_baptism,
                    child_name = temp[0],
                    child_dob = temp[1],
                    child_date_baptism = temp[2],
                    child_school = temp[3]
                )
                
            print('dictionary: ', other_children_dictionary)
            







        # Checking whether there is a telephone or email
        # if details['telephone_number'] != '' or details['email'] != '':
        #     print("okay")
        # else:
        #     messages.error(request, 'Please enter a phone number or email address')
        #     baptism_form = baptismsForm(request.POST) 
        #     return render(request, 'general/baptism.html', {
        #         'baptism': baptism,
        #         'baptism_form': baptism_form
        #     })

        # Checking Godparents details
        # godparent_1_details = []
        # godparent_1_details.append(details['godparent_name_1'])
        # godparent_1_details.append(details['godparent_address_1'])
        # godparent_1_details.append(details['godparent_postcode_1'])
        # godparent_1_details.append(details['godparent_telephone_1'])
        # godparent_1_details.append(details['godparent_dob_1'])
        # godparent_1_details.append(details['godparent_baptism_church_1'])
        # godparent_1_details.append(details['godparent_confirmation_date_1'])
        # godparent_1_details.append(details['godparent_confirmation_church_1'])
        # godparent_1_details.append(details['godparent_practicing_1'])
        
        # for information in godparent_1_details:
        #     if information == '' or information == None:
        #         messages.error(request, "Please fill in all of the details for Godparent 1")
        #         baptism_form = baptismsForm(request.POST) 
        #         return render(request, 'general/baptism.html', {
        #             'baptism': baptism,
        #             'baptism_form': baptism_form
        #         })

        # godparent_2_details = []
        # godparent_2_details.append(details['godparent_name_2'])
        # godparent_2_details.append(details['godparent_address_2'])
        # godparent_2_details.append(details['godparent_postcode_2'])
        # godparent_2_details.append(details['godparent_telephone_2'])
        # godparent_2_details.append(details['godparent_dob_2'])
        # godparent_2_details.append(details['godparent_baptism_church_2'])
        # godparent_2_details.append(details['godparent_confirmation_date_2'])
        # godparent_2_details.append(details['godparent_confirmation_church_2'])
        # godparent_2_details.append(details['godparent_practicing_2'])

        # if details['godparent_name_2'] != '' or details['godparent_name_2'] != None:
        #     for information in godparent_2_details:
        #         if information == '' or information == None:
        #             messages.error(request, "It looks like you have given a second godparent, please fill in all of the required details for the second godparent.")
        #             baptism_form = baptismsForm(request.POST) 
        #             return render(request, 'general/baptism.html', {
        #                 'baptism': baptism,
        #                 'baptism_form': baptism_form
        #             })

        # cw_1_details = []
        # cw_1_details.append(details['cw_name'])
        # cw_1_details.append(details['cw_gender'])
        # cw_1_details.append(details['cw_religion'])
        # cw_1_details.append(details['cw_practicing'])

        # if details['cw_name'] != '' or details['cw_name'] != None:
        #     for information in cw_1_details:
        #         if information == '' or information == None:
        #             messages.error(request, "It looks like you have added a christian witness, ")
        #             baptism_form = baptismsForm(request.POST) 
        #             return render(request, 'general/baptism.html', {
        #                 'baptism': baptism,
        #                 'baptism_form': baptism_form
        #             })


        


        # Checking the Other Children
        # if details['first_child'] == "No":
        #     print("Instance: ", isinstance(details['children-number'], int))
        #     number_of_other_children = details['children-number']
            
        #     for i in range(int(number_of_other_children)):
        #         temp = []

        #         temp.append(details.get("child-name-{}".format(i+1), False))
        #         temp.append(details.get("child-dob-{}".format(i+1), False))
        #         print("baptism date: " + details.get("child-baptism-{}".format(i+1), False))
        #         if details.get("child-baptism-{}".format(i+1), False) == "" or details.get("child-baptism-{}".format(i+1), False) == None:
        #             temp.append("Not Bapised")
        #         else:
        #             temp.append(details.get("child-baptism-{}".format(i+1), False))

        #         temp.append(details.get("child-school-{}".format(i+1), False))
        #         print("Temp: ", temp)
        #         other_children_dictionary["child-{}".format(i+1)] = temp
                
        #     print('dictionary: ', other_children_dictionary)
            
        #     truth_values = False


        # if not truth_values:
        #     baptism_form = baptismsForm(request.POST) 
        #     return render(request, 'general/baptism.html', {
        #         'baptism': baptism,
        #         'baptism_form': baptism_form
        #     })
    
    baptism = SacramentContent.objects.get(SacramentName='Baptism')
    print(baptism)
    return render(request, 'general/baptism.html', {
        'baptism': baptism,
        'baptism_form': baptism_form
    })

def funeral(request):
    funeral = SacramentContent.objects.get(SacramentName='Funeral')
    print(funeral)
    return render(request, 'general/funeral.html', {
        'funeral': funeral
    })

def anointing(request):
    anointing = SacramentContent.objects.get(SacramentName='Anointing of the Sick')
    print(anointing)
    return render(request, 'general/anointing-of-the-sick.html', {
        'anointing': anointing
    })

def confirmation(request):
    confirmation = SacramentContent.objects.get(SacramentName='Confirmation')

    return render(request, 'general/confirmation.html', {
        'confirmation': confirmation
    })

def holy_communion(request):
    holy_communion = SacramentContent.objects.get(SacramentName='Holy Communion')
    return render(request, 'general/holy-communion.html', {
        'communion': holy_communion
    })

def holy_orders(request):
    holy_orders = SacramentContent.objects.get(SacramentName='Holy Orders')
    return render(request, 'general/holy-orders.html', {
        'holy_orders': holy_orders
    })

def marriage(request):
    marriage = SacramentContent.objects.get(SacramentName="Marriage")
    return render(request, 'general/marriage.html', {
        'marriage': marriage
    })


def reconciliation(request):
    reconciliation = SacramentContent.objects.get(SacramentName="Reconciliation")
    return render(request, 'general/reconciliation.html', {
        'reconciliation': reconciliation
    })

def about_us(request):
    clergy_list = Clergy.objects.all()
    print(clergy_list)
    return render(request, 'general/about-us.html', {
        'clergy_list': clergy_list
    })

def schools(request):
    schools = Schools.objects.all()
    print(schools)
    return render(request, 'general/schools.html', {
        'schools': schools
    })

def liturgy(request):
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

    return render(request, 'general/liturgy.html', {
        'sacred_heart_mass_times': sacred_heart_mass_times,
        'st_cuthberts_mass_times': st_cuthberts_mass_times,
    })

    
    
