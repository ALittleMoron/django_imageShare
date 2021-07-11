from django.urls import path

from .views import (HomePage, Account, AddImage, UserLogin, user_logout,
                    UserRegister)


urlpatterns = [
    path('', HomePage.as_view(), name='imagesApp.homePage'),
    path('account/<str:user_name>', Account.as_view(), name='imagesApp.account'),
    path('add-image', AddImage.as_view(), name='imagesApp.addImage'),
    path('register', UserRegister.as_view(), name='imagesApp.register'),
    path('login', UserLogin.as_view(), name='imagesApp.login'),
    path('logout', user_logout, name='imagesApp.logout'),
]