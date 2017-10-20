from django.shortcuts import render
from django.views import View
import random
from survey.forms import FormExperiment1Step1, FormExperiment1Step2, FormExperiment1Step3
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
        return redirect(reverse('experiment1submissionchange'))

class Experiment1Step3(View):
    def get(self, request):
        """
        Function to handle when a get request is done  (display the form to be filled)
        :param request:
        :return: Experiment1Step1 view containing the form
        """
        form = FormExperiment1Step3()
        messages = ['Facebook Advertising will bring you 10% more customers', 'Google AdWords will bring you 10% more customers']

        return render(request, 'experiment1_step3.html', {'form': form, 'message':random.choice(messages)})

    def post(self,request):
        """
        Function to handle when a post request is done, comming back from form submission.
        1.- Store the data in db
        2.- Redirect to next step (rankings1)
        :param request:
        :return: Redirectino rakings1
        """

        if form.is_valid():
            change = form.cleaned_data['submission_change']
            if change == '1':
                #TODO: Update data with the choice selected
                return redirect(reverse('experiment1'))
            else:
                return redirect(reverse('experiment1feedback'))
