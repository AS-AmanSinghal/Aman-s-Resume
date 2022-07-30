from django.contrib import admin
# Register your models here.
from django.utils.html import format_html

from education.models import Education


class MyEducation(admin.ModelAdmin):
    """ My Education """

    class Meta:
        modal = Education

    def image_tag(self, obj):
        return format_html(f'<img width=10% height=10% src="{obj.image.url}" />')

    image_tag.short_description = 'Image'
    list_display = ['image_tag', 'course', 'passing_year', 'score', 'created_at']
    list_display_links = ['course']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Education, MyEducation)
