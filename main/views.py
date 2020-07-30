from django.http import HttpResponse
from django.shortcuts import render,redirect
from main import models,forms
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView

)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class Wall(LoginRequiredMixin, ListView):
    context_object_name = 'posts'
    template_name = 'main/wall.html'
    login_url = 'auth/login'

    def get_queryset(self):
        friendIds = [ friend.person2.id for friend in  models.Friends.objects.filter(person1 = self.request.user) ]
        friendIds = friendIds + [ friend.person1.id for friend in  models.Friends.objects.filter(person2 = self.request.user) ]
        return models.Post.objects.filter(user__in = friendIds).order_by('-created_at')

class Home(LoginRequiredMixin , ListView):
    context_object_name = 'posts'
    template_name = 'main\Home.html'
    login_url = '/auth/login'

    def get_queryset(self):
        return models.Post.objects.filter(user = self.request.user).order_by("-created_at")

    def get_context_data(self , *args ,**kwargs):
        data =  super().get_context_data(*args,**kwargs)
        data['post_form'] = forms.PostForm()
        return data

class Post(View):
    def post(self, request):
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        
        return redirect('/home/')



class PostLike(View):
    model = models.Post

    def post(self, request, pk):
        post = self.model.objects.get(pk = pk)
        models.Like.objects.create(post = post, user = request.user)
        return HttpResponse(code = 204)

class PostComment(View):
    model = models.Post
    form = forms.PostComment

    def post(self, request, pk):
        post = self.model.objects.get(pk = pk)
        form = self.form(request.POST)

        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return HttpResponse(code = 204)
        
        print(form.errors)
        return HttpResponse('Error')
#send add&cancel
class Seeid(View):
    def get(self,request,pk):
        friendIds = [ friend.person2.id for friend in  models.Friends.objects.filter(person1 = self.request.user) ]
        friendIds = friendIds + [ friend.person1.id for friend in  models.Friends.objects.filter(person2 = self.request.user) ]
        context = {
            'profile':User.objects.get(pk = pk),
            'same':False,
            'friend':False,
            "posts":models.Post.objects.filter(user__pk = pk).order_by('-created_at'),
            "gotrequest":False
        }
        if request.user.id == pk:
            context['same']=True
        else:
            if pk in friendIds:
                context['friend']=True
            else:
                try:
                    requests = models.Friendrequests.objects.get(sender = User.objects.get(pk = pk), reciever  = request.user )
                except :
                    requests = None
                if requests != None:
                    context['gotrequest'] = True
        return render(request,'main\profile.html',context) 

'''
class Edit(UpdateView):
    template_name = 'auth\signup.html'
    fields = ['first_name','last_name','username','email']
    success_url = '/'
    model= User

def verify(request,pk):
    if pk == request.user.pk:
        return redirect(Edit.as_view(request,pk))
    else:
        return redirect('/')
        '''
        

class Friends(LoginRequiredMixin,View):
    login_url = '/auth/login'
    def get(self,request):
        friendIds = [ req.sender.id for req in  models.Friendrequests.objects.filter(reciever = self.request.user) ]
        context={
            "search":forms.SearchForm,
            "friendlist":User.objects.filter(id__in = friendIds),
            "searchresult":None
        }
        return render(request,'main\search.html',context)
    def post(self,request):
        friendIds = [ req.sender.id for req in  models.Friendrequests.objects.filter(reciever = self.request.user) ]
        context={
            "search":forms.SearchForm,
            "friendlist":User.objects.filter(id__in = friendIds),
            "searchresult":User.objects.filter(username__contains = request.POST['search'])
        }
        return render(request,'main\search.html',context)
    '''def get(self,request):
        friendIds = [ friend.person2.id for friend in  models.Friends.objects.filter(person1 = self.request.user) ]
        friendIds = friendIds + [ friend.person1.id for friend in  models.Friends.objects.filter(person2 = self.request.user) ]
        context={
            "search":forms.SearchForm,
            "friendlist":User.objects.filter(id__in = friendIds),
            "searchresult":None
        }
        return render(request,'main\search.html',context)
    def post(self,request):
        friendIds = [ friend.person2.id for friend in  models.Friends.objects.filter(person1 = self.request.user) ]
        friendIds = friendIds + [ friend.person1.id for friend in  models.Friends.objects.filter(person2 = self.request.user) ]
        context={
            "search":forms.SearchForm,
            "friendlist":User.objects.filter(id__in = friendIds),
            "searchresult":User.objects.filter(username__contains = request.POST['search'])
        }
        return render(request,'main\search.html',context)'''

class Sendrequest(View):
    def post(self, request, pk):
        reciever = User.objects.get(pk = pk)
        models.Friendrequests.objects.create(sender = request.user, reciever =reciever )
        return HttpResponse(code = 204)

class addfriend(View):
    def post(self,request,pk):
        reciever = User.objects.get(pk = pk)
        models.Friends.objects.create(person1 = request.user , person2 = reciever)
        models.Friendrequests.objects.get(sender = reciever , reciever =request.user).delete()
        return HttpResponse(code = 204)


class cancelrequest(View):
    def post(self,request,pk):
        reciever = User.objects.get(pk = pk)
        models.Friendrequests.objects.get(sender = reciever , reciever =request.user).delete()
        return HttpResponse(code = 204)