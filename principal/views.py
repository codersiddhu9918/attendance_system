from django.shortcuts import render,redirect
from .models import principal_login
from faculty.models import  faculty_login
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def principal(request):
    if request.session.get('puser'):
        return redirect('principal_home')
    else:
        return render(request, 'principal.html')


def plogin(request):
    puser = request.POST['puser']
    ppass = request.POST['ppass']

    res = principal_login.objects.filter(puser=puser, ppass=ppass)

    if len(res) == 1:
        request.session['puser'] = res[0].puser
        return redirect('principal_home')
    else:
        return render(request, 'principal.html', {'error': 'Username or Password Incorrect!!!'})


def principal_home(request):
	if request.session.get('puser'):
		return render(request,'principal_home.html')
	else:
		return redirect('/principal/')


def create_faculty_account(request):
    if request.session.get('puser'):
        fuser = request.POST['fname']
        fpass = request.POST['fpass']

    # res = faculty.objects.filter(fname=fuser)

    # if len(res) > 0:
    #     return render(request, 'account.html', {'msg': 'Student already exists with this roll no.!!!'})
        q = faculty_login(fuser=fuser, fpass=fpass)
        q.save()
        return render(request, 'faculty_account.html', {'msg': 'Account Created Successfully!!!'})
    return redirect('/principal/')
def account(request):
	if request.session.get('puser'):
		return render(request,'faculty_account.html')
	else:
		return redirect('/principal/')


def logout(request):
    if request.session.get('puser'):
        del request.session['puser']
        return redirect('/principal/')
    return redirect('/principal/')


def principal_account(request):
	return render(request,'principal_auth.html')

def principal_auth(request):
	fuser = request.POST['fname']
	fpass = request.POST['fpass']

	# res = faculty.objects.filter(fname=fuser)

	# if len(res) > 0:
	#     return render(request, 'account.html', {'msg': 'Student already exists with this roll no.!!!'})
	q = principal_login(puser=fuser, ppass=fpass)
	q.save()
	return render(request,'index.html',{'msg': 'Account Created Successfully!!!'})


