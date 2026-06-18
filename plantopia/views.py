from django.shortcuts import render
    
def home(request):
    return render(request,template_name='Index.html')
           
            
def login_view(request):
    return render(request, 'login.html') 

def signup_view(request):
    return render(request, 'signup.html')              