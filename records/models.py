from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Category:
    Name = (
        ('Python', 'Python'),
        ('JavaScript', 'JavaScript'),
        ('Linux', 'Linux'),
        ('Django', 'Django'),
        ('Java', 'Java'),
        ('ML', 'ML')
    )


# Create your models here.
class Team(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    photo = models.ImageField(null=False, blank=False, upload_to='media/')
    member_about = models.CharField(max_length=40, null=True, blank=True)
    class Meta:
        default_permissions = ('view')
                       

    def __str__(self):
        return str(self.name)


class Details(models.Model):
    about = models.CharField(max_length=200, null=False, blank=False)
    contact = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.contact


class BlogCategory(models.Model):
    name = models.CharField(max_length=20, choices=Category.Name, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    blog_photo = models.ImageField(blank=False, null=False, upload_to='media/')

    def __str__(self):
        return self.name


class BlogDetails(models.Model):
    technology = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Technology")
    short_details = models.CharField(max_length=40, null=False, blank=False, verbose_name="Short Details")
    description = RichTextField(null=False, blank=False, verbose_name="Description")
    blog_details_photo = models.ImageField(null=True, blank=True, upload_to='Attachments/', verbose_name="Code Snippet")
    written_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Written By")
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.technology)+ "-->" + str(self.short_details)


class BlogComments(models.Model):
    blog_id = models.ForeignKey(BlogDetails, on_delete=models.CASCADE)
    comments = models.TextField(null=True, blank=True)
    like = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, verbose_name="User")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    liked_user = models.TextField(default="string")

    def __str__(self):
        return str(self.comments)


