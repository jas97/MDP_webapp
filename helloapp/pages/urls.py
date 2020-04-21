from django.urls import path

from .views import homeRequest, valueFuncRequest

urlpatterns = [
    path('', homeRequest, name='home'), # Na prazno mapira homepageview
    path('val/<int:dim>/<int:start>/<int:goal>', valueFuncRequest)
]