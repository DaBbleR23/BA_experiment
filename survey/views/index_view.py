from django.shortcuts import render
from django.views import View

from survey.forms import PersonalDataForm


class IndexView(View):
    def get(self, request):
        form = PersonalDataForm()
        return render(request, 'index.html', {'form': form})
