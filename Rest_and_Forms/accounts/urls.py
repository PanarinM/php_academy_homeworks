from django.conf.urls import url

from accounts.views import log_in, log_out, register

urlpatterns = [
    url(r'^login/$', log_in, name="login"),
    url(r'^logout/$', log_out, name="logout"),
    url(r'^register/$', register, name="register"),
]
