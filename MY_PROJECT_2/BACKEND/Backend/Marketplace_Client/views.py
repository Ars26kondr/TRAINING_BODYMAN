from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import Customer_Registration_form
from django.urls import reverse_lazy

def Main_page(r):
    return render(r, 'Main_page.html', )
def Registration(r):
    return render(r, 'SignUp.html', )
class Register_User_View(CreateView):
    form_class=Customer_Registration_form
    template_name='Register_User_View.html'
    success_url=reverse_lazy('Main_page')