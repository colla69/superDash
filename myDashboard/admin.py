from django.contrib import admin

# Register your models here.

from myDashboard.models import DashApps,UniLink,DoneLinksLog

admin.site.register(DashApps)
admin.site.register(UniLink)
admin.site.register(DoneLinksLog)
