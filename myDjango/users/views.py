from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def registerUser (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users/register_success.html')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})