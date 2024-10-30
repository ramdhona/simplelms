from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Count
from lms_core.models import Course  # Ganti 'your_app' dengan nama aplikasi Anda

def stats_view(request):
    # Menghitung statistik
    total_users = User.objects.count()
    total_courses = Course.objects.count()
    users_with_courses = User.objects.filter(course__isnull=False).distinct().count()
    users_without_courses = total_users - users_with_courses
    average_courses_per_user = total_courses / total_users if total_users > 0 else 0
    most_courses_user = User.objects.annotate(course_count=Count('course')).order_by('-course_count').first()

    context = {
        'total_users': total_users,
        'users_without_courses': users_without_courses,
        'average_courses_per_user': average_courses_per_user,
        'most_courses_user': most_courses_user,
        'users_with_no_courses': User.objects.filter(course__isnull=True),
    }
    
    return render(request, 'lms_core/stats.html', context)
