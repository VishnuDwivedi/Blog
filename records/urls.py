from django.urls import path
from .views import *

urlpatterns = [

 path('dashboard/', dashboard, name='dashboard'),
 path('technology/<int:technology_id>/', technologies, name='technology'),
 path('<str:name>/<int:blog_id>/', blog_details, name='blog_details'),
 path('logout/', logout, name='logout'),
 path('add-blog/', BlogCreation.as_view(), name='add-blog'),
 path('accounts/signup', signup, name='signup'),
 path('blog-comments/<int:blog_id>/<str:comment>', save_comment, name='blog-comment'),
# path('update_blog', update_blog),
 path('increase_like/<int:comm_id>', increase_like, name='increase_like'),
 #path('consume_blog', consume_blog),



]
