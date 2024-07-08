from django.urls import path

from api.views import (ServicesView, PostsView, PostView, DoctorsView, CompanyInfoView, CommentsView,
                       CompanyLocationView, BookingCreateView, CallBackRequestView, ServiceView)

urlpatterns = [
    path('services/', ServicesView.as_view(), name='services'),
    path('services/<int:pk>/', ServiceView.as_view(), name='service'),

    path('posts/', PostsView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostView.as_view(), name='post'),


    path('doctors/', DoctorsView.as_view(), name='doctors'),
    # path('doctors/<int:pk>/', DoctorView.as_view(), name='doctor'),

    path('company-info/', CompanyInfoView.as_view(), name='company-info'),
    path('company-locations/', CompanyLocationView.as_view(), name='company-locations'),


    path('comments/', CommentsView.as_view(), name='comments'),

    path('booking/', BookingCreateView.as_view(), name='booking'),
    path('callback/', CallBackRequestView.as_view(), name='callback'),



]