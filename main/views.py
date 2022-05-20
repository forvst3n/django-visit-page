from django.shortcuts import render


def index(request):
    #Show main page
    return render(request,'main/index.html')
def about_us(request):
    #Show about us page
    return render(request,'main/aboutus.html')
def contact(request):
    #Show contact page
    return render(request,'main/contact.html')