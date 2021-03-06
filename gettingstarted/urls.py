from django.urls import path, include

from django.contrib import admin
######################
from django.conf.urls.static import static # new
from django.conf import settings # new
admin.autodiscover()

import hello.views
import MyAppInWebsite.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("external/",hello.views.external,name="external"),
    path("",include('MyAppInWebsite.urls')),
		
	
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
