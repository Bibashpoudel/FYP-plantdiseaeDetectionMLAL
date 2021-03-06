

from django.urls import path
from .views import view_my_profile, loginPage, register, loginPage
from posts.views import PostDeleteView, PostUpdateView


app_name = 'account'

urlpatterns = [
    # path('register', views.register, name='register'),
    path('/', view_my_profile, name="myprofile"),
    path('/login', loginPage, name="login"),
    path('/register', register, name='register'),
    path('/logout', loginPage, name='logout'),
    path('post/<pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<pk>/update/', PostUpdateView.as_view(), name='post-update'),
]
