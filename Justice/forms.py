from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField

class ProfileForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)

		self.fields['is_valid'].disabled = True
		self.fields['username'].help_text = False

	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'is_valid']


class SignupForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'phone_number']