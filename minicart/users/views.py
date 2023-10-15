from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import View,TemplateView
from store.models import Product

# Create your views here.

class CustHomeView(TemplateView):
    template_name="cust-home.html"
    # def get(self,request):
    #     return render(request,"cust-home.html")
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Product.objects.all()
        return context
    
