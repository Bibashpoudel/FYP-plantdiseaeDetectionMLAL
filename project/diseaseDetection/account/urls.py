


from django.urls  import path
from .views import view_my_profile


app_name = 'account'

urlpatterns = [
    # path('register', views.register, name='register'),
    path('/', view_my_profile, name="myprofile" )
]