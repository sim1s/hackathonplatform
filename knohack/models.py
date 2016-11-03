from django.db import models
from django.utils import timezone
#from ckeditor.fields import RichTextField
#from tinymce.models import HTMLField

class Event(models.Model):
    event_name = models.CharField(max_length=75)
    event_theme = models.CharField(max_length=75, blank = True)
    #change to min/max grade
    min_grade = models.IntegerField(choices = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6),
                                                    (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)),
                                                    null = True, blank = True)
    max_grade = models.IntegerField(choices = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6),
                                                    (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)),
                                                    null = True, blank = True)
    time_zone = models.CharField(max_length = 15, help_text = "ex: PST", blank = True)
    start_time = models.DateTimeField(help_text = "Please use 24 hour time.", null = True, blank = True)
    end_time = models.DateTimeField(help_text = "Please use 24 hour time.", null = True, blank = True)
    location_name = models.CharField(max_length=75, help_text = "ex: Pleasanton Library", blank = True)
    location_address_1 = models.CharField(max_length=75, help_text = "ex: 400 Old Bernal Ave", blank = True)
    location_address_2 = models.CharField(max_length=75, help_text = "ex: Building 2, Lobby, etc.", blank = True)
    city = models.CharField(max_length=75, help_text = "ex: Pleasanton", blank = True)
    state = models.CharField(max_length=2, help_text = "ex: CA", blank = True)
    zip_code = models.CharField(max_length = 5, help_text = "ex: 94566", blank = True)
    country = models.CharField(max_length = 75, help_text = "ex: United States", blank = True)
    event_details = models.TextField(default = None, help_text="Detailed description of your event goes here.", blank=True)
    optional_event_details = models.TextField(help_text = "Additional detailed description of your event goes here.", default = None, blank=True)
    event_FAQ = models.TextField(help_text = "FAQs go here.", default = None, blank =True)
    event_contact_name = models.CharField(max_length = 30, help_text = "Name of the contact for your event.", blank = True)
    event_contact_phone = models.CharField(max_length = 30, help_text = "Phone number of the contact for your event.", blank = True)
    event_contact_email = models.CharField(max_length = 255, help_text = "Email of the contact for your event.", blank = True)
    event_banner = models.FileField(upload_to='images/',
                    help_text = "Dimensions: minimum 2160 x 1080px. File Type: JPEG, PNG, BMP, or GIF. File Size: no larger than 10 MB.",
                    null = True, blank = True)
    event_access_code = models.CharField(max_length=10, help_text = "clarify: 10 or fewer character access code for your event.")
    registration_code = models.CharField(max_length=10, help_text = "clarify: 10 or fewer character access code for your event.")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.event_name
