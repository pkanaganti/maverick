from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.views import password_change, password_change_done

app_name = 'crm'
urlpatterns = [

    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    # url(r'^signup/$', signup, {'post_change_redirect': '/signup/done/'}, name='signup'),
    url(r'^password-change/$', password_change, {'post_change_redirect': '/password-change/done/'}, name='password_change'),
    url(r'^password-change/done/$', password_change_done, name='password_change_done'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('service_list', views.service_list, name='service_list'),
    path('service/create/', views.service_new, name='service_new'),
    path('service/<int:pk>/edit/', views.service_edit, name='service_edit'),
    path('service/<int:pk>/delete/', views.service_delete, name='service_delete'),
    path('product_list', views.product_list, name='product_list'),
    path('product/create/', views.product_new, name='product_new'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('customer/<int:pk>/summary/', views.summary, name='summary'),
]
