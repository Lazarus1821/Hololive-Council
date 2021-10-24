from django.contrib import admin
from .models import ChannelName
# Register your models here.


class ChannelNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_url')


admin.site.register(ChannelName, ChannelNameAdmin)