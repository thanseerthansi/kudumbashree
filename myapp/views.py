from django.shortcuts import render
from myapp.models import *
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.contrib.auth import logout
def home(request):
	return render(request,'home/index.html')
def contact(request):
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		subject=request.POST['subject']
		message=request.POST['message']
		a=con(name=name,email=email,subject=subject,message=message)
		a.save()
		return HttpResponseRedirect('/contact/')


	return render(request,'home/contact.html')
def about(request):
	return render(request,'home/about.html')
def login(request):
	if request.method=='POST':
		
		passw=request.POST['password']
		email=request.POST['email']
		
		d=reg.objects.all().filter(password=passw,email=email)
		if d:

			for x in d:

				request.session['loginid']=x.id

				c=x.usertype
				if c=='admin':

					return HttpResponseRedirect('/admintable/')
				elif c=='secretary':
					return HttpResponseRedirect('/secretarytable/')
				elif c=='president':
					return HttpResponseRedirect('/presidenttable/')
				else:
					return HttpResponseRedirect('/login/')
		else:
			return render(request,'home/login.html')

	else:

		return render(request,'home/login.html')
	
def admintable(request):
	if request.session.has_key('loginid'):

		return render(request,'admin/addmembers.html')
	else:
		return render(request,'home/login.html')

def log(request):
	if request.session.has_key('loginid'):
		del  request.session['loginid']
	logout(request)
	return render(request,'home/login.html')
def secretarytable(request):
	if request.session.has_key('loginid'):

		return render(request,'secretary/addmembers.html')
	else:
		return render(request,'home/login.html')
def presidenttable(request):
	if request.session.has_key('loginid'):

		return render(request,'president/addmembers.html')
	else:
		return render(request,'home/login.html')
def admcontact(request):
	if request.session.has_key('loginid'):

		return render(request,'admin/contact.html')
	else:
		return render(request,'home/login.html')

def addmembers(request):
	if request.session.has_key('loginid'):

		if request.method=='POST':
			name=request.POST['name']
			email=request.POST['email']
			dob=request.POST['dob']
			phone=request.POST['phone']
			address=request.POST['address']
			aadhar=request.POST['aadhar']
			status=request.POST['status']
			if member.objects.all().filter(email=email,aadhar=aadhar):
				return render(request,'admin/addmembers.html',{'msg':'already exist'})
			else:
				a=member(name=name,email=email,phone=phone,dob=dob,address=address,aadhar=aadhar,status=status)
				a.save()
				return HttpResponseRedirect("/addmembers/")


		else:
			return render(request,'admin/addmembers.html')
	else:
		return render(request,'home/login.html')
def saddmembers(request):
	if request.session.has_key('loginid'):

		if request.method=='POST':
			name=request.POST['name']
			email=request.POST['email']
			dob=request.POST['dob']
			phone=request.POST['phone']
			address=request.POST['address']
			aadhar=request.POST['aadhar']
			status=request.POST['status']
			if member.objects.all().filter(email=email,aadhar=aadhar):
				return render(request,'secretary/addmembers.html',{'msg':'already exist'})
			else:
				a=member(name=name,email=email,phone=phone,dob=dob,address=address,aadhar=aadhar,status=status)
				a.save()
				return HttpResponseRedirect("/saddmembers/")


		else:
			return render(request,'secretary/addmembers.html')
	else:
		return render(request,'home/login.html')
def paddmembers(request):
	if request.session.has_key('loginid'):

		if request.method=='POST':
			name=request.POST['name']
			email=request.POST['email']
			dob=request.POST['dob']
			phone=request.POST['phone']
			address=request.POST['address']
			aadhar=request.POST['aadhar']
			status=request.POST['status']
			if member.objects.all().filter(email=email,aadhar=aadhar):
				return render(request,'president/addmembers.html',{'msg':'already exist'})
			else:
				a=member(name=name,email=email,phone=phone,dob=dob,address=address,aadhar=aadhar,status=status)
				a.save()
				return HttpResponseRedirect("/paddmembers/")


		else:
			return render(request,'president/addmembers.html')
	else:
		return render(request,'home/login.html')
import datetime
from django.db.models import Q	
def attendence(request):
	if request.session.has_key('loginid'):
		a=datetime.datetime.now()
		d=a.strftime('%x')
		t=a.strftime('%X')
		if request.method=='POST':
			b=request.POST['attend']
			b1=member.objects.get(id=b)
			b2=att(id1=b1,date=d,time=t)
			b2.save()
			return HttpResponseRedirect('/attendence/')
		else:
			c=att.objects.filter(date=d)
			c1=[]
			for x in c:
				c1.append(x.id1.id)
			c2=member.objects.filter(~Q(id__in=c1))
			m3=att.objects.values_list('date',flat=True).distinct()
			return render(request,'admin/attendence.html',{'b':c2,'at':m3})
	else:
		return render(request,'home/login.html')
