from django.urls import path
from django.conf.urls import url
from Table import views

urlpatterns = [
    path("home/", views.home, name="Table-home"),
    path("signup/", views.signup, name="Table-signup"),
    path("", views.login, name="Table-login"),
    path("login/", views.login, name="Table-login"),
    url("sender/", views.sender, name="Table-sender"),
    url("new-user/", views.new_user, name="Table-new-user"),
    url("new-student/", views.new_student, name="Table-new-student")
]
