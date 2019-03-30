from django.shortcuts import render
from .models import Student
from .forms import studentForm
# Create your views here.
def register(request):
	s1=studentForm()
	data={"student":s1}
	return render(request,'app2/register.html',data)
def login(request):
	return render(request,'app2/login.html')	
