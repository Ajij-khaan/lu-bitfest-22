
import imp
from django.shortcuts import redirect, render
from consumer.views import *
from django.views import View
from .forms import UpdateProfileTeacherForm, UpdateProfileStudentForm
from mainapp.models import ConsumerUser, TransportUser
from django.contrib import messages
from django.http import HttpResponseRedirect
from transport.models import BusInfo, UpdateStudentProfile, UpdateTransportProfile, RouteInfo
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
    bus = BusInfo.objects.all()
    c = 0
    for x in numpass:
        if x.mainslot.Route_Number == 4:
            y = x.numberofpass
            c = c+y

    print(c)

    for cap in bus:
        p = c % cap.capacity

    print(p)

    busforr4 = BusInfo.objects.all()[:p]
    print(busforr4)
    route_4_count = busforr4.count()
    print(route_4_count)
    missing_bus_route_4 = p - route_4_count

    print(missing_bus_route_4)

    # Route 3

    numpass = NumberOfPassenger.objects.all()
    bus = BusInfo.objects.all()
    t = 0
    for x in numpass:
        if x.mainslot.Route_Number == 3:
            y = x.numberofpass
            t = t+y

    print(t)

    for cap in bus:
        p1 = t % cap.capacity

    print(p1)

    busforr3 = BusInfo.objects.all()[:p1]
    print(busforr3)
    route_3_count = busforr3.count()
    print(route_3_count)
    missing_bus_route_3 = p - route_3_count

    print(missing_bus_route_3)

    # Route 3

    numpass = NumberOfPassenger.objects.all()
    bus = BusInfo.objects.all()
    m = 0
    for x in numpass:
        if x.mainslot.Route_Number == 2:
            y = x.numberofpass
            m = m+y

    print(m)

    for cap in bus:
        p2 = m % cap.capacity

    print(p2)

    busforr2 = BusInfo.objects.all()[:p2]
    print(busforr2)
    route_2_count = busforr2.count()
    print(route_2_count)
    missing_bus_route_2 = p - route_2_count

    print(missing_bus_route_2)

    # Rout1
    numpass = NumberOfPassenger.objects.all()
    bus = BusInfo.objects.all()
    l = 0
    for x in numpass:
        if x.mainslot.Route_Number == 2:
            y = x.numberofpass
            l = l+y

    print(l)

    for cap in bus:
        p3 = l % cap.capacity

    print(p3)

    busforr1 = BusInfo.objects.all()[:p3]
    print(busforr1)
    route_1_count = busforr1.count()
    print(route_1_count)
    missing_bus_route_1 = p - route_1_count

    print(missing_bus_route_1)

    return render(request, 'num_of_pass.html', {'busforr4': busforr4, 'route_4_count': route_4_count, 'missing_bus_route_4': missing_bus_route_4, 'busforr3': busforr3, 'route_3_count': route_3_count, 'missing_bus_route_3': missing_bus_route_3, 'busforr2': busforr2, 'route_2_count': route_2_count, 'missing_bus_route_2': missing_bus_route_2, 'busforr1': busforr1, 'route_1_count': route_1_count, 'missing_bus_route_1': missing_bus_route_1, 'updateprofilestudent': 'updateprofilestudent', 'updateprofileteacher': 'updateprofileteacher'})
