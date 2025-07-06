"""
URL configuration for dj_lesson project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static

from dj_lesson import settings
from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include

from lesson_1.views import func_page_not_found

# from lesson_1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lesson_1.urls')),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = func_page_not_found

admin.site.site_header = "Моя админка"
admin.site.index_title = "Известные женщины мира"