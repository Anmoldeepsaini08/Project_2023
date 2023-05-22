from django.shortcuts import render,redirect
from admin_pannel.models import Users,Items,Book_table

def index(request):
    

    return render(request,'home.html')
            


def menu(request):
    items = Items.objects.all()

    return render(request,'menu.html',{'items':items})


def table_book(request):

    if request.method == 'POST':

        reser = Book_table()

        reser.user_name= request.POST.get('name')
        reser.user_email = request.POST.get('email')
        reser.user_phone = request.POST.get('p_number')
        reser.date = request.POST.get('date')
        reser.time = request.POST.get('time')
        reser.people = request.POST.get('people')


        reser.save()

    return render(request,'tables.html')


def contact_form(request):

    return render(request,'contact_form.html')