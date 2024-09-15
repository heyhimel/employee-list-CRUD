from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import *
from django.core.paginator import Paginator

# Create your views here.

# home
def home(request):
    if request.method == "POST":
        nme = request.POST.get('empName')
        date = request.POST.get('empBirthDate')
        mail = request.POST.get('empEmail')
        phon = request.POST.get('empNum')

        #searching data by filter (insensitive)
        #all html input field must be filld
        # employeesRecord = addEmployeeTable.objects.filter(
        #     Q(empName__icontains=nme) |
        #     Q(empBirthDate=date) |
        #     Q(empEmail__icontains=mail) |
        #     Q(empNum=phon)
        # )

        
        # not mandatory to fill all html input field
        # Start with an empty Q object
        query = Q()

        # Add filters only if input is provided for that field
        if nme:
            query |= Q(empName__icontains=nme)
        if date:
            query |= Q(empBirthDate=date)
        if mail:
            query |= Q(empEmail__icontains=mail)
        if phon:
            query |= Q(empNum=phon)

        # Apply the constructed query
        employeesRecord = addEmployeeTable.objects.filter(query)
        
    #simply data record show
    else:
        employeesRecord = addEmployeeTable.objects.all()

    # Set up pagination with 4 records per page
    paginator = Paginator(employeesRecord, 4)
    page_number = request.GET.get('page')
    employeesRecord = paginator.get_page(page_number)
        
    return render(request, 'home.html',{'employeesData': employeesRecord})


# add employee record
def addEmployee(request):
    if request.method == "POST":
        img = request.FILES.get('imgFile')
        nme = request.POST.get('name')
        date = request.POST.get('date')
        mail = request.POST.get('email')
        phon = request.POST.get('phone')

        #print(nme,date,mail)
        # Create and save the new employee record
        new_employee = addEmployeeTable(
            imageFile=img,
            empName=nme,
            empBirthDate=date,
            empEmail=mail,
            empNum=phon
        )
        new_employee.save()
        messages.success(request, 'Employee added successfully!')

        #return redirect('add-employee')
    return render(request, 'addEmployee.html')


#showing employees data with sort property
def employees(request):
    #sorting data record show
    if request.method == "POST":
        sortType = request.POST.get('dropdown_value')
        
        employeesRecord = addEmployeeTable.objects.all().order_by(sortType)

    #simply data record show
    else:
        employeesRecord = addEmployeeTable.objects.all()

    return render(request, 'employe.html', {'employeesData': employeesRecord})


# deleting employee record
def delEmployee(request, empID):
    if request.method == "POST":
        # Get the employee record by ID (passed from the URL)
        employee = get_object_or_404(addEmployeeTable, id = empID)
        # Delete the employee record
        employee.delete()

        return redirect('homepage')
    
# editing employee record
def editEmployee(request, empID):
    #getting the targeted object
    #we can use here filter(query)
    employee = get_object_or_404(addEmployeeTable, id = empID)

    #new updated value receiving 
    if request.method == "POST":
        employee.empName = request.POST.get('empName')
        employee.empBirthDate = request.POST.get('empBirthDate')
        employee.empEmail = request.POST.get('empEmail')
        employee.empNum = request.POST.get('empNum')

        if request.FILES.get('imageFile'):
            employee.imageFile = request.FILES.get('imageFile')

        employee.save()

    return render(request, 'editEmployee.html', {'employee':employee})