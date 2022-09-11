
from django.shortcuts import redirect, render
from transport.forms import BusSignForm
from django.contrib import messages
from django.views import View
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import BusInfo


class BusHomeView(View):
    def get(self, request):
        allbus = BusInfo.objects.all()[::-1]
        return render(request, 'busshow.html', {'allbus': allbus})


class AddBusView(View):
    def get(self, request):
        form = BusSignForm()
        return render(request, 'addbus.html', {'form': form})

    def post(self, request):
        form = BusSignForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Successfully Saved')
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        return render(request, 'addbus.html', {'form': form})


class EditBusInfo(View):

    def get(self, request, id):
        pi = BusInfo.objects.get(id=id)
        form = BusSignForm(instance=pi)
        return render(request, 'update_bus.html', {'form': form})

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
        businfo = BusInfo.objects.get(id=id)
        businfo.delete()
        messages.success(request, "delete successfully")
        return redirect("/transport")
