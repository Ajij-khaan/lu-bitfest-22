
from django.shortcuts import redirect, render
from mainapp.models import TransportUser
from transport.forms import BusSignForm, RouteSignForm, UpdateProfileForm
from django.contrib import messages
from django.views import View
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import BusInfo, RouteInfo


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
