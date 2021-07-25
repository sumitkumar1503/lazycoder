
from django.contrib import admin
from django.urls import path
from coder import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),


    path('adminlogin', LoginView.as_view(template_name='coder/adminlogin.html'),name='adminlogin'),
    path('customerlogin', LoginView.as_view(template_name='coder/customerlogin.html'),name='customerlogin'),

    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('donate', views.donate_view,name='donate'),

    path('logout', LogoutView.as_view(template_name='coder/logout.html'),name='logout'),
]