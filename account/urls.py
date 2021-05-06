from django.urls import path
from account.views import (

        registration_view,

)

app_name = 'account'

urlpatterns = [
    path('', registration_view, name='register'),
]