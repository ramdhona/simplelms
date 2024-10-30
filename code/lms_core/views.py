# lms_core/views.py
from django.shortcuts import render
from django.db import models  # Impor models dari django.db
from lms_core.models import Course  # Pastikan model Course diimpor
from django.contrib.auth.models import User  # Impor model User

def stats_view(request):
    total_users = User.objects.count()  # Total Users
    total_users_without_courses = User.objects.filter(courses__isnull=True).count()  # Total Users Without Courses
    average_courses_per_user = Course.objects.values('creator').distinct().count()  # Rata-rata Courses per User

    # User dengan jumlah course terbanyak
    most_courses_user = User.objects.annotate(course_count=models.Count('courses')).order_by('-course_count').first()
    
    # List users tanpa course
    users_without_courses = User.objects.filter(courses__isnull=True)

    context = {
        'total_users': total_users,
        'total_users_without_courses': total_users_without_courses,
        'average_courses_per_user': average_courses_per_user,
        'most_courses_user': most_courses_user,
        'users_without_courses': users_without_courses,
    }
    
    return render(request, 'lms_core/stats.html', context)
