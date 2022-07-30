from django.contrib import admin

# Register your models here.
from skills.models import Skills


class MySkills(admin.ModelAdmin):
    """ My Skills """

    class Meta:
        modal = Skills

    list_display = ['technology', 'created_at']
    list_display_links = ['technology']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Skills, MySkills)
