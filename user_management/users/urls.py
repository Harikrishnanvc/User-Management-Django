from django.urls import path
from .views import RegisterUser, UserLogin, student_view, editor_view, admin_view,staff_view, sign_out

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('student/', student_view, name='student'),
    path('editor/', editor_view, name='editor'),
    path('admin/', admin_view, name='admin'),
    path('staff/', staff_view, name='staff'),
    path('logout/', sign_out, name='logout')
]