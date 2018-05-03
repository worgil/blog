from django.contrib import admin
from .models import post


# from post.models import post
# Register your models here.
class PosAdmin(admin.ModelAdmin):
    list_display = ['title', 'publishing_date']
    list_display_links = ['publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['title', 'content']
    list_editable = ['title']

    class Meta:
        model = post


admin.site.register(post, PosAdmin)
