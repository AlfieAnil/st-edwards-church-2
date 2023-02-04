from django.contrib import admin
from .models import MassTimes, PriestMessage, Photo, ContactUsReturns, ParishHubTimes, CalendarItem, NewsletterPDF, SacramentContent
# Register your models here.

admin.site.register(MassTimes)
admin.site.register(PriestMessage)
admin.site.register(Photo)
admin.site.register(ContactUsReturns)
admin.site.register(ParishHubTimes)
admin.site.register(CalendarItem)
admin.site.register(NewsletterPDF)
admin.site.register(SacramentContent)
