from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponseRedirect
from models import Student
from sets import Set

class PersonForm(forms.Form):
	name = forms.CharField(max_length=100)
	labnum = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100, widget = forms.PasswordInput)
	
@csrf_exempt
def edit_person(request):
	labsDone = None
	allList = None
	badPass = False
	showPig = False
	if request.method == 'POST': # If the form has been submitted...
		form = PersonForm(request.POST) # A form bound to the POST data
		if request.POST['password'] == 'what':
			s = Student.objects.get(name=request.POST['name'])
			if request.POST['labnum'] == 'view':
				labsDone = s.labcos
			else:					
				labcos = list(Set([lab.strip() 
					for lab in s.labcos.split(',') + request.POST['labnum'].split(',')
					if lab != '']))
				s.labcos = ','.join(labcos)#final
				s.save()
				return HttpResponseRedirect(request.path) # Redirect after POST
		elif request.POST['password'] == 'showme':
			allList = Student.objects.all()
			for s in allList:
				s.labcos = ','.join(sorted(s.labcos.split(',')))
		elif request.POST['labnum'] == 'aitirocks':
			showPig = True
		else:
			badPass = True

	else:
		form = PersonForm() # An unbound form
			
	
	form.fields['name'].widget = forms.Select(
		choices = [(s.name, s.name) for s in Student.objects.all()])
	return render_to_response('checks/index.html', {
	'form': form, 'bad_pass': badPass, 'labsDone': labsDone, 'allList':allList, 'showPig':showPig
	})
