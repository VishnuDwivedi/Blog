from django.contrib import admin
from .models import *

# Register your models here.


class BlogDetailsAdmin(admin.ModelAdmin):
    model = BlogDetails
    list_filter = ('technology',)


admin.site.register(Team)
admin.site.register(Details)
admin.site.register(BlogCategory)
admin.site.register(BlogDetails, BlogDetailsAdmin)
admin.site.register(BlogComments)

