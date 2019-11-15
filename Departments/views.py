from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404
from .models import Department
from .forms import DepartmentCreationForm


# Create your views here.
@login_required(login_url='account/login/')
def index(request):
    name = 'departments'
    current_user = request.user
    if request.method == 'POST':
        form = departmentCreationForm(request.POST)
        if form.is_valid():
            department = form.save(commit=False)
            department.user = current_user
            department.save()
            return redirect('home')
        else:
           form = DepartmentCreationForm()
        return render(request,
                      'department.html', 
                      {"user":current_user,
                        "comment_form":form}
                )
   

    