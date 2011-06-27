from django.conf.urls.defaults import *
 
import views
 
urlpatterns = patterns('', 
 
    url(r'^$', 'checks.views.edit_person'),
)
