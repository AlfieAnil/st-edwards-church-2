from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django_ckeditor_5.fields import CKEditor5Field
import datetime
# Create your models here.

# Mass Times Model
class MassTimes(models.Model):
    ChurchID = models.IntegerField()
    Time = models.TextField()
    Day = models.CharField(max_length=9)
    Comment = models.TextField()

    def __str__(self):
        return self.Day

class PriestMessage(models.Model):
    PostID = models.AutoField(primary_key=True)
    Title = models.TextField(null=False, blank=False)
    Message = models.TextField()
    DateTime = models.TextField(null=False, blank=False)

class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    pmessage = models.ForeignKey(PriestMessage, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    
    def __str__(self):
        return 'image'


class ContactUsReturns(models.Model):
    ContactID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Member = models.CharField(max_length=3)
    Message = models.TextField()

    def __str__(self):
        return "{}. {}".format(self.ContactID, self.Name)

class ParishHubTimes(models.Model):
    Time = models.TextField()
    Day = models.CharField(max_length=9)

    def __str__(self):
        return '{} - {}'.format(self.Day, self.Time)


class CalendarItem(models.Model):
    Day = models.DateField()
    Time = models.CharField(max_length=15)
    Title = models.CharField(max_length=50)
    Details = models.TextField()

    def __str__(self):
        return '{}. {}'.format(self.Title, self.Details)

class NewsletterPDF(models.Model):
    newsletter_pdf = models.FileField()

class SacramentContent(models.Model):
    SacramentName = models.CharField(max_length=50)
    # SacramentDescription = RichTextField(blank=True, null=True)
    SacramentDescription = RichTextUploadingField(null=True)

class Clergy(models.Model):
    clergyName = models.CharField(max_length=100)
    clergyRole = models.CharField(max_length=50)
    clergyDescription = models.TextField()
    clergyPicture = models.ImageField(null=False, blank=False)

    def __str__(self):
        return '{}. {}'.format(self.clergyName, self.clergyRole)

class Schools(models.Model):
    schoolName = models.TextField()
    schoolIcon = models.ImageField()
    schoolDescription = models.TextField()
    schoolPhone = models.CharField(max_length=12)
    schoolFacebook = models.TextField()
    schoolWebsite = models.TextField()

    def __str__(self):
        return self.schoolName



class BaptismForm(models.Model):
    practicing_church_time = models.TextField(default='')
    child_surname = models.TextField()
    child_dob = models.DateField()
    child_baptism_name = models.TextField()

    address = models.TextField()
    postcode = models.CharField(max_length=7)

    # contact - at least one required
    telephone_number = models.CharField(max_length=12, blank=True)
    email = models.EmailField(blank=True)

    # details of parents - all required
    father_name = models.TextField()
    father_dob = models.DateField()
    father_religion = models.TextField()

    father_baptised_in_parish = models.CharField(max_length=1)

    father_date_baptism = models.TextField(blank=True, null=True)
    father_baptism_church = models.TextField(blank=True, default='None', null=True)
    father_date_confirmation = models.TextField(blank=True, default='None', null=True)
    father_confirmation_church = models.TextField()

    # mother details
    mother_name = models.TextField()
    mother_dob = models.DateField()
    mother_religion = models.TextField()

    mother_baptised_in_parish = models.CharField(max_length=1)

    mother_date_baptism = models.TextField(blank=True, default='None', null=True)
    mother_baptism_church = models.TextField(null=True)
    mother_date_confirmation = models.TextField(blank=True, default='None', null=True)
    mother_confirmation_church = models.TextField(null=True)

    mother_maidan_name = models.TextField(null=True)

    parents_marital_status = models.TextField()

    # godparent 1 is autofilled to be roman catholic
    godparent_name_1 = models.TextField()
    godparent_religion_1 = models.TextField()
    godparent_address_1 = models.TextField()
    godparent_postcode_1 = models.CharField(max_length=7)

    godparent_telephone_1 = models.CharField(max_length=12)

    godparent_dob_1 = models.DateField()
    godparent_baptism_church_1 = models.TextField()
    godparent_confirmation_date_1 = models.DateField()
    godparent_confirmation_church_1 = models.TextField()
    godparent_practicing_1 = models.TextField()

    # godparent 2 is autofilled to be roman catholic
    godparent_name_2 = models.TextField(blank=True)
    godparent_religion_2 = models.TextField(blank=True)
    godparent_address_2 = models.TextField(blank=True)
    godparent_postcode_2 = models.CharField(max_length=7, blank=True)

    godparent_telephone_2 = models.CharField(max_length=12, blank=True)

    godparent_dob_2 = models.TextField(null=True, blank=True, default='None')
    godparent_baptism_church_2 = models.TextField(blank=True)
    godparent_confirmation_date_2 = models.TextField(null=True, blank=True, default="None")
    godparent_confirmation_church_2 = models.TextField(blank=True)
    godparent_practicing_2 = models.TextField(blank=True)

    # Christian witness
    cw_name = models.TextField(blank=True)
    cw_gender = models.CharField(max_length=1)
    cw_religion = models.TextField(blank=True)
    cw_practicing = models.TextField(blank=True)

    cw_name_2 = models.TextField(null=True, blank=True)
    cw_gender_2 = models.CharField(max_length=1, null=True, blank=True)
    cw_religion_2 = models.TextField(null=True, blank=True)
    cw_practicing_2 = models.TextField(null=True, blank=True)

    # family details
    first_child = models.CharField(max_length=1)
    
    # catechesis
    course_attended = models.CharField(max_length=1)
    course_church = models.TextField()

class ChildClass(models.Model):
    family_entry = models.ForeignKey(BaptismForm, on_delete=models.CASCADE)
    child_name = models.TextField()
    child_dob = models.DateField()
    child_date_baptism = models.TextField(blank=True, default='None')
    child_school = models.TextField(blank=True) 
