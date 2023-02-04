from django.contrib import admin
from .models import MassTimes, PriestMessage, Photo, ContactUsReturns, ParishHubTimes, CalendarItem, NewsletterPDF, SacramentContent, Clergy, Schools, BaptismForm, ChildClass
# Register your models here.

admin.site.register(MassTimes)
admin.site.register(PriestMessage)
admin.site.register(Photo)
admin.site.register(ContactUsReturns)
admin.site.register(ParishHubTimes)
admin.site.register(CalendarItem)
admin.site.register(NewsletterPDF)
admin.site.register(SacramentContent)
admin.site.register(Clergy)
admin.site.register(Schools)
admin.site.register(BaptismForm)
admin.site.register(ChildClass)