from django.db import models


class DoctorSocial(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    icon = models.ImageField(upload_to='doctors/')

    def __str__(self):
        return f'<DoctorSocial {self.name}>'


class DoctorEducation(models.Model):
    title = models.CharField(max_length=255)
    # year = models.CharField(max_length=255)

    def __str__(self):
        return f'<DoctorEducation {self.title}>'


class Doctor(models.Model):
    fullname = models.CharField(max_length=255)
    image = models.ImageField(upload_to='doctors/')
    position = models.CharField(max_length=255)
    best = models.BooleanField()
    location = models.CharField(max_length=255)
    biography = models.TextField()

    social = models.ManyToManyField(DoctorSocial, blank=True)
    education = models.ManyToManyField(DoctorEducation, blank=True)

    def __str__(self):
        return f'<Doctor {self.fullname}>'
