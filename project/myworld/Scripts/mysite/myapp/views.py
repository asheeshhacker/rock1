from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import game ,postdata,contdb

from django.views.generic.edit import FormView


# Create your views here.
def sub1(request):
    
    data ={
        'tittle':'home page',
           }
    
    return render(request,"index.html",data)
def chat(request):
    dbdata = game.objects.all()
    
    
        
    return render(request,"chat.html",{'dbdata':dbdata ,"tittle":'CHAT'})
    
def saveform(request):
    names = request.POST.get('name1')
    des  = request.POST.get('name2')
        
    game(name=names,description = des).save()
    return redirect(chat)       
    
def post(request):
      
    postdb = postdata.objects.all()
    
    return render(request,"post.html",{"postdb":postdb ,'tittle':'POST'})
def fullpost(request,pid):
   
    pdid = postdata.objects.get(slug=pid)
    print(pdid)
    return render (request,'fullpost.html',{'pdid':pdid})

def contact(request):
    return render(request,'contact.html')

def contactform(request):
    names = request.POST.get('name')
    email = request.POST.get('mail')
    cmts = request.POST.get('cmt')
    
    contdb(name=names,mail=email,cmt=cmts).save()
    return render(request,'contact.html')