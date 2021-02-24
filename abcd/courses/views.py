from django.shortcuts import render,redirect
from .forms import CourseForm,UserForm,Video_form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Course,Video
# Create your views here.

@login_required()
def course_upload(request):
    if request.method == 'POST':
        u_form = UserForm(request.POST or None,instance=request.user)
        c_form = CourseForm(request.POST or None, request.FILES or None)
        if u_form.is_valid() and c_form.is_valid():
            u_form.save()
            c_form.save()
            messages.success(request,'Course uploaded successfully')
            return redirect('Home:home')
        else:
            messages.error(request,'Please orrect the error below')
    else:
        u_form = UserForm(instance=request.user)
        c_form = CourseForm()
    template = 'course/course_upload.html'
    return render(request,template,{'u_form':u_form,'c_form':c_form})


def course_list(request):
    template = 'course/course_list.html'
    course = Course.objects.all()
    return render(request,template,{'courses':course})



@login_required()
def video_upload(request):
    if request.method == 'POST':
        v_form = Video_form(request.POST or None, request.FILES or None)
        if v_form.is_valid():
            v_form.save()
            messages.success(request,'Video uploaded successfully')
            return redirect('Home:home')
        else:
            messages.error(request,'Please correct the error below')
    else:
        v_form = Video_form()
    template = 'course/video_upload.html'
    return render(request,template,{'v_form':v_form})


def course_video(request,pk):
    template = 'course/course_videos.html'
    video = Video.objects.filter(pk=pk)
    return render(request,template,{'videos':video})


