from django.db import models
class reg(models.Model):
	name=models.CharField(max_length=100,default='')
	password=models.CharField(max_length=100,default='')
	email=models.CharField(max_length=100,default='')
	usertype=models.CharField(max_length=100,default='')
class member(models.Model):
	name=models.CharField(max_length=100,default='')
	email=models.CharField(max_length=100,default='')
	phone=models.CharField(max_length=100,default='')
	dob=models.CharField(max_length=100,default='')
	address=models.CharField(max_length=100,default='')
	aadhar=models.CharField(max_length=100,default='')
	status=models.CharField(max_length=100,default='')
class att(models.Model):
	id1=models.ForeignKey(member,on_delete=models.CASCADE)
	date=models.CharField(max_length=100,default='')
	time=models.CharField(max_length=100,default='')
class loan(models.Model):
	id2=models.ForeignKey(member,on_delete=models.CASCADE)
	income=models.CharField(max_length=100,default='')
	loantype=models.CharField(max_length=100,default='')
	amount=models.CharField(max_length=100,default='')
	status=models.CharField(max_length=100,default='pending')
	balance=models.CharField(max_length=100,default='')
class pay(models.Model):
	id3=models.ForeignKey(loan,on_delete=models.CASCADE)
	payamount=models.CharField(max_length=100,default='')
	date=models.CharField(max_length=100,default='')
	time=models.CharField(max_length=100,default='')
class con(models.Model):
	name=models.CharField(max_length=100,default='')
	email=models.CharField(max_length=100,default='')
	subject=models.CharField(max_length=100,default='')
	message=models.CharField(max_length=100,default='')

		

# Create your models here.
