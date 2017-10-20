from django.shortcuts import render
from django.views import View
import random
from survey.forms import FormExperiment1Step1, FormExperiment1Step2
from django.urls import reverse
from django.shortcuts import redirect

class Experiment1Step1(View):
    def get(self, request):
        """
        Function to handle when a get request is done  (display the form to be filled)
        :param request:
        :return: Experiment1Step1 view containing the form
        """
        form = FormExperiment1Step1()
        return render(request, 'experiment1_step1.html', {'form': form})

    def post(self,request):
        """
        Function to handle when a post request is done, comming back from form submission.
        1.- Store the data in db
        2.- Redirect to next step (rankings1)
        :param request:
        :return: Redirectino rakings1
        """
        #TODO: Update data with the choice selected
        return redirect(reverse('experiment1ranking1'))

class Experiment1Step2(View):
    def get(self, request):
        """
        Function to handle when a get request is done  (display the form to be filled)
        :param request:
        :return: Experiment1Step1 view containing the form
        """
        form = FormExperiment1Step2()
        return render(request, 'experiment1_step2.html', {'form': form})

    def post(self,request):
        """
        Function to handle when a post request is done, comming back from form submission.
        1.- Store the data in db
        2.- Redirect to next step (rankings1)
        :param request:
        :return: Redirectino rakings1
        """
        #TODO: Update data with the choice selected
        return redirect(reverse('experiment1ranking1'))
