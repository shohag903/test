from django.shortcuts import render
from.models import contact

def contactus(request):
       if request.method == "POST":
              name=request.POST.get('name')
              email=request.POST.get('email')
              subject=request.POST.get('subject')
              message=request.POST.get('message')
              contactdata = contact.objects.create(name = name, email = email, subject = subject,
               messsage = message)
              contactdata.save()
              return render(request,'contact.html')
       return render(request,'contact.html')