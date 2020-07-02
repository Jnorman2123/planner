from django.contrib import admin
from .models import User, Availability

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_available', 'start_time', 'end_time')
    exclude = ('date_created', )


admin.site.register(User, UserAdmin)
admin.site.register(Availability, AvailabilityAdmin)
