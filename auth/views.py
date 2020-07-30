from django.shortcuts import render ,redirect
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.views import View
from auth import forms
from django.contrib.auth import login
class loginreq(LoginView):
    template_name = 'auth\login.html'
    redirect_authenticated_user = True

class logout(LogoutView):
    pass


class signupreq(View):
    def get(self,request):
        context = {
            "form" : forms.Signupform
        }
        return render(request , 'auth\signup.html' , context)
    def post(self,request):
        filledform  = forms.Signupform(request.POST , request.FILES)
        if filledform.is_valid():
            user = filledform.save()
            login(request , user)
            return redirect('/')
        else:
            context = {
                "forms" : filledform,
            }
            return render(request , 'auth\signup.html' , context)
