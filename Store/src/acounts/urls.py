from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='acounts'
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('profile/<str:username>', views.my_profile, name='my_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('edit_my_profile/<str:username>', views.edit_my_profile, name='edit_my_profile'),

    #for enter your Email
    path('reset_password', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_email.html'),name='password_reset'),
    #for send message SECECCESS
    path('reset_password_done', auth_views.PasswordResetDoneView.as_view(template_name='password_change_done.html'),name='password_reset_done'),
    #to change your password
    path('reset/<uid64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    #send message to tell you password Changed
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
]
