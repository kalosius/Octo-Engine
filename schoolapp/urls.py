from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import initiate_payment, check_payment_status, momo_callback


urlpatterns = [
    path('initiate-payment/', initiate_payment, name='initiate_payment'),
    path('payment-status/<str:transaction_id>/', check_payment_status, name='check_payment_status'),


    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('gamesports/', views.gamesports, name='gamesports'),
    path('clubsandactivities/', views.clubsandactivities, name='clubsandactivities'),
    path('events/', views.events, name='events'),
    path('schooladmin/', views.schooladmin, name='schooladmin'),
    path('unebperformance/', views.unebperformance, name='unebperformance'),
    path('beststudents/', views.beststudents, name='beststudents'),
    path('admissions/', views.admissions, name='admissions'),
    path('seniorone/auth/register', views.formoneregister, name='formoneregister'),
    path('select-form/', views.select_form, name='selectform'),
    path('momo-callback/', momo_callback, name='momo_callback'),

]

# Images to load in the browser
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

