from django.shortcuts import redirect

# to check if the user is login or not
def unauthenticated_user(view_function):
    def wrapper_function(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_function(request,*args,**kwargs)        
    return wrapper_function


# give access to admin id the request comes from the admin otherwise the access is given to normal page for normal user
def admin_only(view_function):
    def wapper_function(request,*args,**kwargs):
        if request.user.is_staff:
            return view_function(request,*args,**kwargs)
        else:
            return redirect('/')
    return wapper_function