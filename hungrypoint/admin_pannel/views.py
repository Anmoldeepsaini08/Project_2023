from django.shortcuts import render,redirect
from .models import Items,Book_table,Contact_form,Sub
# Create your views here.


def index(request):
    if request.method == 'POST':

        item = Items()

        item.name= request.POST.get('name')
        item.category = request.POST.get('category')
        item.description = request.POST.get('desc')
        item.price = request.POST.get('price')
        item.image = request.FILES['image']

        item.save()

    return render(request,'admin.html')


def manage(request):

    if request.method == 'POST':

  
        delete_item = request.POST.get('delete')
        Items.objects.get(name=delete_item).delete()
        
        return redirect('manage')
    
    else:
        items = Items.objects.all()
        
        return render(request,'manage.html',{'items_display':items})
    


def tables(request):
    reser = Book_table.objects.all()

    return render(request,'booked_table.html',{'reserved':reser})



def contact(request):

    details = Contact_form.objects.all()
    return render(request,'contact.html',{'details':details})


def subscribe(request):

    sub = Sub.objects.all()

    return render(request,'subscriber.html',{'sub':sub})