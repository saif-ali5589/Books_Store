from django.shortcuts import render
from .models import Books_Data

# Create your views here.

def home(request):
    return render(request,"Home_Page.html")

def Contact(request):
    return render(request,"Contact_Page.html")

def Books_Page(request,pk=None):
    print(pk)
    if pk:
        print("1")
        data = Books_Data.objects.all().filter(cat_type=pk)
        for i in data:
            print(type(i.cat_type))
        return render(request,"Books_Store.html",{"data":data})
    else:
        data = Books_Data.objects.all()
        return render(request,"Books_Store.html",{"data":data})
def Owner_Contact(request,pk=None):
    c = Books_Data.objects.filter(id=pk)
    return render(request,"contact_person.html",{"d":c})
