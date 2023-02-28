from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('specs', views.specs, name='specs'),
    path('workers', views.workers, name='workers'),
    path('builds', views.builds, name='builds'),
    path('contacts', views.contacts, name='contacts'),
    path('specs/<int:pk>', views.ProductView.as_view(), name='db-detail')
]