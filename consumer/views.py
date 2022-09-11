
import imp
from django.shortcuts import redirect, render
from consumer.views import *
from django.views import View
from .forms import UpdateProfileTeacherForm, UpdateProfileStudentForm
from mainapp.models import ConsumerUser, TransportUser
from django.contrib import messages
from django.http import HttpResponseRedirect
from transport.models import UpdateStudentProfile, UpdateTransportProfile


class HomeConsumerView(View):
    def get(self, request):
        consumer = request.session.get('consumer')
        user_transport = ConsumerUser.objects.get(user_name=consumer)
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
        return render(request, 'home.html', {'updateprofileteacher': updateprofileteacher, 'updateprofilestudent': updateprofilestudent})


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
