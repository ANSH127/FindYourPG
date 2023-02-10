from django.shortcuts import render,HttpResponse,redirect

from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from PG.models import Userdetail,Contact,multipleimage,RentarDetail,Booking,Schedule
# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
    

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name','')
        c_email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        msg=request.POST.get('msg','')
        contact=Contact(name=name,email=c_email,phone=phone,message=msg)
        contact.save()
        
        messages.success(request,"Your Response submitted successfully")
        return redirect('/')

        
    else:
        return render(request,'contact.html')

def register(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        phone=request.POST.get('phone','')
        email=request.POST.get('email','')
        city=request.POST.get('city','')
        main_address=request.POST.get('m_address','')
        detail_address=request.POST.get('d_address','')
        vacency=request.POST.get('vacent','')
        price=request.POST.get('price','')
        room_details=request.POST.get('r_details','')
        room_photos=request.FILES.getlist('r_img')
        
        renter_form=RentarDetail(name=name,phone=phone,email=email,City=city,main_address=main_address,detailed_address=detail_address,room_details=room_details,room_vacent=vacency,price=price)
        renter_form.save()
        for image in room_photos:
            x=multipleimage(room_photos=image,room=RentarDetail.objects.filter(sno=renter_form.sno)[0])
            x.save()
        # print(name,phone,email,city,main_address,detail_address,vacency,room_details)
        
        messages.success(request,"Your Registration Completed successfully")
        return redirect('/')
    else:
        return render(request,'register.html')

def home1(request,slug):
        obj=RentarDetail.objects.filter(City=slug)
        # print(obj)
        return render(request,'home1.html',{'obj':obj,'scity':slug,'tresults':len(obj)})

def view(request,slug,myid,slug2):
    print(myid)
    obj=RentarDetail.objects.filter(sno=myid)
    detail=(obj[0].room_details)
    list=(detail.split(','))
    return render(request,'view.html',{'item':obj[0],'slug':slug2,'list':list})
    
def checkout(request,slug,myid,slug2):
    
    obj=RentarDetail.objects.filter(sno=myid)[0]
    
    # print(obj)

    return render(request,'booking.html',{'item':obj})



def schedule(request,slug,myid,slug2):
    if request.method=='POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        age=request.POST.get('age','')
        gender=request.POST.get('radiobtn','')
        visitor=request.POST.get('visitor','')
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        schedule=Schedule(name=name,email=email,phone=phone,age=age,gender=gender,visitor=visitor,date=date,time=time,info=RentarDetail.objects.filter(sno=myid)[0])
        schedule.save()
        messages.success(request,"Your Visit Scheduled successfully")

        return redirect('/')
    
    
        
    
        
    obj=RentarDetail.objects.filter(sno=myid)[0]
    
    # print(obj)

    return render(request,'schedule.html',{'item':obj})
    

def handlesignup(request):
    if request.method=='POST':
        # get the post parameter
        username=request.POST.get('username','')
        name=request.POST.get('name','')
        signup_email=request.POST.get('signup_email','')
        phone=request.POST.get('phone','')
        password=request.POST.get('password','')
        password1=request.POST.get('password1','')
        # print(username,name,signup_email,password,password1)
        if len(name.split())!=2:
            messages.error(request,'Enter your full name')
            return redirect('signup')

        fname=name.split()[0]
        lname=name.split()[1]
        # username should be atleast 10 character long
        if len(username)>10:
            messages.error(request,'username must be under 10 characters')
            return redirect('signup')
        # username should be alphanumeric
        
        if not  username.isalnum():
            messages.error(request,'username should only cantain letters and number')
            return redirect('signup')
        # password should be match with confirm password field
        if password!=password1:
            messages.error(request,'Password does not match')
            return redirect('signup')

        
        myuser=User.objects.create_user(username,signup_email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        userdetail=Userdetail(username=username,name=name,phone=phone,email=signup_email,password=password)
        userdetail.save()
        
        
        user=authenticate(username=username, password=password)
        login(request,user)


        messages.success(request,"Your FindYourPG account successfully created")
        return redirect('/')


    else:
        return render(request,'signup.html')



def handlelogin(request):
    if request.method=='POST':
        loginusername=request.POST.get('username','')
        loginpassword=request.POST.get('password','')
        user=authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request,user)
            
            messages.success(request,"Successfully Logged in")

            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials, Please Try Again')
            return redirect('/')



        
    else:
        return render(request,'login.html')
    


def handlelogout(request):
    logout(request)
    messages.success(request,'Successfully Logout')
    return redirect('/')



def handlepayment(request,slug,myid,slug2):
    if request.method=="POST":
        fname=request.POST.get('fname','')
        lname=request.POST.get('lname','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        age=request.POST.get('age','')
        gender=request.POST.get('radiobtn','')
        residance=request.POST.get('choice','')
        print(fname,lname,email,phone,age,gender,residance)
        booking=Booking(name=fname+lname,email=email,phone=phone,age=age,gender=gender,residance=residance,info=RentarDetail.objects.filter(sno=myid)[0])
        booking.save()


        return HttpResponse('payment gateway')
    else:
        return redirect('/')
    
