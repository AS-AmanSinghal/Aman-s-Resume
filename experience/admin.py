from django.contrib import admin
# Register your models here.
from django.utils.html import format_html

from experience.models import Experience


class MyExperience(admin.ModelAdmin):
    """ My Experience """

    class Meta:
        modal = Experience

    def image_tag(self, obj):
        return format_html(f'<img width=10% height=10% src="{obj.image.url}" />')

    image_tag.short_description = 'Image'
    list_display = ['image_tag', 'company_name', 'address', 'created_at']
    list_display_links = ['company_name']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Experience, MyExperience)
