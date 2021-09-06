
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
   

    path('viewproject/<str:longnameurl>', views.viewproject_view,name='viewproject'),
    path('downloadproject/<str:longnameurl>', views.downloadproject_view,name='downloadproject'),
    path('all-projects-by-lazycoder', views.showallproject_view,name='all-projects-by-lazycoder'),
    path('paid-projects-by-lazycoder', views.showpaidproject_view,name='paid-projects-by-lazycoder'),
    path('free-projects-by-lazycoder', views.showfreeproject_view,name='free-projects-by-lazycoder'),
    path('terms', views.terms_view,name='terms'),
    path('search', views.search_view,name='search'),
    path('privacy', views.privacy_view,name='privacy'),
    path('refund', views.refund_view,name='refund'),
    path('aboutus', views.aboutus_view,name='aboutus'),
    path('contactus', views.contactus_view,name='contactus'),
    

    path('logout', LogoutView.as_view(template_name='coder/logout.html'),name='logout'),
]
