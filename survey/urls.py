from django.conf.urls import url

from . import views
from .views.index_view import IndexView
from .views.experiment1 import Experiment1Step1, Experiment1Step2, Experiment1Step3
from .views.experiment2 import Experiment2Step1, Experiment2Step2

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='survey'),
    url(r'experiment1/$', Experiment1Step1.as_view(), name='experiment1'),
    url(r'experiment1/ranking1$', Experiment1Step2.as_view(), name='experiment1ranking1'),
    url(r'experiment1/submissionchange$', Experiment1Step3.as_view(), name='experiment1submissionchange'),

    url(r'experiment2/$', Experiment2Step1.as_view(), name='experiment2'),

]
