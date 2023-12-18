from django.urls import path
from . import views


urlpatterns = [
    path('<slug:slug>/', views.single_school_views, name="single-school"),
    path('all', views.all_schools_list, name="all-schools"),
]
