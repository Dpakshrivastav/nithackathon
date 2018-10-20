from django.conf.urls import url
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'coolie/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^$', views.home, name='home'),
    url(r'^reserve/$', views.reserve, name='reserve'),
    url(r'^destination/$', views.destination, name='destination'),
<<<<<<< HEAD
    url(r'^(?P<coolie_id>[0-9]+)/$', views.profile, name='profile')
=======
    url(r'^(?P<pk>[0-9]+)/$', views.profile, name='profile')
>>>>>>> de45a63f82ee259d1250267d18c0945aae8ebee7

]