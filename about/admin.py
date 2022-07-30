from django.contrib import admin
from django.utils.html import format_html

from .models import About


class MyAbout(admin.ModelAdmin):
    class Meta:
        modal = About

    def image_tag(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="100" height="100"/>')

    image_tag.short_description = 'Image'
    list_display = ['image_tag', 'email', 'age', 'created_at']
    list_display_links = ['email']
    readonly_fields = ['created_at']


# Register your models here.
admin.site.register(About, MyAbout)
