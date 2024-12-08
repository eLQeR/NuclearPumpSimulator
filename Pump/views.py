from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pump
from .forms import PumpForm, PumpControlForm


def index(request):
    return render(request, 'index.html')

def pump_list(request):
    pumps = Pump.objects.all()
    return render(request, 'pump_list.html', {'pumps': pumps, 'user_role': request.user.role})


@login_required
def pump_list(request):
    pumps = Pump.objects.all()
    return render(request, 'pump_list.html', {'pumps': pumps, 'user_role': request.user.role})


@login_required
def pump_detail(request, pk):
    pump = get_object_or_404(Pump, pk=pk)
    logs = pump.logs.order_by('-timestamp')
    return render(request, 'pump_detail.html', {'pump': pump, 'logs': logs})


@permission_required('Pump.add_pump', raise_exception=True)
def pump_create(request):
    if request.method == 'POST':
        form = PumpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pump_list')
    else:
        form = PumpForm()
    return render(request, 'pump_form.html', {'form': form})


@permission_required('Pump.change_pump', raise_exception=True)
def pump_update(request, pk):
    pump = get_object_or_404(Pump, pk=pk)
    if request.method == 'POST':
        form = PumpForm(request.POST, instance=pump)
        if form.is_valid():
            form.save()
            return redirect('pump_detail', pk=pk)
    else:
        form = PumpForm(instance=pump)
    return render(request, 'pump_form.html', {'form': form})


@permission_required('Pump.delete_pump', raise_exception=True)
def pump_delete(request, pk):
    pump = get_object_or_404(Pump, pk=pk)
    if request.method == 'POST':
        pump.delete()
        return redirect('pump_list')
    return render(request, 'pump_confirm_delete.html', {'pump': pump})

def pump_control(request, pk):
    pump = get_object_or_404(Pump, pk=pk)
    if request.method == 'POST':
        form = PumpControlForm(request.POST, instance=pump)
        if form.is_valid():
            form.save()
            return redirect('pump_detail', pk=pk)
    else:
        form = PumpControlForm(instance=pump)
    return render(request, 'pump_control.html', {'form': form, 'pump': pump})
