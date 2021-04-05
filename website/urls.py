from django.urls import path
from website import views

#urls here
urlpatterns = [
    
    path('',views.home,name='home'),
    path('lugari.html',views.lugari,name='lugari'),
    path('central.html/',views.central,name='central'),
    path('ikolomani.html/',views.ikolomani,name='ikolomani'),
    path('butere.html/',views.butere,name='butere'),
    path('khwisero.html/',views.khwisero,name='khwisero'),
    path('likuyani.html/',views.likuyani,name='likuyani'),
    path('malava.html/',views.malava,name='malava'),
    path('mumiaseast.html/',views.mumiaseast,name='mumiaseast'),
    path('mumiaswest.html/',views.mumiaswest,name='mumiaswest'),
    path('navakholo.html/',views.navakholo,name='navakholo'),
    path('shinyalu.html/',views.shinyalu,name='shinyalu'),
    path('contact.html/',views.contact,name='contact')
    
]