def sattendence(request):
	if request.session.has_key('loginid'):
		a=datetime.datetime.now()
		d=a.strftime('%x')
		t=a.strftime('%X')
		if request.method=='POST':
			b=request.POST['attend']
			b1=member.objects.get(id=b)
			b2=att(id1=b1,date=d,time=t)
			b2.save()
			return HttpResponseRedirect('/sattendence/')
		else:
			c=att.objects.filter(date=d)
			c1=[]
			for x in c:
				c1.append(x.id1.id)
			c2=member.objects.filter(~Q(id__in=c1))
			m3=att.objects.values_list('date',flat=True).distinct()
			return render(request,'secretary/attendence.html',{'b':c2,'at':m3})
	else:
		return render(request,'home/login.html')
def pattendence(request):
	if request.session.has_key('loginid'):
		a=datetime.datetime.now()
		d=a.strftime('%x')
		t=a.strftime('%X')
		if request.method=='POST':
			b=request.POST['attend']
			b1=member.objects.get(id=b)
			b2=att(id1=b1,date=d,time=t)
			b2.save()
			return HttpResponseRedirect('/pattendence/')
		else:
			c=att.objects.filter(date=d)
			c1=[]
			for x in c:
				c1.append(x.id1.id)
			c2=member.objects.filter(~Q(id__in=c1))
			m3=att.objects.values_list('date',flat=True).distinct()
			return render(request,'president/attendence.html',{'b':c2,'at':m3})
	else:
		return render(request,'home/login.html')
import json
def att_dis(request):
	we=request.GET["p"]
	result_set = []
	var=[]

	var=att.objects.all().filter(date=we)
	for x in var:
		result_set.append({'name':x.id1.name,'date':x.date, 'tim':x.time})
	return HttpResponse(json.dumps(result_set),content_type='application/json')
def loanapplication(request):
	if request.session.has_key('loginid'):
		a=member.objects.all()
		if request.method=="POST":
			c=request.POST['income']
			d=request.POST['loantype']
			e=request.POST['amount']
			f=request.POST['pp']
			idd=member.objects.get(id=f)
			g=int(e)+int(e)*0.1

			if loan.objects.filter(id2=f,status="approved"):

				return render(request,'admin/loanapplication.html',{'b':a,'msg':'a loan is in proceeding'})
			else:

				ab=loan(income=c,loantype=d,amount=e,id2=idd,balance=int(g))
				ab.save()
				return render(request,'admin/loanapplication.html',{'b':a})
		else:
			return render(request,'admin/loanapplication.html',{'b':a})

		return render(request,'admin/loanapplication.html',{'b':a})
	else:
		return render(request,'home/login.html')
def sloanapplication(request):
	if request.session.has_key('loginid'):
		a=member.objects.all()
		if request.method=="POST":
			c=request.POST['income']
			d=request.POST['loantype']
			e=request.POST['amount']
			f=request.POST['pp']
			idd=member.objects.get(id=f)
			g=int(e)+int(e)*0.1

			if loan.objects.filter(id2=f,status="approved"):

				return render(request,'secretary/loanapplication.html',{'b':a,'msg':'A loan is in proceeding !'})
			else:

				ab=loan(income=c,loantype=d,amount=e,id2=idd,balance=int(g))
				ab.save()
				return render(request,'secretary/loanapplication.html',{'b':a})
		else:
			return render(request,'secretary/loanapplication.html',{'b':a})

		return render(request,'secretary/loanapplication.html',{'b':a})
	else:
		return render(request,'home/login.html')
def ajax(request):
	we=request.GET["p"]
	print(we)
	var=member.objects.all().filter(id=we)
	for x in var:
		d1=x.name
		d2=x.email
		d3=x.phone
		d4=x.dob
		d5=x.address
		d6=x.status

		print(d1)
		dat={"aa":d1,'bb':d2,'cc':d3,'dd':d4,'ee':d5,'ff':d6}
	return JsonResponse(dat)
def loandetail(request):
	if request.session.has_key('loginid'):
		a=loan.objects.filter(status="pending")
		return render(request,'admin/loandetail.html',{'c':a})
	else:
		return render(request,'home/login.html')
def ploandetail(request):
	if request.session.has_key('loginid'):
		a=loan.objects.filter(status="pending")
		return render(request,'president/loandetail.html',{'c':a})
	else:
		return render(request,'home/login.html')
def approve(request):
	if request.method=='GET':
		a=request.GET['a']

		b=loan.objects.filter(id=a).update(status='approved',)

		return HttpResponseRedirect('/loandetail/')
def papprove(request):
	if request.method=='GET':
		a=request.GET['a']

		b=loan.objects.filter(id=a).update(status='approved',)

		return HttpResponseRedirect('/ploandetail/')
