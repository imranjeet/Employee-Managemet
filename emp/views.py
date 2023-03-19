from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Emp, Testimonial
from .form import FeedbackForm

# Create your views here.


def emp_home(request):
    emps = Emp.objects.all()

    return render(request, 'emp/home.html', {"emps": emps})


def add_emp(request):
    if request.method == "POST":

        # data fetch
        emp_name = request.POST.get('emp_name')
        emp_id = request.POST.get('emp_id')
        emp_phone = request.POST.get('emp_phone')
        emp_address = request.POST.get('emp_address')
        emp_working = request.POST.get('emp_working')
        emp_department = request.POST.get('emp_department')

        # create model object and set data
        e = Emp()
        e.name = emp_name
        e.emp_id = emp_id
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True

        # save the object
        e.save()

        # prepare msg

        print("Data is comming")
        return redirect('/emp/home/')
    return render(request, 'emp/add_emp.html', {})


def delete_emp(request, emp_id):
    emp = Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect('/emp/home/')


def update_emp(request, emp_id):
    emp = Emp.objects.get(pk=emp_id)
    return render(request, 'emp/update_emp.html', {"emp": emp})


def do_update_emp(request, emp_id):
    if request.method == "POST":
        # data fetch
        emp_name = request.POST.get('emp_name')
        empId = request.POST.get('emp_id')
        emp_phone = request.POST.get('emp_phone')
        emp_address = request.POST.get('emp_address')
        emp_working = request.POST.get('emp_working')
        emp_department = request.POST.get('emp_department')

        e = Emp.objects.get(pk=emp_id)

        e.name = emp_name
        e.emp_id = empId
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True

        # save the object
        e.save()

    return redirect('/emp/home/')


def testimonials(request):
    testi = Testimonial.objects.all()
    return render(request, 'emp/testimonials.html', {"testi": testi})

def feedback(request):
    if request.method == "POST":
        form=FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            print("data saved")
        else:
            return render(request, 'emp/feedback.html', {"form": form}) 
    else: 
        form=FeedbackForm()
        return render(request, 'emp/feedback.html', {"form": form})
