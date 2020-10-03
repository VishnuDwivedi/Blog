from .models import *
from django.forms import ModelForm


class BlogDetailsForm(ModelForm):
    class Meta:
        model = BlogDetails
        exclude = ('comments',)
        fields = ('technology', 'short_details', 'description', 'blog_details_photo', )





