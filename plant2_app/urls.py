from django.urls import path
from . import views #local import
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('razorpay/', views.Razorpay, name='razorpay'),
    path('razorpay/done/', views.done, name='done'),
    path('reset_password/',auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
