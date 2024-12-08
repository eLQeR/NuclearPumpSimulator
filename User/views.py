from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required

from .forms import UserEditForm
from .models import User

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

@login_required
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user_detail.html', {'user': user})

@login_required
@permission_required('auth.change_user', raise_exception=True)
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Змініть на вашу сторінку списку користувачів
    else:
        form = UserEditForm(instance=user)
    return render(request, 'user_edit.html', {'form': form, 'user': user})

@login_required
@permission_required('auth.delete_user', raise_exception=True)
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')  # Повертає на список користувачів
    return render(request, 'user_confirm_delete.html', {'user': user})