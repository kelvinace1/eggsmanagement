from django.shortcuts import render
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form':form
    }
    return render(request, "users/register.html", context)