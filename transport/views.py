
from urllib import request
from urllib.request import Request
from django.shortcuts import redirect, render
from mainapp.models import TransportUser
from transport.forms import BusSignForm, RouteSignForm, SendMessageForm, AddpassForm, BusStopageForm
from django.contrib import messages
from django.views import View
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import BusInfo, RouteInfo, NumberOfPassenger, BusStopage
from consumer.models import RequestBus


# Bus Info


class BusHomeView(View):
    def get(self, request):
        transpost = request.session.get('transport')
        if transpost:
            allbus = BusInfo.objects.all()[::-1]
            return render(request, 'busshow.html', {'allbus': allbus})
        else:
            return redirect('/')


class AddBusView(View):
    def get(self, request):
        transpost = request.session.get('transport')
        if transpost:
            form = BusSignForm()
            return render(request, 'addbus.html', {'form': form})
        else:
            return redirect('/')

    def post(self, request):
        form = BusSignForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Successfully Saved')
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        return render(request, 'addbus.html', {'form': form})


class EditBusInfo(View):

    def get(self, request, id):
        transpost = request.session.get('transport')
        if transpost:
            pi = BusInfo.objects.get(id=id)
            form = BusSignForm(instance=pi)
            return render(request, 'update_bus.html', {'form': form})
        else:
            return redirect('/')

    def post(self, request, id):
        pi = BusInfo.objects.get(id=id)
        form = BusSignForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations!! Updated Successfully')
            return redirect('/transport')
        else:
            messages.warning(request, 'Not Updated')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class DeleteBusInfo(View):
    def get(self, request, id):
        transpost = request.session.get('transport')
        if transpost:
            businfo = BusInfo.objects.get(id=id)
            businfo.delete()
            messages.success(request, "delete successfully")
            return redirect("/transport")
        else:
            return redirect("/")


# Route Info

class RouteallView(View):
    def get(self, request):
        transpost = request.session.get('transport')
        if transpost:
            allroute = RouteInfo.objects.all()[::-1]
            return render(request, 'routeshow.html', {'allroute': allroute})
        else:
            return redirect("/")


class AddRouteView(View):
    def get(self, request):
        transpost = request.session.get('transport')
        if transpost:
            form = RouteSignForm()
            return render(request, 'addroute.html', {'form': form})
        else:
            return redirect("/")

    def post(self, request):
        form = RouteSignForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Successfully Saved')
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        return render(request, 'addroute.html', {'form': form})


class EditRouteInfo(View):

    def get(self, request, id):
        transpost = request.session.get('transport')
        if transpost:
            pi = RouteInfo.objects.get(id=id)
            form = RouteSignForm(instance=pi)
            return render(request, 'update_route.html', {'form': form})
        else:
            return redirect("/")

    def post(self, request, id):
        pi = RouteInfo.objects.get(id=id)
        form = RouteSignForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations!! Updated Successfully')
            return redirect('/allroute')
        else:
            messages.warning(request, 'Not Updated')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class DeleteRouteInfo(View):
    def get(self, request, id):
        transpost = request.session.get('transport')
        if transpost:
            businfo = RouteInfo.objects.get(id=id)
            businfo.delete()
            messages.success(request, "delete successfully")
            return redirect("/allroute")
        else:
            return redirect("/")


def logout(request):
    transpost = request.session.get('transport')
    if transpost:
        del request.session['transport']
        return redirect("/")
    else:
        return redirect("/")


class ShowrequestView(View):
    def get(self, request):
        transpost = request.session.get('transport')
        if transpost:
            allrequest = RequestBus.objects.all()
            return render(request, 'requestbusshow.html', {'allrequest': allrequest})
        else:
            return redirect("/")


class AddmessageView(View):
    def get(self, request, id):
        transpost = request.session.get('transport')
        myrquest = RequestBus.objects.get(id=id)
        if transpost:
            form = SendMessageForm()
            return render(request, 'send_message.html', {'form': form})
        else:
            return redirect("/")

    def post(self, request, id):
        form = SendMessageForm(request.POST)
        myrquest = RequestBus.objects.get(id=id)
        if form.is_valid():

            obj = form.save(commit=False)
            obj.request_user = myrquest.user
            obj.root = myrquest.root_bus
            obj.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        return render(request, 'send_message.html', {'form': form})


class AddpassView(View):
    def get(self, request):
        transpost = request.session.get('transport')
        if transpost:
            form = AddpassForm()
            return render(request, 'numberofpass.html', {'form': form})
        else:
            return redirect("/")

    def post(self, request):
        form = AddpassForm(request.POST)

        if form.is_valid():
            messages.success(request, "successfully saved")
            form.save()

            return redirect("NumberOfPassengerview")

        return render(request, 'numberofpass.html', {'form': form})


class AddBustopageView(View):
    def get(self, request):
        transpost = request.session.get('transport')
        if transpost:
            form = BusStopageForm()
            return render(request, 'add_bus_stopage.html', {'form': form})
        else:
            return redirect("/")

    def post(self, request):
        form = BusStopageForm(request.POST)

        if form.is_valid():
            messages.success(request, "successfully saved")
            form.save()

            return redirect("busstopageview")

        return render(request, 'add_bus_stopage.html', {'form': form})


def busstopageview(request):
    busstopage = BusStopage.objects.all()
    return render(request, 'bustopageview.html', {'busstopage': busstopage})


class EditBusstopageInfo(View):

    def get(self, request, id):
        transpost = request.session.get('transport')
        if transpost:
            pi = BusStopage.objects.get(id=id)
            form = BusStopageForm(instance=pi)
            return render(request, 'updatebusstopage.html', {'form': form})
        else:
            return redirect("/")

    def post(self, request, id):
        pi = BusStopage.objects.get(id=id)
        form = BusStopageForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations!! Updated Successfully')
            return redirect('busstopageview')
        else:
            messages.warning(request, 'Not Updated')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class DeleteBusstopageInfo(View):
    def get(self, request, id):
        transpost = request.session.get('transport')
        if transpost:
            businfo = BusStopage.objects.get(id=id)
            businfo.delete()
            messages.success(request, "delete successfully")
            return redirect("allroute")
        else:
            return redirect("/")


def NumberOfPassengerview(request):
    numpass = NumberOfPassenger.objects.all()
    return render(request, 'num_of_passenger.html', {'numpass': numpass})


class EditPasenegerInfo(View):

    def get(self, request, id):
        transpost = request.session.get('transport')
        if transpost:
            pi = NumberOfPassenger.objects.get(id=id)
            form = AddpassForm(instance=pi)
            return render(request, 'updatepass.html', {'form': form})
        else:
            return redirect("/")

    def post(self, request, id):
        pi = NumberOfPassenger.objects.get(id=id)
        form = AddpassForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations!! Updated Successfully')
            return redirect('NumberOfPassengerview')
        else:
            messages.warning(request, 'Not Updated')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class DeletePassenegerInfo(View):
    def get(self, request, id):
        transpost = request.session.get('transport')
        if transpost:
            businfo = NumberOfPassenger.objects.get(id=id)
            businfo.delete()
            messages.success(request, "delete successfully")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect("/")
