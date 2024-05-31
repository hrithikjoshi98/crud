from django.shortcuts import render

def home(request):
    return render(request, 'crud_model_form/home.html')