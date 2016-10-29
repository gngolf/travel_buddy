from django.shortcuts import render, redirect
from .models import Users, Plans
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'travel/index.html')

def register(request):
    username = request.POST.get("username_up")
    email = request.POST.get("email_up")
    password = request.POST.get("pwd_up").encode()
    confirmpassword = request.POST.get("passwordconf_up").encode()
    info = Users.UserManager.regUser(username, email, password)
    if info[0] is True:
        request.session['name'] = username
        return redirect('/welcome')

    else:
        if Users.UserManager.validuser(username):
            messages.error(request, 'Username is not long enough!!', extra_tags='username')

        if Users.UserManager.validemail(email):
            messages.error(request, 'Email is not valid', extra_tags='email')

        if Users.UserManager.validemail(password):
            messages.error(request, 'Password must be at least 8 characters!!', extra_tags='password')

        if Users.UserManager.matchpasswords(password, confirmpassword):
            messages.error(request, 'Password Confirmation doesn\'t match!!', extra_tags='passwordconfirm')
        return redirect('/')


def login(request):
    username = request.POST.get("username_in")
    password = request.POST.get('pwd_in').encode()
    Users.UserManager.logUser(username, password)

    if Users.UserManager.logUser(username, password):
        request.session['name'] = request.POST['username_in']

        context = {
            "name": Users.UserManager.filter(username=username, password=password).last()
        }
        return redirect('/welcome', context)
    else:
        if Users.UserManager.validuser(username):
            messages.error(request, 'Username is not long enough!!', extra_tags='username_in')
        if Users.UserManager.validemail(password):
            messages.error(request, 'Password must be at least 8 characters!!', extra_tags='password_in')
        return redirect('/')


def welcome(request):
	context = {
		'plans': Plans.objects.all()
	}
	return render(request, 'travel/welcome.html', context)


def add(request):
	return render(request, 'travel/add.html')


def create(request):
	Plans.objects.create(destination=request.POST['new_dest'], plan=request.POST['new_desc'], start=request.POST['new_start'], end=request.POST['new_end'])
	return redirect('/welcome')

def info(request, id):
	request.session['current_row'] = id
	row = Plans.objects.filter(id=id)[0]
	context = {
		'destination': row.destination,
		'description': row.plan,
		'start': row.start,
		'end': row.end
	}
	return render(request, 'travel/info.html', context)

def logout(request):
	request.session.clear()
	return redirect('/')

