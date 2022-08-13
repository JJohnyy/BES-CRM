from django import forms
from django.contrib.auth import get_user_model
from .models import Lead, Category
from django.contrib.auth.forms import UserCreationForm, UsernameField


User = get_user_model()


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'address',
            'phone',
            'email',
            'description',
            'agent',
        )
    def phone_validation(self):
        phone = 'phone'
        try self.cleaned_data.get.int((userInput)):
            pass
        else ValueError:
            raise forms.ValidationError('Phone must be a valid phone number')



class LeadForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    age = forms.IntegerField(min_value=0)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'name',
        )


class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'category',
        )
