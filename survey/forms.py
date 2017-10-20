from django import forms
from django.forms.widgets import NumberInput, Widget

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

INDUSTRY_CHOICES = (
    (1, 'Accounting'),
    (2, 'Airlines / Aviation'),
    (3, 'Alternative Dispute Resolution'),
    (4, 'Alternative Medicine'),
    (5, 'Animation'),
    (6, 'Apparel & Fashion'),
    (7, 'Architecture & Planning'),
    (8, 'Arts & Crafts'),
    (9, 'Automotive'),
    (10, 'Aviation & Aerospace'),
    (11, 'Banking'),
    (12, 'Biotechnology'),
    (13, 'Broadcast Media'),
    (14, 'Building Materials'),
    (15, 'Business Supplies & Equipment'),
    (16, 'Capital Markets'),
    (17, 'Chemicals'),
    (18, 'Civic & Social Organization'),
    (19, 'Civil Engineering'),
    (20, 'Commercial Real Estate'),
    (21, 'Computer & Network Security'),
    (22, 'Computer Games'),
    (23, 'Computer Hardware'),
    (24, 'Computer Networking'),
    (25, 'Computer Software'),
    (26, 'Construction'),
    (27, 'Consumer Electronics'),
    (28, 'Consumer Goods'),
    (29, 'Consumer Services'),
    (30, 'Cosmetics'),
    (31, 'Dairy'),
    (32, 'Defense & Space'),
    (33, 'Design'),
    (34, 'Education Management'),
    (35, 'E-Learning'),
    (36, 'Electrical / Electronic Manufacturing'),
    (37, 'Entertainment'),
    (38, 'Environmental Services'),
    (39, 'Events Services'),
    (40, 'Executive Office'),
    (41, 'Facilities Services'),
    (42, 'Farming'),
    (43, 'Financial Services'),
    (44, 'Fine Art'),
    (45, 'Fishery'),
    (46, 'Food & Beverages'),
    (47, 'Food Production'),
    (48, 'Fund-Raising'),
    (49, 'Furniture'),
    (50, 'Gambling & Casinos'),
    (51, 'Glass, Ceramics & Concrete'),
    (52, 'Government Administration'),
    (53, 'Government Relations'),
    (54, 'Graphic Design'),
    (55, 'Health, Wellness & Fitness'),
    (56, 'Higher Education'),
    (57, 'Hospital & Health Care'),
    (58, 'Hospitality'),
    (59, 'Human Resources'),
    (60, 'Import & Export'),
    (61, 'Individual & Family Services'),
    (62, 'Industrial Automation'),
    (63, 'Information Services'),
    (64, 'Information Technology & Services'),
    (65, 'Insurance'),
    (66, 'International Affairs'),
    (67, 'International Trade & Development'),
    (68, 'Internet'),
    (69, 'Investment Banking'),
    (70, 'Investment Management'),
    (71, 'Judiciary'),
    (72, 'Law Enforcement'),
    (73, 'Law Practice'),
    (74, 'Legal Services'),
    (75, 'Legislative Office'),
    (76, 'Leisure, Travel & Tourism'),
    (77, 'Libraries'),
    (78, 'Logistics & Supply Chain'),
    (79, 'Luxury Goods & Jewelry'),
    (80, 'Machinery'),
    (81, 'Management Consulting'),
    (82, 'Maritime'),
    (83, 'Market Research'),
    (84, 'Marketing & Advertising'),
    (85, 'Mechanical or Industrial Engineering'),
    (86, 'Media Production'),
    (87, 'Medical Devices'),
    (88, 'Medical Practice'),
    (89, 'Mental Health Care'),
    (90, 'Military'),
    (91, 'Mining & Metals'),
    (92, 'Motion Pictures & Film'),
    (93, 'Museums & Institutions'),
    (94, 'Music'),
    (95, 'Nanotechnology'),
    (96, 'Newspapers'),
    (97, 'Non-Profit Organization Management'),
    (98, 'Oil & Energy'),
    (99, 'Online Media'),
    (100, 'Outsourcing / Offshoring'),
    (101, 'Package / Freight Delivery'),
    (102, 'Packaging & Containers'),
    (103, 'Paper & Forest Products'),
    (104, 'Performing Arts'),
    (105, 'Pharmaceuticals'),
    (106, 'Philanthropy'),
    (107, 'Photography'),
    (108, 'Plastics'),
    (109, 'Political Organization'),
    (110, 'Primary / Secondary Education'),
    (111, 'Printing'),
    (112, 'Professional Training & Coaching'),
    (113, 'Program Development'),
    (114, 'Public Policy'),
    (115, 'Public Relations & Communications'),
    (116, 'Public Safety'),
    (117, 'Publishing'),
    (118, 'Railroad Manufacture'),
    (119, 'Ranching'),
    (120, 'Real Estate'),
    (121, 'Recreational Facilities & Services'),
    (122, 'Religious Institutions'),
    (123, 'Renewables & Environment'),
    (124, 'Research'),
    (125, 'Restaurants'),
    (126, 'Retail'),
    (127, 'Security & Investigations'),
    (128, 'Semiconductors'),
    (129, 'Shipbuilding'),
    (130, 'Sporting Goods'),
    (131, 'Sports'),
    (132, 'Staffing & Recruiting'),
    (133, 'Supermarkets'),
    (134, 'Telecommunications'),
    (135, 'Textiles'),
    (136, 'Think Tanks'),
    (137, 'Tobacco'),
    (138, 'Translation & Localization'),
    (139, 'Transportation / Trucking / Railroad'),
    (140, 'Utilities'),
    (141, 'Venture Capital & Private Equity'),
    (142, 'Veterinary'),
    (143, 'Warehousing'),
    (144, 'Wholesale'),
    (145, 'Wine & Spirits'),
    (146, 'Wireless'),
    (147, 'Writing & Editing'),
)

