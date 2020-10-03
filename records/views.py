from django.shortcuts import render, redirect
from .models import *
from django.views.generic import View
from .forms import BlogDetailsForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('records:dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def dashboard(request):
    details = Details.objects.filter(id=1).values('about', 'email', 'contact')
#file1= BlogDetails.objects.filter(id=23)
#   file1=file1.blog_details_photo.name
#   print(file1)
    s = str(request.user)
    if s == 'AnonymousUser':

        user = False

    else:
        user = User.objects.get(username=request.user.username)

    context = {
        'details': details,
        'user': user
    }
    return render(request, 'index.html', context)


def technologies(request, technology_id):
    s = str(request.user)

    if s == 'AnonymousUser':

        user = False

    else:
        user = User.objects.get(username=request.user.username)
    technology_details = BlogDetails.objects.filter(technology=technology_id, approved=True).values('id',
                                                                                                    'technology__name',
                                                                                                    'short_details',
                                                                                                    'written_by__username',
                                                                                                    'created_at').order_by(
        '-id')

    details = Details.objects.filter(id=1).values('about', 'email', 'contact')
    return render(request, 'blogs/technology.html',
                  {'technology_details': technology_details, 'details': details, 'user': user})


def blog_details(request, name, blog_id):
    details = Details.objects.filter(id=1).values('about', 'email', 'contact')
    s = str(request.user)

    if s == 'AnonymousUser':

        user = False

    else:
        user = User.objects.get(username=request.user.username)

    blog_details = BlogDetails.objects.filter(technology__name=name, pk=blog_id).values('id','technology__name',
                                                                                        'short_details', 'description',
                                                                                        'blog_details_photo',
                                                                                        'written_by')

    comment = BlogComments.objects.filter(blog_id=blog_id).order_by('-id').values('id', 'comments', 'user__username',
                                                                                  'created_at', 'like')[:15]

    return render(request, 'blogs/blog_details.html',
                  {'blog_details': blog_details, 'details': details, 'comment': comment, 'user': user})


@method_decorator(login_required, name='dispatch')
class BlogCreation(View):
    def get(self, request):
        form = BlogDetailsForm()
        return render(request, 'forms/addForm.html', {"form": form
                                                      })

    def post(self, request):
        post = request.POST.copy()
        user = User.objects.get(username=request.user.username)
        request.POST = post

        form = BlogDetailsForm(request.POST, request.FILES)

        if form.is_valid():
            new = form.save(commit=False)
            new.written_by= user

            new.save()

            return HttpResponseRedirect(reverse('records:dashboard'))
        else:

            return render(request, 'forms/addForm.html',
                          {"form": form, })


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('records:dashboard'))


@login_required
def save_comment(request, blog_id, comment):

        user = User.objects.get(username=request.user.username)
        pki = BlogComments.objects.create(blog_id=BlogDetails.objects.get(pk=blog_id), comments=comment, user=user)
        result = list(BlogComments.objects.filter(pk=pki.id).order_by('comments').values('id', 'comments', 'like',
                                                                                         'user__username',
                                                                                         'created_at'))

        result[0]['created_at'] = '0 min ago'

        return JsonResponse(result, safe=False)


@login_required
def increase_like(request, comm_id):
    like = BlogComments.objects.get(id=comm_id)

    if request.user.username in like.liked_user:
        like_no = BlogComments.objects.get(id=comm_id)
        print(like_no.like)
        like_count = like_no.like - 1
        user = like_no.liked_user.replace(request.user.username,"")
        like_no.like = like_count
        like_no.liked_user = user
        like_no.save()
        return JsonResponse(like_count, safe=False)

    else:
        like_no = BlogComments.objects.get(id=comm_id)
        print(like_no.like)
        users = like_no.liked_user
        like_count = like_no.like + 1
        like_no.like = like_count
        like_no.liked_user = users+","+request.user.username
        like_no.save()
        return JsonResponse(like_count, safe=False)
