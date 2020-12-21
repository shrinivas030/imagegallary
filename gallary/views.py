from django.shortcuts import render

# Create your views here.

from .forms import Imageform
from .models import gallarymodel

# Create your views here.
def imageview(request):
    if request.method=='POST':
        form=Imageform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    images=gallarymodel.objects.all()
    form = Imageform()
    context={'form':form,'images':images,}
    return render(request,'gallary/index.html',context)

def searchview(request):
    if request.method=="GET":
        search=request.GET.get('search')
        images=gallarymodel.objects.all().filter(catagory=search)
        context={'images':images}
        return render(request,'gallary/searchpage.html',context)