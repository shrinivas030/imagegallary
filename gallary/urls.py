from django.urls import path
from gallary import views
urlpatterns = [
    path('',views.imageview,name='imagepage'),
    path('searchpage',views.searchview,name='searchpage')

]
