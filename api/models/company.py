from django.db import models


class CompanyCertificate(models.Model):
    image = models.ImageField(upload_to='companies/')


class CompanyBenefit(models.Model):
    image = models.ImageField(upload_to='companies/')
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f'<CompanyBenefits {self.name}>'


class CompanyLocation(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='companies/')
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    hours = models.CharField(max_length=255)

    def __str__(self):
        return f'<CompanyLocation {self.name}>'


class CompanyInfo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    video = models.URLField()
    project_video = models.URLField()
    project_image = models.ImageField(upload_to='companies/')

    global_location = models.CharField(max_length=255)
    global_hours = models.CharField(max_length=255)
    global_phone_number = models.CharField(max_length=20)
    global_email = models.EmailField()

    locations = models.ManyToManyField(CompanyLocation, blank=True)
    benefits = models.ManyToManyField(CompanyBenefit, blank=True)
    certificates = models.ManyToManyField(CompanyCertificate, blank=True)

    our_team_image = models.ImageField(upload_to='companies/')


    def __str__(self):
        return f'<CompanyInfo {self.name}>'
