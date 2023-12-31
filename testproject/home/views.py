from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def calcu(request):
    result=0
    data = {}
    try:
        if request.method == 'POST':
            num1 = int(request.POST.get('num1'))
            num2 = int(request.POST.get('num2'))
            result = num1 + num2
            data = {'num1': num1,'num2': num2, 'result': result}
    except:
        pass
    return render(request,'index.html',data)
def result(request):
    try:
        if request.method == 'POST':
            num1 = int(request.POST.get('num1'))
            num2 = int(request.POST.get('num2'))
            result = num1 + num2
            data = {'num1': num1,'num2': num2, 'result': result}
            return HttpResponse(result)

    except:
        pass