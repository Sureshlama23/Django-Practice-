from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def home(request):
    test_object = Test.objects.all()
    content = {'test_object':test_object}
    return render(request,'index.html', context=content)
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        bio = request.POST.get('bio')
        image = request.FILES.get('image')
        Test.objects.create(name=name,bio=bio,image=image)
        return redirect('home')

    return render(request,'create.html')

