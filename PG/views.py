from django.shortcuts import render,HttpResponse,redirect

from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from PG.models import Userdetail,Contact,multipleimage,RentarDetail,Booking,Schedule,Proof,dueProof,Profile
from datetime import date
from .mail import send_forget_password_mail
import uuid
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
        nearby_facilities=request.POST.get('nearby_facilities','')
        price=request.POST.get('price','')
        room_details=request.POST.get('r_details','')
        room_photos=request.FILES.getlist('r_img')
        
        renter_form=RentarDetail(name=name,phone=phone,email=email,City=city,main_address=main_address,detailed_address=detail_address,room_details=room_details,room_vacent=vacency,price=price,nearby_facilities=nearby_facilities)
        renter_form.save()
        for image in room_photos:
            x=multipleimage(room_photos=image,room=RentarDetail.objects.filter(sno=renter_form.sno)[0])
            x.save()
        # print(name,phone,email,city,main_address,detail_address,vacency,room_details)
        
        messages.success(request,"Your Respone Submitted We will contact you soon!")
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
    detail2=(obj[0].nearby_facilities)
    list=(detail.split(','))
    list2=(detail2.split(','))
    return render(request,'view.html',{'item':obj[0],'slug':slug2,'list':list,'list2':list2})
    
def checkout(request,slug,myid,slug2):
    
    obj=RentarDetail.objects.filter(sno=myid)[0]
    
    return render(request,'booking.html',{'item':obj,'date':str(date.today())})



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
        profile_obj = Profile.objects.create(user = myuser)
        profile_obj.save()
        
        
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
            return redirect('login')



        
    else:
        return render(request,'login.html')
    


def handlelogout(request):
    logout(request)
    messages.success(request,'Successfully Logout')
    return redirect('/')



def handlepayment(request,slug,myid,slug2):
    if request.user.is_authenticated:
        if request.method=="POST":
            fname=request.POST.get('fname','')
            lname=request.POST.get('lname','')
            email=request.POST.get('email','')
            phone=request.POST.get('phone','')
            age=request.POST.get('age','')
            gender=request.POST.get('radiobtn','')
            a_date=request.POST.get('date','')
            month=request.POST.get('month','')
            fare=request.POST.get('fare','')
            token_fare=request.POST.get('token_fare','')
            residance=request.POST.get('choice','')
            print(fname,lname,email,phone,age,gender,residance,fare,token_fare)
            if token_fare=='0':
                amount=fare
            else:
                amount=token_fare
            print(amount)
            booking=Booking(name=fname+lname,email=email,phone=phone,age=age,gender=gender,a_date=a_date,month=month,tfare=fare,amount_paid=amount,remaining_due=int(fare)-int(amount),residance=residance,info=RentarDetail.objects.filter(sno=myid)[0])
            booking.save()
            bookingid=booking.sno
            obj=RentarDetail.objects.filter(sno=myid)[0]
        

            return render(request,'qrpage.html',{'price':amount,'id':bookingid})
        else:
            return redirect('/')
    else:
        messages.warning(request,'Login Or SingUp to Checkout')
        return redirect('login')
    


def check(request,myid):
    print(myid)
    if request.user.is_authenticated:
        if request.method=='POST':
            obj=Booking.objects.filter(sno=myid)[0]
            print(obj)
            proof=request.FILES.getlist('img')[0]
            print(proof)
            obj2=Proof(info=obj,img=proof,name=request.user)
            obj2.save()
            messages.success(request,'Your Response submitted to us Successfully')

            return redirect('/')
        else:
            return HttpResponse('Error')
    else:
        return redirect('login')




def booking(request):
    if request.user.is_authenticated:

        obj=Proof.objects.filter(name=request.user)
        print(obj)
        if len(obj)==0:
            return render(request,'notfound.html')
        return render(request,'your_booking.html',{'obj':obj})
    else:
        
        messages.warning(request,'Login Or SingUp')
        return redirect('login')



def handleduepayment(request,myid):
    if request.user.is_authenticated:
        if request.method=='POST':
            obj2=Proof.objects.filter(sno=myid)[0]
            print(obj2)
            proof=request.FILES.getlist('img')[0]
            amt=request.POST.get('amt','')
            print(proof,amt)
            obj3=dueProof(parent=obj2,img=proof,name=request.user,amount=amt)
            obj3.save()
            messages.success(request,'Your Response submitted to us Successfully. We will update your amount as soon as possible!')
            return redirect('/')
        else:
            obj=Proof.objects.filter(sno=myid)[0]
            print(obj.info.remaining_due)
            if obj.name==str(request.user) and obj.info.remaining_due!=0 :
                return render(request,'qrpage2.html',{'price':obj.info.remaining_due,'id':myid})
            else:
                return HttpResponse('error')
    else:
        messages.warning(request,'Login Or SingUp to Checkout')
        return redirect('login')
    


def forget_password(request):
    if request.method=='POST':
        username = request.POST.get('username')
        val=User.objects.filter(username=username) 
        val2=User.objects.filter(email=username)
        print(val,val2)
        if not (len(val)>=1 or len(val2)>=1):
                messages.success(request, 'Not user found with this username.')
                return redirect('forget_password')
        if len(val2)>=1:

            user_obj = User.objects.get(email = username)
        else:
            user_obj = User.objects.get(username = username)
        token = str(uuid.uuid4())
        profile_obj= Profile.objects.get(user = user_obj)
        profile_obj.forget_password_token = token
        profile_obj.save()
        send_forget_password_mail(user_obj.email,token)
        messages.success(request, 'An email is sent.')
        return redirect('forget_password')
        
        
    return render(request,'forgetpass.html')


def change_password(request,token):
    profile_obj = Profile.objects.filter(forget_password_token = token).first()
    print(profile_obj)
    if profile_obj==None:
        return render(request,'404.html')
    context = {'user_id' : profile_obj.user.id}
    if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            user_id = request.POST.get('user_id')
            print(new_password,confirm_password,user_id)
            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'/change_password/{token}/')
                
            
            if  new_password != confirm_password:
                messages.success(request, "Password  doesn't match.")
                return redirect(f'/change_password/{token}/')
                         
            
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('/login/')
            
    
    return render(request,'changepass.html',context)