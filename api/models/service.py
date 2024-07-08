from django.db import models


class ServiceImage(models.Model):
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return f'<ServiceImage {self.image}>'


class ServiceBenefit(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'<ServiceBenefit {self.title}>'


class UniqueServiceBenefit(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'<UniqueServiceBenefit {self.title}>'


class Service(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='services/')
    short_description = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to='services/')
    description = models.TextField()

    protect_repair_desc = models.TextField()
    protect_repair_image = models.ImageField(upload_to='services/')

    benefits_description = models.CharField(max_length=255)
    benefits_blocks = models.ManyToManyField(UniqueServiceBenefit, blank=True, related_name='benefits_blocks')

    more_know_description = models.CharField(max_length=255)
    more_know_video = models.URLField()
    more_know_images = models.ManyToManyField(ServiceImage, blank=True, related_name='more_know_images')

    come_and_see_description = models.CharField(max_length=255)
    come_and_see_main_image = models.ImageField(upload_to='services/')
    come_and_see_benefits = models.ManyToManyField(ServiceBenefit, blank=True)
    come_and_see_images = models.ManyToManyField(ServiceImage, blank=True, related_name='come_and_see_images')

    final_block_description = models.CharField(max_length=255)
    final_block_images = models.ManyToManyField(ServiceImage, blank=True, related_name='final_block_images')

    def __str__(self):
        return f'<Service {self.title}>'
