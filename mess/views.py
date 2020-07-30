from django.shortcuts import render
from mess import models,forms
from django.views import View
from django.contrib.auth.models import User
# Create your views here.
class privatemessage(View):
    def get(self,request,pk):
        msgids = [msg.id for msg in  models.messagerecord.objects.filter(msg_reciever = self.request.user , msg_sender=User.objects.get(pk=pk)) ]
        msgids = msgids + [msg.id for msg in  models.messagerecord.objects.filter(msg_sender = self.request.user , msg_reciever=User.objects.get(pk=pk))]
        #print(msgids)
        try :
            msghistory = models.messagerecord.objects.filter(pk__in = msgids).order_by('-created_at')
        except:
            msghistory = None
        context={
            "form":forms.msgform,
            "msghistory":msghistory,
            "othername":User.objects.get(pk=pk)
        }
        return render(request,'message\private.html',context)
    
    def post(self,request,pk):
        msgids = [msg.id for msg in  models.messagerecord.objects.filter(msg_reciever = self.request.user , msg_sender=User.objects.get(pk=pk)) ]
        msgids = msgids + [msg.id for msg in  models.messagerecord.objects.filter(msg_sender = self.request.user , msg_reciever=User.objects.get(pk=pk))]
        #print(msgids)
        formm = forms.msgform(request.POST)
        if formm.is_valid():
            filledform = formm.save(commit=False)
            filledform.msg_sender = request.user
            filledform.msg_reciever= User.objects.get(pk=pk)
            filledform.save()
        try :
            msghistory = models.messagerecord.objects.filter(pk__in = msgids).order_by('-created_at')
        except:
            msghistory = None
        context={
            "form":forms.msgform,
            "msghistory":msghistory,
            "othername":User.objects.get(pk=pk)
        }
        return render(request,'message\private.html',context)