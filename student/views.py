from django.shortcuts import render,redirect,HttpResponse
from .models import students
from .models import present

# Create your views here.
def student(request):
	if request.session.get('rollno'):
		return redirect('shome')
	else:
		return render(request,'student.html')
	
def slogin(request):
	rollno = request.POST['rollno']
	spass = request.POST['spass']
	
	res = students.objects.filter(rollno=rollno, spass=spass)
	
	if len(res)==1:
		request.session['rollno'] = res[0].rollno
		return redirect('shome')
	else:
		return render(request,'student.html',{'error':'Roll no or Password incorrect!!!'})

def shome(request):
	if request.session.get('rollno'):
		return render(request,'shome.html')
	else:
		return redirect('/student/')
		
def slogout(request):
	if request.session.get('rollno'):
		del request.session['rollno']
		return redirect('/student/')
	return redirect('/student/')
	
def s_chk_att(request):
	if request.session.get('rollno'):
		res = present.objects.all().order_by('-id')
		return render(request,'s_chk_att.html',{'res':res})
	return redirect('/student/')
	
def chk_present(request):
	if request.session.get('rollno'):
		chk_date = request.GET['d']

		res = present.objects.filter(adate=chk_date)
		k = res[0].s_ids
		k = eval(k)

		d = []
		for i in k:
			o = students.objects.filter(id=int(i))
			data = o[0]
			d.append(data)

		if len(res) > 0:
			return render(request, 's_chk_present.html', {'data': d})
		else:
			return HttpResponse("Wrong Date!!!")
	return redirect('/student/')



	
	
	
	