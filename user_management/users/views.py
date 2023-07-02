from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import View

from .decortators import role_required
from .users_registration_form import RegistrationForm, RegistrationFormFields


class RegisterUser(View):
    def get(self, request):
        form = RegistrationFormFields()
        return render(request, 'user_register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.password = make_password(password)
            user.save()
            return redirect('login')
        return render(request, 'user_register.html', {'form': form})


class UserLogin(View):
    ROLE_URL_MAPPING = {
        'student': 'student',
        'staff': 'staff',
        'admin': 'admin',
        'editor': 'editor',
    }

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            role = user.user_role
            if role in self.ROLE_URL_MAPPING:
                role_url = self.ROLE_URL_MAPPING[role]
                print(role_url)
                return redirect(f'{role_url}')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'login.html')


@role_required('editor')
def editor_view(request):
    context = {'user': request.user}
    return render(request, 'editor.html', context)

@role_required('student')
def student_view(request):
    context = {'user': request.user}
    return render(request, 'student.html', context)


@role_required('admin')
def admin_view(request):
    context = {'user': request.user}
    return render(request, 'admin.html', context)


@role_required('staff')
def staff_view(request):
    context = {'user': request.user}
    return render(request, 'staff.html', context)

def sign_out(request):
    logout(request)
    return redirect('register')