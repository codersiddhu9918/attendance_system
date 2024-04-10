from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import faculty_login
from student.models import students
from student.models import present
from datetime import date


# Create your views here.
def faculty(request):
	if request.session.get('fuser'):
		return redirect('home')
	else:
		return render(request,'faculty.html')
	
	
def flogin(request):
	fuser = request.POST['fuser']
	fpass = request.POST['fpass']
	
	res = faculty_login.objects.filter(fuser=fuser,fpass=fpass)
	
	if len(res)==1:
		request.session['fuser'] = res[0].fuser
		return redirect('home')
	else:
		return render(request,'faculty.html',{'error':'Username or Password Incorrect!!!'})
		
def home(request):
	if request.session.get('fuser'):
		return render(request,'home.html')
	else:
		return redirect('/faculty/')
		
def logout(request):
	del request.session['fuser']
	return redirect('/faculty/')
	
def account(request):
	if request.session.get('fuser'):
		return render(request,'account.html')
	else:
		return redirect('/faculty/')
		
def create_account(request):
	rollno = request.POST['rollno']
	sname = request.POST['sname']
	spass = request.POST['spass']
	
	res = students.objects.filter(rollno=rollno)
	
	if len(res)>0:
		return render(request,'account.html',{'msg':'Student already exists with this roll no.!!!'})
	else:
		q = students(rollno=rollno, sname=sname, spass=spass)
		q.save()
		
		return render(request,'account.html',{'msg':'Account Created Successfully!!!'})

def update_att(request):
	if request.session.get('fuser'):
		res = students.objects.all()
		return render(request,'attend.html',{'res':res})
	else:
		return redirect('/faculty/')

def up_attend(request):
	id = request.POST.getlist('att')
	pdate = date.today()
	
	ck = present.objects.filter(adate=pdate)
	
	if len(ck)>0:
		k = present.objects.get(adate=pdate)
		k.s_ids = id
		k.save()
		return render(request,'home.html',{'info':"Today's attendance is updated!!! "})
	else:
		inq = present(adate=pdate, s_ids=id)
		inq.save()
		return render(request,'home.html',{'info':"Today's attendance is created!!! "})

def chk_att(request):
	res = present.objects.all().order_by('-id')
	return render(request,'chk_att.html',{'res':res})

def chk_present(request):
	chk_date = request.GET['d']
	
	res = present.objects.filter(adate=chk_date)
	k = res[0].s_ids
	k = eval(k)
	
	d = []
	for i in k:
		o = students.objects.filter(id=int(i))
		data = o[0]
		d.append(data)
	
	if len(res)>0:
		return render(request,'chk_present.html',{'data':d})
	else:
		return HttpResponse("Wrong Date!!!")
