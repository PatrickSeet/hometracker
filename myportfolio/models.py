from django.db import models

# Create your models here.
class Projects(models.Model):
    project = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    link = models.URLField(null=True)

    def __unicode__(self):
        return self.project