from django.shortcuts import render,redirect
from .models import Order
from .forms import OrderForm

def viewhygio(request):
    form=OrderForm(request.POST or None)
    if form.is_valid():
        order=form.save(commit=False)
        order.save()
    return render(request,'orders/index.html',{'form':form})


# Create your views here.
