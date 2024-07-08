from django.contrib import admin

from api.models import (Service, Post, PostImage, Doctor, DoctorSocial, DoctorEducation, CompanyInfo, CompanyLocation,
                        CompanyBenefit, Comment, CompanyCertificate, CallBackRequest, Booking,
                        ServiceBenefit, ServiceImage, UniqueServiceBenefit)

admin.site.register(Service)
admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(Doctor)
admin.site.register(DoctorSocial)
admin.site.register(DoctorEducation)
admin.site.register(CompanyInfo)
admin.site.register(CompanyLocation)
admin.site.register(CompanyBenefit)
admin.site.register(Comment)
admin.site.register(CompanyCertificate)
admin.site.register(CallBackRequest)
admin.site.register(Booking)
admin.site.register(ServiceBenefit)
admin.site.register(ServiceImage)
admin.site.register(UniqueServiceBenefit)

