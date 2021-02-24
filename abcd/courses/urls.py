from django.urls import path
from .views import course_upload,course_list,video_upload,course_video

app_name = 'Course'

urlpatterns = [
    path('course_upload/',course_upload,name='course_upload'),
    path('course_list/',course_list,name='course_list'),
    path('video_upload/',video_upload,name='video_upload'),
    path('course_video/<int:pk>/',course_video,name='course_video'),
]