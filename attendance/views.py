from django.shortcuts import render
from principal.models import principal_login

# Create your views here.
def index(request):
	return render(request,'index.html')

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


