from django.db import models

# Create your models here.


# dash_apps

class DashApps(models.Model):
    name = models.TextField(db_column='Name', max_length=100)  # Field name made lowercase.
    link = models.CharField(max_length=500, blank=True, null=True)
    img_link = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'myDashboard_dash_apps'

class UniLink(models.Model):
    name = models.TextField(db_column='Name', max_length=100)  # Field name made lowercase.
    link = models.CharField(max_length=500, blank=True, null=True)
    homepage = models.TextField(max_length=500, blank=True, null=True)
    uebungen = models.TextField(max_length=500, blank=True, null=True)
    cloudlink = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'myDashboard_uni_links'

