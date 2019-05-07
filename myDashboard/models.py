from django.db import models

# Create your models here.


# dash_apps
APP ="app"
UTIL = "util"
APP_TYPES = (
    (APP, 'app'),
    (UTIL, 'util'),
)
class DashApps(models.Model):

    name = models.TextField(db_column='Name', max_length=100)  # Field name made lowercase.
    link = models.TextField(max_length=500, blank=True, null=True)
    img_link = models.TextField(max_length=500, blank=True, null=True)
    type = models.CharField(db_column='Type', max_length=20, choices=APP_TYPES, default=APP)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'myDashboard_dash_apps'


##uni links
class UniLink(models.Model):
    name = models.TextField(db_column='Name', max_length=100)
    link = models.TextField(max_length=500, blank=True, null=True)
    homepage = models.TextField(max_length=500, blank=True, null=True)
    uebungen = models.TextField(max_length=500, blank=True, null=True)
    cloudlink = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'myDashboard_uni_links'


# log seen links
class DoneLinksLog(models.Model):
    link = models.TextField(max_length=500)
    done = models.BooleanField()

    def __str__(self):
        return self.link

    class Meta:
        managed = False
        db_table = 'myDashboard_donelinks_log'