from django.conf.urls import url
from .views import UserForm
from django.urls import path,include
app_name="signup"
urlpatterns=[
    path("",UserForm.as_view(),name="signup")
]