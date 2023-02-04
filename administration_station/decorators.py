from django.http import HttpResponse
from django.shortcuts import redirect

# Stops the user from going to the login page
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('parish-admin-home')
        else:
            return view_func(request, *args, **kwargs)


    return wrapper_func
def allowed_users_parish_home(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0]
                print("Group: ", group)
                print(allowed_roles)
                if str(group) in allowed_roles:
                    print("in")
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect('parish-admin-home')
            else:
                return redirect('login')
        return wrapper_func
    return decorator

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0]
                print("Group: ", group)
                print(allowed_roles)
                if str(group) in allowed_roles:
                    print("in")
                    return view_func(request, *args, **kwargs)
                else:
                    return redirect('parish-admin-home')
            else:
                return redirect('home')
        return wrapper_func
    return decorator