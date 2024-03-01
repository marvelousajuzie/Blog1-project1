from django.urls import path
from . import views


urlpatterns = [
    path('',views.index , name= 'index'),
    path('createblog', views.createblog, name= 'createblog'),
    path('updateblog/<int:pk>', views.updateblog, name= 'updateblog'),
    path('deleteblog/<int:pk>', views.deleteblog, name= 'deleteblog'),
    path('post/<str:pk>', views.post, name= 'post'),
]
