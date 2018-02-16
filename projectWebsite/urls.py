from django.conf.urls import url
from . import views
from projectWebsite.views import home_view, about_view, features_view, fake_view, true_view

urlpatterns = [
    url(r'^$', home_view.as_view(), name='projectWebsite'),
    url(r'home', home_view.as_view(), name='projectWebsite'),
    url('about', about_view.as_view(), name='projectWebsite'),
    url('features', features_view.as_view(), name='projectWebsite'),
    url('fake', fake_view.as_view(), name='projectWebsite'),
    url('true', true_view.as_view(), name='projectWebsite'),

]