EXPERIMENT1_STEP1_INVESTMENTS_CHOICES = (
    ('1','Facebook Advertising'),
    ('2','Google AdWords')
)

EXPERIMENT1_STEP3_SUBMISSION_CHANGE = (
    ('1','YES'),
    ('2','NO')
)

class RangeInput(NumberInput):
    input_type = 'range'


class FormPersonalDataForm(forms.Form):
    gender = forms.ChoiceField(label='What is your gender?', widget=forms.RadioSelect, choices=GENDER_CHOICES)
    age = forms.IntegerField(label='What is your age?')
    highest_degree = forms.ChoiceField(
        label='What is the highest degree or level of school you have completed? If currently enrolled, highest degree received',
        widget=forms.RadioSelect, choices=DEGREE_CHOICES)
    industry = forms.ChoiceField(label='Which industry do you work in or are most involved with?',
                                 widget=forms.Select, choices=INDUSTRY_CHOICES)
    digital_competence = forms.ChoiceField(label='Rank your level of competence in digital marketing',
                              widget=RangeInput(attrs={'step':1, 'min':0, 'max': 100}))


class FormExperiment1Step1(forms.Form):
    channel_to_invest = forms.ChoiceField(label='', widget=forms.RadioSelect, choices=EXPERIMENT1_STEP1_INVESTMENTS_CHOICES)

class FormExperiment1Step2(forms.Form):
    intuition = forms.ChoiceField(label='Intuition',
                              widget=RangeInput(attrs={'step':1, 'min':0, 'max': 100}))
    knowledge = forms.ChoiceField(label='Knowledge',
                              widget=RangeInput(attrs={'step':1, 'min':0, 'max': 100}))
    information = forms.ChoiceField(label='Information gather from other sources',
                              widget=RangeInput(attrs={'step':1, 'min':0, 'max': 100}))

class FormExperiment1Step3(forms.Form):
    submission_change = forms.ChoiceField(label='Would you like to change your submission?', widget=forms.RadioSelect, choices=EXPERIMENT1_STEP3_SUBMISSION_CHANGE)