from django.urls import path, include
from . import views

urlpatterns = [
    path('parish-admin-home', views.parish_admin_home, name='parish-admin-home'),
    path('login', views.loginPage, name="login"),
    path('logout', views.logout_user, name='logout'),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('create-user', views.registerPage, name="create-user"),
    path('manage-priest-message', views.createPriestMessage, name="manage-priest-message"),
    path('upload-newsletter', views.NewsletterUpload, name='upload-newsletter'),
    path('contact-us-responses', views.contact_us_responses, name='contact-us-responses'),
    path('edit-baptism', views.baptism_edit, name='edit-baptism'),
    path('edit-reconciliation', views.reconciliation, name='edit-reconciliation'),
    path('edit-anointing-sick', views.anointing_sick, name='edit-anointing-sick'),
    path('edit-confirmation', views.confirmation, name='edit-confirmation'),
    path('edit-holy-communion', views.holy_communion, name='edit-holy-communion'),
    path('edit-holy-orders', views.holy_orders, name='edit-holy-orders'),
    path('edit-marriage', views.marriage, name='edit-marriage'),
    path('edit-funeral', views.funeral, name='edit-funeral'),
    path('edit-priest-post/<postid>', views.edit_post, name='edit-post'),
    path('baptism-form-responses', views.baptism_form_returns, name='baptism-form-responses'),
    path('view-baptism-info/<baptismid>', views.display_baptism_info, name='display-baptism-info'),
    path('manage-users', views.manage_users, name='manage-users')
]