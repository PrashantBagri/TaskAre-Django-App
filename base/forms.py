from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import newUser, Task

class taskForm(forms.ModelForm):
    class Meta :
        model = Task
        fields = ["title", "targetDate", "description"]
        labels = {
            'title' : 'Task',
            'targetDate' : 'Target Date',
            'description' : 'Description',          
        }
        widgets = {
            'title': forms.TextInput(attrs={'class':"outline outline-2 w-[250px] h-[30px] rounded-full p-5 text-sm"}),
            'targetDate': forms.DateInput(attrs={'class':"outline outline-2 w-[250px] h-[30px] rounded-full p-5 text-sm"}),
            'description' : forms.TextInput(attrs={'class':'outline outline-2 w-[250px] h-[30px] rounded-full p-5 text-sm'})
        }
        
class userRegister(forms.ModelForm):
    class Meta:
        model = newUser
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        labels = {
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'email' : 'Email',
            'username' : 'Username',
            'password': 'Password'            
        }
        help_texts = {
            'username' : None
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':"outline outline-2 w-[250px] h-[30px] rounded-full p-5 text-sm"}),
            'last_name': forms.TextInput(attrs={'class':"outline outline-2 w-[250px] h-[30px] rounded-full p-5 text-sm"}),
            'email' : forms.EmailInput(attrs={'class':'outline outline-2 w-[250px] h-[30px] rounded-full p-5 text-sm'}),
            'username' : forms.TextInput(attrs={'class':'outline outline-2 w-[250px] h-[30px] rounded-full p-5 text-sm'}),
            'password' : forms.PasswordInput(attrs={'class': 'outline outline-2 w-[250px] h-[30px] rounded-full p-5 text-sm'})
        }