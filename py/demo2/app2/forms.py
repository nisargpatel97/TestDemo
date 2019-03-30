from django.forms import ModelForm
from .models import *

class studentForm(ModelForm):
	class Meta:
		model=Student
		fields=['name','sid']
