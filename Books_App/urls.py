from django.urls import path,re_path
from . import views

urlpatterns = [
                path('',views.home,name='home'),
                path('Contact/',views.Contact,name='Contact'),
                path('Books_Page/',views.Books_Page,name='Book_page'),
                path('<int:pk>/',views.Owner_Contact,name='contact_person'),
                path('<str:pk>/',views.Books_Page,name='type_book'),

]
