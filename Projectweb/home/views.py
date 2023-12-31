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

