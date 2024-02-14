from django.urls import path
from . import views
from members.views import login_user

app_name = 'members'
urlpatterns = [
    path('login_user',views.login_user,name="login"),
]
