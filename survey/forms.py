from django import forms

GENDER_CHOICES = (
    ('A', 'Male'),
    ('B', 'Female'),
    ('C', 'Other'),
)

DEGREE_CHOICES = (
    ('A', 'Less than high school'),
    ('B', 'High school graduate, diploma or the equivalent'),
    ('C', 'Bachelor\'s degree'),
    ('D', 'Master\'s degree'),
    ('E', 'Professional degree'),
    ('F', 'Doctorate degree'),
    ('G', 'Other'),
)


class PersonalDataForm(forms.Form):
    gender = forms.ChoiceField(label='What is your gender?', widget=forms.RadioSelect, choices=GENDER_CHOICES)
    age = forms.IntegerField(label='What is your age?')
    highest_degree = forms.ChoiceField(
        label='What is the highest degree or level of school you have completed? If currently enrolled, highest degree received',
        widget=forms.RadioSelect, choices=DEGREE_CHOICES)
