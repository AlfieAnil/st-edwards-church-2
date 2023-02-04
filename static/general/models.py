from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
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
    SacramentDescription = RichTextUploadingField(blank=True, null=True)
