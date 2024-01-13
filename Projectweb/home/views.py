from django.shortcuts import render
from .models import service,contactEquiry
from news.models import News
from django.core.paginator import Paginator
from django.http.response import HttpResponse

# Create your views here.
def home(request):
    news_data = News.objects.all()
    data = {'news_data':news_data}
    return render(request,'index.html',data)
def propertyDetails(request):
    return render(request,'property-details.html')
def properties(request):
    return render(request,'properties.html')
def contant(request):
    return render(request,'contact.html')
def calculator(request):
    data = {}
    try:
        if request.method == 'POST':
            num1 = eval(request.POST.get('num1'))
            num2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == '+':
                sum = num1 + num2
            elif opr == '-':
                sum = num1 - num2
            elif opr == '*':
                sum = num1 * num2
            else:
                sum = num1 / num2
            data = {'num1':num1,'num2':num2,'opr':opr, 'sum': sum}
    except:
        sum ='Invalid operation...'
        print(sum)
    return render(request,'calculator.html',data)
def evanOdd(request):
    result = ''
    try:
        if request.method == 'POST':
            number = eval(request.POST.get('number'))
            if number%2 == 0:
                result = (f'this is evan number {number}')
            else:
                result = (f'This is odd number {number}')
    except:
        pass
    return render(request,'evan.odd.html',{'result': result})
def marksheet(request):
    data = {}
    if request.method == '':
        return render(request,'marksheet.html',{'error':True})
    else:
        subject1 = eval(request.POST.get('subject1'))
        subject2 = eval(request.POST.get('subject2'))
        subject3 = eval(request.POST.get('subject3'))
        subject4 = eval(request.POST.get('subject4'))
        subject5 = eval(request.POST.get('subject5'))
        Total = subject1 + subject2 + subject3 + subject4 + subject5
        percentage = (Total*100/500)
        if percentage >= 60:
            division = 'First Division' 
        elif percentage >= 40:
            division = 'Second Division'
        elif percentage >=35:
            division = 'Third Division'
        else:
            division = 'Fail'
        data = {'total':Total,'percentage':percentage,'division':division}
    return render(request,'marksheet.html',data)
def services(request):
    service_data = service.objects.all()
    paginator = Paginator(service_data,2)
    page_number = request.GET.get('page')
    servicefinalData = paginator.get_page(page_number)
    total_page = servicefinalData.paginator.num_pages


# <<<<<_____---------------__________>>>>>>>>>>#
    # # Ascending & Desending 
    # # To set query with like or exact macth user this ===>> 
    # service_data = service.objects.all().order_by('service_name')
    # if request.method == 'GET':
    #     serviceTitle = request.GET.get('servicename')
    #     if serviceTitle is not None:
    #         service_data = service.objects.filter(service_name__icontains=serviceTitle)
    # # print(service_data)
    data = {'data':servicefinalData,
            'lastpage':total_page,
            'totalpagelist':[page+1 for page in range(total_page)]
    }
    return render(request,'service.html',data)
def newsDetails(request,slug):
    newsDetails = News.objects.get(news_slug=slug) 
    data = { 
        'newsDetails': newsDetails
    }
    return render(request,'newsdetails.html',data)

def saveEquiry(request):
        if request.method == 'POST':
            fullname = request.POST.get('fullname')
            email = request.POST.get('email')
            number = request.POST.get('number')
            message = request.POST.get('message')
            data = contactEquiry(fullname=fullname,email=email,number=number,message=message)
            data.save()
        else:
            return HttpResponse('Invalid Input')
        return render(request,'contact.html')
def aboutUs(request):
    return render(request,'aboutus.html')
