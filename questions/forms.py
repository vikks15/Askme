from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError

class AskForm(forms.Form):
	title = forms.CharField(
		widget=forms.TextInput (
			attrs = {'class': 'form-control' }
			)
		)
	text = forms.CharField(
		widget=forms.Textarea (
			attrs = {'class': 'form-control' }
			)
		)

	tags = forms.CharField(
		widget=forms.Textarea (
			attrs = {'class': 'form-control' }
			)
		)
	
	def clean(self):
		title = self.cleaned_data.get('title')
		text = self.cleaned_data.get('text')
		tags = self.cleaned_data.get('tags')
		
		# if len(title) > 64:
		# 	raise ValidationError('Sorry, maximum size of question title is 64 symbols!')
		# return user
		return

class AnswerForm (forms.ModelForm):
	class Meta:
		model = Answer
		fields = ('title', 'text',)
		#fields = ['text']
		#widgets = {
		#'text':forms.Textarea(attrs={
		#	'class':'form-control',
		#	'rows': 5,
		#	'placeholder':'Write your answer'
		#	})
		#}

	#text = forms.CharField(
	#	widget=forms.Textarea (
	#		attrs = {'class': 'form-control' }
	#		)
	#	)

class SignInForm(AuthenticationForm):
	username = forms.CharField(
		widget=forms.TextInput ( attrs = {
			'class': 'form-control',
			'placeholder': 'Login'
		}))
	password = forms.CharField(
		widget=forms.PasswordInput ( attrs = {
			'class': 'form-control',
			'placeholder': 'Password'
		}))

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		if not user or not user.is_active:
			raise ValidationError('Error in username or password. User does not exist.')
		return user
	
	def login(self, request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		return user

	class Meta:
		model = Profile
		fields = ('username', 'password')
		widgets = {
      		'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Login'}),
      		'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
		}

class RegisterForm(forms.Form):
	login = forms.CharField(
		widget=forms.TextInput (
			attrs = {'class': 'form-control' }
			)
		)
	email = forms.CharField(
		widget=forms.TextInput (
			attrs = {'class': 'form-control' }
			)
		)
	password = forms.CharField(
		widget=forms.TextInput (
			attrs = {'class': 'form-control' }
			)
		)
	repeatpass = forms.CharField(
		widget=forms.TextInput (
			attrs = {'class': 'form-control' }
			)
		)


class SettingsFormUser(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name')
		widgets = {
      		'username': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.TextInput(attrs={'class': 'form-control'}),
			'first_name': forms.TextInput(attrs={'class': 'form-control'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control'}),
		}

class SettingsFormProfile(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('avatar', )
		widgets = {
      		'avatar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Login'}),
		}