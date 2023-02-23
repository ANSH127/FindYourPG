from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Userdetail(models.Model):
    sno=models.AutoField(primary_key=True)
    username=models.CharField(max_length=10)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=13)
    password=models.CharField(max_length=50)
    
    def __str__(self):
        return "username "+str(self.username)+" Phone "+self.phone


class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=13)
    message=models.TextField()

    
    def __str__(self):
        return "sno "+str(self.sno)+" msg "+self.message[:20]


class RentarDetail(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=13)
    email=models.CharField(max_length=20)
    City=models.CharField(max_length=20)
    main_address=models.CharField(max_length=100)
    detailed_address=models.CharField(max_length=500)
    room_details=models.TextField()
    room_vacent=models.IntegerField()
    nearby_facilities=models.TextField(default='')
    price=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    map=models.CharField(max_length=2000,default='')

class multipleimage(models.Model):
    sno=models.AutoField(primary_key=True)
    room=models.ForeignKey(RentarDetail,on_delete=models.CASCADE)
    room_photos=models.ImageField(upload_to='room/photo',default='')


class Booking(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=13)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    a_date=models.DateField(auto_now_add=False)
    month=models.IntegerField(default=1)
    residance=models.CharField(max_length=100)
    tfare=models.IntegerField(default=0)
    amount_paid=models.IntegerField(default=0)
    remaining_due=models.IntegerField(default=0)
    info=models.ForeignKey(RentarDetail,on_delete=models.CASCADE,default='')
    b_date=models.DateField(auto_now_add=True)
    b_time=models.TimeField(auto_now_add=True)



class Schedule(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=13)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    visitor=models.IntegerField()
    date=models.DateField(auto_now_add=False)
    time=models.TimeField(auto_now_add=False)
    info=models.ForeignKey(RentarDetail,on_delete=models.CASCADE,default='')

    
class Proof(models.Model):

    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default='')
    info=models.ForeignKey(Booking,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='room/proof')
    b_date=models.DateField(auto_now_add=True)
    file=models.FileField(blank=True)
    status=models.CharField(max_length=30)


class dueProof(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    parent=models.ForeignKey(Proof,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='room/dueproof')
    payment_date=models.DateField(auto_now_add=True)
    amount=models.IntegerField()
    status=models.CharField(max_length=30)






class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
