from django.shortcuts import render
from project1.forms import sum_form

# Create your views here.

def Home(request):
    values = sum_form()
    result = 0
    data = {'values':values}
    if request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        result = num1 + num2
        data = {'vulues':values, 'result': result}
    return render(request,'index.html',data)

    
