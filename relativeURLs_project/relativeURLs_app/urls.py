from django.urls import path
from relativeURLs_app import views

# SET THE NAMESPACE!
app_name = 'relativeURLs_app'

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