def cancel(request):
	if request.method=='GET':
		a=request.GET['a']
		b=loan.objects.filter(id=a).delete()
		return HttpResponseRedirect('/loandetail/')
def pcancel(request):
	if request.method=='GET':
		a=request.GET['a']
		b=loan.objects.filter(id=a).delete()
		return HttpResponseRedirect('/ploandetail/')
def loantracking(request):
	if request.session.has_key('loginid'):
		a=loan.objects.all().filter(status="approved")
		return render(request,'admin/loantracking.html',{'b':a})
	else:
		return render(request,'home/login.html')
def sloantracking(request):
	if request.session.has_key('loginid'):
		a=loan.objects.all().filter(status="approved")
		return render(request,'secretary/loantracking.html',{'b':a})
	else:
		return render(request,'home/login.html')
def addamount(request):
	if request.session.has_key('loginid'):
		e=datetime.datetime.now()
		d=e.strftime('%x')
		t=e.strftime('%X')
		if request.method=="GET":
			a=request.GET['a']
			b=loan.objects.filter(id=a)

			return render(request,'admin/loanaddamount.html',{'b':b})
		if request.method=='POST':
			cd=request.POST['pd']
			payamount=request.POST['pa']
			ac=loan.objects.get(id=cd)
			ba=request.POST['bl']
			ba1=float(ba)-float(payamount)
			if ba1<0:
				c2=loan.objects.filter(id=cd)
				return render(request,'admin/loanaddamount.html',{'b':c2,'msg':'The amount added is more than the balance amount'})
			else:

				dt=pay(id3=ac,payamount=payamount,date=d,time=t)
				dt.save()
				ba2=loan.objects.filter(id=cd).update(balance=int(ba1))
				if ba1==0:

					c=loan.objects.filter(id=cd).update(status="closed")


			
			return HttpResponseRedirect('/loantracking/')
	else:
		return render(request,'home/login.html')
def saddamount(request):
	if request.session.has_key('loginid'):
		e=datetime.datetime.now()
		d=e.strftime('%x')
		t=e.strftime('%X')
		if request.method=="GET":
			a=request.GET['a']
			b=loan.objects.filter(id=a)
			return render(request,'secretary/loanaddamount.html',{'b':b})
		if request.method=='POST':
			cd=request.POST['pd']
			payamount=request.POST['pa']
			ac=loan.objects.get(id=cd)
			ba=request.POST['bl']
			ba1=float(ba)-float(payamount)

			if ba1<0:
				c2=loan.objects.filter(id=cd)
				return render(request,'admin/loanaddamount.html',{'b':c2,'msg':'The amount is more than the balance amount'})
			else:

				dt=pay(id3=ac,payamount=payamount,date=d,time=t)
				dt.save()
				ba2=loan.objects.filter(id=cd).update(balance=int(ba1))
				if ba1==0:

					c=loan.objects.filter(id=cd).update(status="closed")

		
			return HttpResponseRedirect('/sloantracking/')
	else:
		return render(request,'home/login.html')
def loanstatus(request):
	if request.session.has_key('loginid'):
		c_list = ['approved']
		a=loan.objects.all().filter(status__in=c_list)


		return render(request,'admin/loanstatus.html',{'b':a})
	else:
		return render(request,'home/login.html')
def detail(request):
	if request.session.has_key('loginid'):
		
		if request.method=='GET':

			a=request.GET['a']
			if a=="":
				return HttpResponseRedirect('/loanstatus/')
			else:
				c=loan.objects.filter(id=a)

				d=pay.objects.filter(id3=a)
				if d:

					return render(request,'admin/detail.html',{'b':c,'e':d})
				else:
					return render(request,'admin/detail.html',{'b':c,'e':d,'msg':'Not paid yet !'})

		
		   
	else:
		return render(request,'home/login.html')
def ploanstatus(request):
	if request.session.has_key('loginid'):
		c_list = ['approved']
		a=loan.objects.all().filter(status__in=c_list)

		return render(request,'president/loanstatus.html',{'b':a})
	else:
		return render(request,'home/login.html')
def pdetail(request):
	if request.session.has_key('loginid'):
		
		if request.method=='GET':

			a=request.GET['a']
			if a=="null":
				return HttpResponseRedirect('/ploanstatus/')
			else:
				c=loan.objects.filter(id=a)

				d=pay.objects.filter(id3=a)
				if d:

					return render(request,'president/detail.html',{'b':c,'e':d})
				else:
					return render(request,'president/detail.html',{'b':c,'e':d,'msg':'Not paid yet!'})

		
		   
	else:
		return render(request,'home/login.html')
def emajax(request):

	we=request.GET['p']
	print(we)
	
	if member.objects.filter(aadhar=we):
		
		c="a"
		dat={"aa":c}
		return JsonResponse(dat)
	else:

		c=""
		dat={'bb':c}
		return JsonResponse(dat)






		
	

	



# Create your views here.
