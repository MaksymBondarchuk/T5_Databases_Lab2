from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', 'webi.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^server', 'app.views.server'),
    url(r'^trigger_start', 'app.views.server_trigger_start'),
    url(r'^trigger_stop', 'app.views.server_trigger_stop'),
    url(r'^proc', 'app.views.server_stored_procedure'),
    url(r'^session1', 'app.views.server_execute'),
    url(r'^new_event', 'app.views.create_event'),
)