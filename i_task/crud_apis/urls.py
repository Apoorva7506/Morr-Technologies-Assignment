from django.urls import path, re_path, include
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import *


urlpatterns = [
    # path("", login, name="login"),
     path("", index, name="index"),
     url(r"^contact/$", ContactListView.as_view()),
     url(r'^contact/?(?P<pk>[^/]+)/$', ContactDetail.as_view()),
     url("search/", ContactSearchView.as_view()),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]