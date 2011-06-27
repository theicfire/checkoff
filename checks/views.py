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
		if request.POST['password'] == 'pass':
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
		elif request.POST['password'] == 'showall':
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


'''
	for p in Student.objects.all():
		p.delete()

	mall = [['Aaron Nichie, All Python,DJ1,DJ5,dj2,dj3,dj4'],['Agana Agana-Nsiire, 1,2,3,4,5,8,9,10,dj1'],['Amaoko Radjwan, 1,2,3,4,5,6,7,9,10,dj1'],['Ansah Baidoo, 1,2,3,4,5,6,7,8,10,dj1'],['Ansah Felix Yaw, 1,2,3,4,5,6,7,8,9,10,11,dj1'],['Asante Kwadwo Okrah, All Python,DJ5,dj1,dj2,dj3,dj4'],['Asiedy Asante Bismark,2,3,4,5,08,DJ4,DJ5,dj1,dj2,dj3'],['ATSO YAO NELSON, 7b,All Python,DJ1,DJ5,dj2,dj3,dj4'],['Attuquayefio Rodney N.K, All Python,DJ1,DJ2,dj1,dj3,dj4'],['Barbara Gyasi, 1,2,3,4,5,6,7,8,9,10,11,dj2,dj3'],['CYNTHIA OWUSU, 1,2,3,4,5,6,8,9,10,DJ1,DJ4,dj2,dj3'],['Fleischer Paul Benjamin Spurgeon, All Python,DJ1,DJ2,DJ3,DJ6,dj4,dj5'],['Kafu Adabunu, 1,2,3,4,5,6,8,9,10,dj1'],['Kwadwo Boateng Ofori Amanfo, All Python,dj1,dj2,dj3,dj4,dj5'],['Kwame Asiedu Owusu Afram, All Python,DJ2,DJ5,DJ6,dj3,dj4'],['Kwame Nseboah Nyarko, All Python,DJ5,dj1,dj2,dj3,dj4'],['Kwasi Kwakye Adomako, 1,2,3,4,5,6a,7,8,9,10,11,dj1,dj2,dj3,dj4,dj5'],['Lady-Asaph Lamptey, All Python,DJ2,dj1,dj3,dj4,dj5,dj6'],['Lartey Louis-Mark, All Python,DJ2,DJ5,dj1,dj3,dj4'],['Moses Amoaso Kwesi Acquah, All Python,DJ2,DJ3,DJ4,dj1,dj5'],['Naa Kai Koney, 1,2,3,4,5,6,7a,8,9,10,11,DJ1'],['Odame Agyapong, 1,2,3,4,5,6,7a,8,9,10,dj1'],['OPPONG KYEREMANTENG, All Python,DJ1,DJ5,dj2,dj3,dj4,dj5,dj6'],['Owusu-Boakye Kwame Okyere, All Python,DJ1,DJ3,DJ4,DJ5,DJ6,dj2'],['Richard Kojo Ghartey, 1,2,3,4,5,7,8,10,DJ2,DJ3,DJ4'],['sarpong kwadwo asare, 1,2,3,4,5,6,7a,8,9,10,DJ1,DJ2,DJ5,dj3,dj4'],['SELASE NEWTON KRAKANI, 1,2,3,4,5,6,7,8,9,10,11,DJ1,DJ3,DJ5,dj2,dj4,dj6']]
	for p in mall:
		print 'go',
		x = [a.strip().lower() for a in p[0].split(',')]
		name = x[0]
		print name, 
		labs = x[1:]
		if len(Student.objects.filter(name=name)) == 0:
			print 'start make'
			per = Student(name=name, labcos=','.join(labs))
			per.save()
'''
