from django.shortcuts import render
from django.views import View
import random
from survey.forms import FormPersonalDataForm
from django.urls import reverse
from django.shortcuts import redirect

class IndexView(View):
    def get(self, request):
        """
        Function to handle when a get request is done  (display the form to be filled)
        :param request:
        :return: Index view containing the form
        """
        form = FormPersonalDataForm()
        return render(request, 'index.html', {'form': form})

    def post(self,request):
        """
        Function to handle when a post request is done, comming back from form submission.
        1.- Store the data in db
        2.- Redirect to a random experiment
        :param request:
        :return: Redirectino to a random experiment
        """
        #TODO: Create an uniqueid for each user
        #TODO: Store info in the Database
        experiment = self.__get_random_experiment()
        return redirect(experiment)

    def __get_random_experiment(self):
        """
        Get a random experiment view among the ones in the experiment list
        :return: One randomly picked experiment
        """
        experiments = [reverse('experiment1'), reverse('experiment1')]
        return random.choice(experiments)