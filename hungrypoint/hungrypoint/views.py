from django.shortcuts import render,redirect
from admin_pannel.models import Items,Book_table,Contact_form,Sub


def index(request):
    if request.method == 'POST':
        sub = Sub()

        sub.user_email  = request.POST.get('sub')
        sub.subscribed = 'Yes'

        sub.save()
    

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
    if request.method == 'POST':

        c_form = Contact_form()

        c_form.user_name= request.POST.get('name')
        c_form.user_email = request.POST.get('email')
        c_form.subject = request.POST.get('subject')
        c_form.message = request.POST.get('message')



        c_form.save()

    return render(request,'contact_form.html')