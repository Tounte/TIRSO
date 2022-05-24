
from django.contrib import admin
from django.urls import path
from etat_stock import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', LoginView.as_view(redirect_authenticated_user=True),name='login'),
    path('logout', LogoutView.as_view(),name='logout'),
    path('',views.stock,name="etat_stock"),
    path('etat_stock',views.stock,name="etat_stock"),
    path('reception',views.reception,name="reception"),
    path('livraison',views.livraison,name="livraison"),
    path('avaries',views.avaries,name="avaries"),
]
