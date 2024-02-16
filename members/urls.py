from django.urls import path
from . import views
from members.views import login_user

app_name = 'members'
urlpatterns = [
    path('login_user',views.login_user,name="login"),
    path('logout_user',views.logout_user, name='logout'),
    path('register_user',views.register_user, name='register_user'),
]
