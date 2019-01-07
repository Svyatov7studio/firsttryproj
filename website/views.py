from django.shortcuts import render

def index(request):
    return render(request,'maintemplate/homePage.html')

def contact(request):
    return render(request, 'maintemplate/contactfile.html',{'values': ['Если у Вас есть вопросы - звоните', '+7 (999) 999 99 99']})
