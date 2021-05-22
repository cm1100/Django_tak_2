from django.contrib import admin
from django.urls import path,include
from .views import PicCreateview,Articles_View,ArticlesView2,HomeView,After_Adding_View
from .views import stream_file
from django.views.generic import TemplateView

app_name="blogs"

urlpatterns = [
    path("home/",HomeView.as_view(),name="homepage"),
    path("blogs/",PicCreateview.as_view(),name="create_pic"),
    path("blogs/list/<int:pk>",Articles_View.as_view(),name="list_articles"),
    path('pic_picture/<int:pk>', stream_file, name='pic_picture'),
    path('pic_list',ArticlesView2.as_view(),name="list_article"),
    path('',After_Adding_View.as_view(),name="after")

]
