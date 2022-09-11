from pyexpat.errors import messages
from re import M
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import TransportSignForm, ConsumerUserForm
# Create your views here.
from .models import ConsumerUser, TransportUser
from django.contrib import messages


class LoginTransportView(View):
    return_url = None

    def get(self, request):
        LoginTransportView.return_url = request.GET.get('return_url')
        return render(request, 'login_transport.html', {'login_transport': 'active'})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        transport = TransportUser.get_transport_by_username(username)

        if transport:
            flag = check_password(password, transport.password)
            if flag:
                request.session['transport'] = transport.username
                return redirect('/transport')
            else:
                messages.warning(request, "Email Or Password Invalid")
        else:
            messages.warning(request, "Email Or Password Invalid")

        return render(request, 'login_transport.html')


class RegisterTransportView(View):
    def get(self, request):
        form = TransportSignForm()
        return render(request, 'register_transport.html', {'form': form})

    def post(self, request):
        form = TransportSignForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            cpassword = form.cleaned_data['cpassword']
            if password != cpassword:
                messages.warning(request, 'Password Not Match')
            else:
                mypassword = make_password(password)
                mypassword1 = make_password(cpassword)
                obj = form.save(commit=False)
                obj.password = mypassword
                obj.cpassword = mypassword1
                obj.save()
                messages.success(request, 'Successfully Saved')
                form.save()
                return redirect("transport_login")
        return render(request, 'register_transport.html', {'form': form})


class LoginConsumerView(View):
    return_url = None

    def get(self, request):
        LoginTransportView.return_url = request.GET.get('return_url')
        return render(request, 'login_consumer.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        transport = ConsumerUser.get_consumer_by_username(username)

        if transport:
            flag = check_password(password, transport.password)
            if flag:
                request.session['consumer'] = transport.user_name
                return redirect('/consumer')
            else:
                messages.warning(request, "Email Or Password Invalid")
        else:
            messages.warning(request, "Email Or Password Invalid")

        return render(request, 'login_consumer.html')


class RegisterConsumerView(View):
    def get(self, request):
        form = ConsumerUserForm()
        return render(request, 'register_consumer.html', {'form': form})

    def post(self, request):
        form = ConsumerUserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            cpassword = form.cleaned_data['cpassword']
            if password != cpassword:
                messages.warning(request, 'Password Not Match')
            else:
                mypassword = make_password(password)
                mypassword1 = make_password(cpassword)
                obj = form.save(commit=False)
                obj.password = mypassword
                obj.cpassword = mypassword1
                obj.save()
                messages.success(request, 'Successfully Saved')
                form.save()

        return render(request, 'register_consumer.html', {'form': form})
