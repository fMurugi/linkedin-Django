from django.urls import path

from . import views

urlpatterns = [
    path('home',views.HomeView.as_view()),
    # path('authorize',views.AuthorizedView.as_view(),name='home'),
    path('login',views.LoginInterfaceView.as_view()),
    path('logout',views.LogoutInterfaceView.as_view()),
]