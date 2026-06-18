from django.contrib import admin
from django.urls import path
from plantopia import views as b_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('' ,b_views.home, name ='home'),
     path ('login/' ,b_views.login_view, name ='login'),
    path ('signup/' ,b_views.signup_view, name ='signup'),

]
