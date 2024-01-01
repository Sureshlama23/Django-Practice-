from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
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