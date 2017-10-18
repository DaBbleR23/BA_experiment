from django.conf.urls import url

from . import views
from .views.index_view import IndexView
urlpatterns = [
    url(r'^$', IndexView.as_view()),
]
