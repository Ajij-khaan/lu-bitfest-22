
import imp
from django.shortcuts import redirect, render
from consumer.views import *
from django.views import View
from .forms import UpdateProfileTeacherForm, UpdateProfileStudentForm
from mainapp.models import ConsumerUser, TransportUser
from django.contrib import messages
from django.http import HttpResponseRedirect
from transport.models import UpdateStudentProfile, UpdateTransportProfile, RouteInfo
from .forms import RequestBusForm
from transport.models import SendMeessage, NumberOfPassenger


class HomeConsumerView(View):
    def get(self, request):
        consumer = request.session.get('consumer')
        user_transport = ConsumerUser.objects.get(user_name=consumer)
        transpost = request.session.get('consumer')
        if transpost:
            allroute = RouteInfo.objects.all()[::-1]

            try:
                updateprofileteacher = UpdateTransportProfile.objects.get(
                    user_transport=user_transport)
                print(updateprofileteacher)
            except:
                updateprofileteacher = None

            try:
                updateprofilestudent = UpdateStudentProfile.objects.get(
                    user_consumer=user_transport)
                print(updateprofilestudent)

            except:
                updateprofilestudent = None
            return render(request, 'routeshowconsumer.html', {'updateprofileteacher': updateprofileteacher, 'updateprofilestudent': updateprofilestudent, 'allroute': allroute})
        else:
            return redirect("/")


class AddProfileView(View):
    def get(self, request):

        consumer = request.session.get('consumer')
        user_transport = ConsumerUser.objects.get(user_name=consumer)
        try:
            updateprofileteacher = UpdateTransportProfile.objects.get(
                user_transport=user_transport)

        except:
            updateprofileteacher = None

        try:
            updateprofilestudent = UpdateStudentProfile.objects.get(
                user_consumer=user_transport)

        except:
            updateprofilestudent = None

        if consumer:
            if user_transport.role == "Teacher":
                form = UpdateProfileTeacherForm()
                return render(request, 'profile.html', {'form': form, 'updateprofileteacher': updateprofileteacher})
            elif (user_transport.role == "Student"):
                form = UpdateProfileStudentForm()
                return render(request, 'profile.html', {'form': form, 'updateprofilestudent': updateprofilestudent})
        else:
            return redirect("/")

    def post(self, request):
        consumer = request.session.get('consumer')
        user_transport = ConsumerUser.objects.get(user_name=consumer)
        if consumer:
            if user_transport.role == "Teacher":
                form = UpdateProfileTeacherForm(request.POST)
                if form.is_valid():
                    obj = form.save(commit=False)
                    obj.user_transport = user_transport
                    obj.save()
                    messages.success(request, 'Successfully Saved')
                    form.save()

                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            elif (user_transport.role == "Student"):
                form = UpdateProfileStudentForm(request.POST)
                if form.is_valid():
                    obj = form.save(commit=False)
                    obj.user_consumer = user_transport
                    obj.save()
                    messages.success(request, "Sucessfully Saved")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            return redirect("/")

        return render(request, 'profile.html', {'form': form})


def showprofilfe(request):
    consumer = request.session.get('consumer')
    user_transport = ConsumerUser.objects.get(user_name=consumer)
    try:
        updateprofileteacher = UpdateTransportProfile.objects.get(
            user_transport=user_transport)

    except:
        updateprofileteacher = None

    try:
        updateprofilestudent = UpdateStudentProfile.objects.get(
            user_consumer=user_transport)

    except:
        updateprofilestudent = None

    return render(request, 'profileshow.html', {'updateprofileteacher': updateprofileteacher, 'updateprofilestudent': updateprofilestudent})


class RequestBusView(View):
    def get(self, request):
        consumer = request.session.get('consumer')
        user_transport = ConsumerUser.objects.get(user_name=consumer)
        form = RequestBusForm()
        try:
            updateprofileteacher = UpdateTransportProfile.objects.get(
                user_transport=user_transport)

        except:
            updateprofileteacher = None

        try:
            updateprofilestudent = UpdateStudentProfile.objects.get(
                user_consumer=user_transport)

        except:
            updateprofilestudent = None

        return render(request, 'requestbus.html', {'form': form, 'updateprofileteacher': updateprofileteacher, 'updateprofilestudent': updateprofilestudent})

    def post(self, request):
        consumer = request.session.get('consumer')
        print(consumer)
        username = ConsumerUser.objects.get(user_name=consumer)

        form = RequestBusForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = username
            obj.save()
            messages.success(request, 'Successfully Saved')
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def notifiactionbus(request):
    consumer = request.session.get('consumer')

    username = ConsumerUser.objects.get(user_name=consumer)

    mymessage = SendMeessage.objects.filter(request_user=username)

    return render(request, 'notification.html', {'mymessage': mymessage})


def notdelete(request, id):
    maindel = SendMeessage.objects.get(id=id)
    maindel.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def number_of_passeneger(request):
    consumer = request.session.get('consumer')
    user_transport = ConsumerUser.objects.get(user_name=consumer)
    try:
        updateprofileteacher = UpdateTransportProfile.objects.get(
            user_transport=user_transport)

    except:
        updateprofileteacher = None

    try:
        updateprofilestudent = UpdateStudentProfile.objects.get(
            user_consumer=user_transport)

    except:
        updateprofilestudent = None
    numpass = NumberOfPassenger.objects.all()
    return render(request, 'num_of_pass.html', {'numpass': numpass, 'updateprofilestudent': 'updateprofilestudent', 'updateprofileteacher': 'updateprofileteacher'})
