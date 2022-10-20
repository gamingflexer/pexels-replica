from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from home.models import Post
from django.forms import ModelForm

class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))

class Meta:
    model = User 
    field = ['User', 'email', 'password1', 'password2']
    labels = {'email': 'Email'}
    widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}
    
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

class MypasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Old Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus':True,'class':'form-control'}))
    new_password1 = forms.CharField(label=("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}))
    

# define the class of a form
class PostForm(ModelForm):
	class Meta:
		# write the name of models for which the form is made
		model = Post	

		# Custom fields
		fields =["username", "gender", "text"]

	# this function will be used for the validation
	def clean(self):

		# data from the form is fetched using super function
		super(PostForm, self).clean()
		
		# extract the username and text field from the data
		username = self.cleaned_data.get('username')
		text = self.cleaned_data.get('text')

		# conditions to be met for the username length
		if len(username) < 5:
			self._errors['username'] = self.error_class([
				'Minimum 5 characters required'])
		if len(text) <10:
			self._errors['text'] = self.error_class([
				'Post Should Contain a minimum of 10 characters'])

		# return any errors if found
		return self.cleaned_data
