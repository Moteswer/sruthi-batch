from django.contrib import admin
from django.urls import path, include
from .views import ProfileDetailView,kidprofile_details, home_view, kid_profile_registration_view, list_profiles, movie_list, profile_details, profile_registration_view, register_customer,login_view

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_customer, name='register_customer'),
    path('login/', login_view, name='login'),
    path('list_profiles/<int:customer_id>/', list_profiles, name='list_profiles'),
    path('profile/<int:customer_id>/', profile_registration_view, name='profile_registration'),
    path('profile/detail/<int:customer_id>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('customer/<int:customer_id>/kid-profile-registration/', kid_profile_registration_view, name='kid_profile_registration'),
    path('profile/detail/<int:customer_id>/profile/<int:profile_id>/', profile_details, name='profile_details'),
    path('profile/detail/<int:customer_id>/kidprofile/<int:profile_id>/', kidprofile_details, name='kidprofile_details'),
    path('media/', movie_list, name='movie_list'),

]
