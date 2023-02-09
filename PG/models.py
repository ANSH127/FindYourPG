from django.db import models

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

class multipleimage(models.Model):
    sno=models.AutoField(primary_key=True)
    room=models.ForeignKey(RentarDetail,on_delete=models.CASCADE)
    room_photos=models.ImageField(upload_to='room/photo',default='')