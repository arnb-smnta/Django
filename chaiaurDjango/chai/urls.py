from django.urls import path
from . import views

# chai/
urlpatterns = [
    path("", views.all_chai, name="all_chai"),
    path("<int:chaiId>/", views.chaiDetails, name="chaidetails"),
]
