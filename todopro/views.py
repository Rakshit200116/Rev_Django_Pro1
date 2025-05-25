from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth.models import User
from todopro.models import TODOModel
from django.contrib.auth import authenticate,login,logout


def signUp(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        fname=request.POST.get('fnam')
        email = request.POST.get('email')
        pas = request.POST.get('Pwd')
        myuser = User.objects.create_user(fname,email,pas)
        myuser.save()
        return redirect('/loginpage')

    return render(request,'signup.html')
        
def loginfunc (request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        fname=request.POST.get('fnam')
        pas = request.POST.get('Pwd')
        userr = authenticate(request,username = fname,password = pas)
        if userr is not None:
            login(request,userr)
            return redirect('/todopage')
        else:
            return redirect('/loginpage')

    return render(request,'loginpage.html')

def todopage(request):
    if request.user.is_authenticated:
        fname = request.user.username
        task = TODOModel.objects.filter(user = request.user.id)
        if request.method == 'POST':
            title = request.POST.get('tit')
            TODOModel.objects.create(title = title,user = request.user)
            return redirect('/todopage')
        return render(request,'todo.html',{'users':fname,'task':task})
    else:
        return redirect('/loginpage')

def delete(request,title):
    task = get_object_or_404(TODOModel,title = title)
    task.delete()
    return redirect('/todopage')