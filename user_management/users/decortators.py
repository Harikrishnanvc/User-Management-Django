from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def role_required(role):
    def decorator(view_func):
        @login_required
        def wrapper(request, *args, **kwargs):
            if request.user.user_role == role:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('login')
        return wrapper
    return decorator