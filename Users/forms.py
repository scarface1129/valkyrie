from django import forms
from .models import Profile
# from profiles.tasks import sleepy

from django.contrib.auth import get_user_model
from .models import send_activation_email

User=get_user_model() 


class RegisterForm(forms.ModelForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = [

		        'username',
		         'email',
		         
		         ]
	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email__iexact=email)
		if qs.exists():
			raise forms.ValidationError('the Email Address Has Already been Used by Another User ')
		return email

	def clean_password2(self):
		# just checking if the two passwords match
		password1=self.cleaned_data.get('password1')
		password2=self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('Password dosent match!!!')
		return password2


	def save(self, commit=True):
		# saving the provided password in hashed format
		user=super(RegisterForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		user.is_active=False
		#creat a new user hash for activating email

		if commit:
			user.save()
			print(user)
			send_activation_email(user)
		return user		

from phonenumber_field.formfields import PhoneNumberField
class ProfileUpdate(forms.ModelForm):
    # phone_number = PhoneNumberField()
    class Meta:
        model = Profile 
        fields = [
            
            'full_name',
            'phone_number',
            'address',
			'media',
                    
        ]