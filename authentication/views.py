from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from authentication.models import User_authentication

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'homepage.html', {'success':"hello"})

def signup(request):
    if request.method == "POST":
        fname = request.POST.get('txtfirst')
        lname = request.POST.get('txtlast')
        email = request.POST.get('txtmail')
        address = request.POST.get('txtadd')
        street = request.POST.get('txtstreet')
        city = request.POST.get('txtcity')
        pincode = request.POST.get('txtpin')
        username = request.POST.get('txtuser')
        password_1 = request.POST.get('password1')
        password_2 = request.POST.get('password2')
        if password_1 == password_2:
            
            new_user = User.objects.create_user(username = username, email  = email , password=password_1)
            new_user.first_name = fname
            new_user.last_name = lname
            new_user.save()
            myuser = {
                "address" : address,
                "street" : street,
                "city" : city,
                "pin_code" : pincode,
            }
            User_authentication.objects.create(user = new_user, **myuser)
            return render(request,'index.html', {'error':'Successfully register'})     
        else:
                return render (request,'index.html', {'error':'Password does not match!'})
    else:
        return render(request,'index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('txtemail')
        user_email = User.objects.get(email=email).username
        print('@@@@@@@@@@@@@@@@@',user_email)
        user = auth.authenticate(username = user_email, email = email)
        print('##############################' ,user)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render (request,'index.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'index.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('index')