from django.contrib import admin
from django.urls import path, include
from lms_core.views import stats_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lmscore/', include('lms_core.urls')),
    path('lmscore/stats/', stats_view, name='stats'),
]
