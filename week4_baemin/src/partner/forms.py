from django.forms import TextInput, Textarea, ModelForm
from .models import Partner, Menu

class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields = (
            "name",
            "contact",
            "address",
            "description",
        )
        widgets = {
            'name': TextInput(attrs={"class":"form-control"}),
            'contract': TextInput(attrs={"class":"form-control"}),
            'address': TextInput(attrs={"class":"form-control"}),
            'description': Textarea(attrs={"class":"form-control"}),
        }

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = (
            "image",
            "menu_name",
            "price",
        )

        widgets = {
            #'image': TextInput(attrs={"class":"form-control"}),
            'menu_name': TextInput(attrs={"class":"form-control"}),
            'price': TextInput(attrs={"class":"form-control"}),
        }
