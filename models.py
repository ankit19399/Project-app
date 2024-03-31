from django.db import models

class Tasks(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    CATEGORY_CHOICES = (  
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('other', 'Other'),
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)