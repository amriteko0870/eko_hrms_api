from django.contrib import admin
import apiApp.models as models

# Register your models here.

admin.site.register(models.user_details)
admin.site.register(models.timesheet_log)
admin.site.register(models.overtime_log)
admin.site.register(models.leave_log)
admin.site.register(models.task_log)
admin.site.register(models.event_log)
admin.site.register(models.projects_log)
