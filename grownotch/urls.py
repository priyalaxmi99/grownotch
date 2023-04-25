"""grownotch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.site.site_header = " Grownotch Admin"
admin.site.site_title = " Grownotch Admin Portal"
admin.site.index_title = "Welcome to Grownotch Admin Portal"


from webapp import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index, name = "index"),
    path('index.html', v.index, name = "index1"),
    path('aboutus.html', v.about, name = "about"),
    path('local-seo.html', v.localseo, name = "localseo"),
    path('search-engine-optimization.html', v.globalseo, name = "globalseo"),
    path('content-writing.html', v.content, name = "content"),
    path('online-reputation-management.html', v.orm, name = "orm"),
    path('digital-marketing.html', v.dm, name = "dm"),
    path('web-design.html', v.web, name = "web"),
    path('social-media-marketing.html', v.smm, name = "smm"),
    path('pay-per-click-marketing.html', v.ppc, name = "ppc"),
    path('testmonials.html', v.testi, name = "testi"),
    path('contactus.html', v.contact, name = "contact"),
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)