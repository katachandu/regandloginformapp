from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Reg


# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class RegisterInput(View):
    def get(self,request):
        return render(request,'register.html')
class Register(View):
    def post(self,request):
        res=Reg(firstname=request.POST["firstname"],
               lastname=request.POST["lastname"],
               email=request.POST["email"],
               mobile = request.POST["mobile"],
               dob=request.POST["dob"],
               username=request.POST["username"],
               password=request.POST["password"],
               cpassword=request.POST["cpassword"]
               )
        res.save()
        return HttpResponse("you registered successfully")
class LoginInput(View):
    def get(self,request):
        return render(request,'login.html')
class Login(View):
    def post(self,request):
        qs=Reg.objects.filter(username=request.POST["username"],
                              password=request.POST["password"])
        if qs:
            return HttpResponse("login successfully")
        else:
            return HttpResponse(" login failed")

# Create your views here.
