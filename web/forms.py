from django import forms

from .models import Post
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

TYPE_OF_BUSINESS_CHOICES= [
    ('Sole Proprietorship', 'Sole Proprietorship'),
    ('Partnership', 'Partnership'),
    ('Corporation', 'Corporation'),
    ('Benefit corporation', 'Benefit corporation'),
    ('L3C', 'L3C'),
    ('S corporation', 'S corporation'),
    ('C corporation', 'C corporation'),
    ('LLP', 'LLP'),
    ('Series LLC', 'Series LLC'),
    ('Limited Liability Company (LLC)', 'Limited Liability Company (LLC)'),
    ]
BG_TEMPLATES = [
    ('media/TemplateFiles/1.jpg','Shiny White'),
    ('media/TemplateFiles/2.jpg','Pinky Blue'),
    ('media/TemplateFiles/3.jpg','Glassy Yellow'),
    ('media/TemplateFiles/4.jpg','Glossy Pink'),
    ('media/TemplateFiles/5.jpg','OrBlack'),
    ('media/TemplateFiles/6.jpg','Blue'),
    ('media/TemplateFiles/7.jpg','Colourful'),
    ('media/TemplateFiles/8.jpg','Dark'),
    ('media/TemplateFiles/9.jpg','PurpleOrange'),
    ('media/TemplateFiles/10.jpg','Rainbow'),
]
    
class PostForm(forms.ModelForm):
    #phone_number = PhoneNumberField()
    #phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget())
    #phone_number = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': 'Phone'}),label="Phone number", required=False)
    email=forms.EmailField(required=True)
    btype= forms.CharField(label='Type of Business', widget=forms.Select(choices=TYPE_OF_BUSINESS_CHOICES))
    bgtemplate= forms.CharField(label='Choose a Background Template', widget=forms.Select(choices=BG_TEMPLATES))
    address= forms.CharField(label='Address')
    
    class Meta:
        model = Post
        fields = ['title','btype','email','phone_number', 'content','address','bgtemplate']

        widgets = {
            'phone_number': PhoneNumberPrefixWidget(attrs={'class': 'form-control','placeholder': 'Contact'},initial='IN'),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Details'}),
        }

