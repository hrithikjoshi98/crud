from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Product
from .forms import ProductForm
# Create your views here.

def update_page(request, my_id):
    form = ProductForm()
    data = Product.objects.get(id=my_id)
    form.fields['name'].initial = data.name
    form.fields['desc'].initial = data.desc
    form.fields['price'].initial = data.price
    form.fields['quantity'].initial = data.quantity
    print(my_id, data.name)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if 'home' in request.POST:
            return HttpResponseRedirect('/')
        if 'update' in request.POST:
            if form.is_valid():
                name = form.cleaned_data['name']
                desc = form.cleaned_data['desc']
                price = form.cleaned_data['price']
                quantity = form.cleaned_data['quantity']
                

                # password = form.cleaned_data['password']
                Product(id=my_id, name=name, desc=desc, price=price, quantity=quantity).save()
                return HttpResponseRedirect('/')
                        

    return render(request, 'crud/update_page.html', {'id':my_id, 'name': data.name , 'desc': data.desc, 'price': data.price, 'quantity': data.quantity, 'form': form})

def home(request):
    all_data = Product.objects.all()
    form = ProductForm()
    if request.method == 'POST':
        if 'add' in request.POST:
            form = ProductForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                desc = form.cleaned_data['desc']
                price = form.cleaned_data['price']
                quantity = form.cleaned_data['quantity']

                Product(name=name, desc=desc, price=price, quantity=quantity).save()
                # print(name, '\n', email, '\n', password)
            else:
                form = ProductForm()
        if 'delete' in request.POST:
            print('delete clicked')
            delid = request.POST.get('delid')
            Product(id=delid).delete()
            print(delid)
    contexts = {'all_data': all_data, 'form': form}
    return render(request, 'crud/home.html', contexts)
