# tuition_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import StudentRegistration
from django.shortcuts import get_object_or_404
from .forms import *


def display(request):
    students_db = StudentRegistration.objects.all()
    
    students = []
    
    for student in students_db:
        stud = {
            "name" : student.name,
            "phone" : student.phone,
            "father_name" : student.father_name,
            "father_phone" : student.father_phone,
            "father_occ" : student.father_occupation,
            # "img" : student.img,
            "address" : student.address,
            "standard" : student.standard,
            "board" : student.board,
            "subject" : student.subject,
            "school" : student.school,
            "branch" : student.branch,
            "fees" : student.fees,
            "payment_mode" : student.payment_mode,
            # "payment+proof" : student.payment_proof,
        }
        
        students.append(stud)
        
    return JsonResponse({
        "students" : students
    })
        
def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tuition_app:registration_success')  # Using the URL name
    else:
        form = RegistrationForm()
    
    return render(request, 'tuition_app/registration.html', {'form': form})

def success_view(request):
    return render(request, 'tuition_app/success.html')

@login_required
def filter_students(request):
    standard = request.GET.get('standard', '')
    board = request.GET.get('board', '')
    school = request.GET.get('school', '')
    branch = request.GET.get('branch', '')
    search = request.GET.get('search')

    students = StudentRegistration.objects.all()

    if standard:
        students = students.filter(standard=standard)
    if board:
        students = students.filter(board=board)
    if school:
        students = students.filter(school=school)
    if branch:
        students = students.filter(branch=branch)
    if search:
        students = students.filter(name__icontains = search)

    total_students = students.count()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        students_list = list(students.values(
            'id',  # Added 'id' to use in the redirect URL
            'name', 'phone', 'address', 'branch', 'standard', 
            'board', 'subject', 'school', 'fees', 'payment_mode', 'payment_proof'
        ))
        for student in students_list:
            if student['payment_proof']:
                student['payment_proof'] = request.build_absolute_uri('/media/' + student['payment_proof'])
        return JsonResponse({'students': students_list})

    context = {
        'students': students,
        'total_students': total_students,
    }
    return render(request, 'tuition_app/filter_students.html', context)

@login_required
def student_detail(request, student_id):
    student = get_object_or_404(StudentRegistration, id=student_id)
    context = {
        'student': student,
    }
    return render(request, 'tuition_app/student_detail.html', context)


def delete_student(request, student_id):
    student = StudentRegistration.objects.get(id = student_id)
    student.delete()
    
    print(student_id)
    
    return redirect('/app/filter_students')


def update_student(request, student_id):
    student = StudentRegistration.objects.get(id = student_id)
    
    if request.method == "POST":
        data = request.POST
    
        name = data.get('name')
        phone = data.get('phone')
        address = data.get('address')
        branch = data.get('branch')
        standard = data.get('standard')
        board = data.get('board')
        subject = data.get('subject')
        school = data.get('school')
        fees = data.get('fees')
        payment_mode = data.get('payment_mode')
        # payment_proof = request.FILES.get('payment_proof')
        # img = request.FILES.get('img')
        
        #check code for image and payment image 
    
        student.name = name
        student.phone = phone
        student.address = address
        student.branch = branch
        student.standard = standard
        student.board = board
        student.subject = subject
        student.school = school
        student.fees = fees
        student.payment_mode = payment_mode
        
        # if payment_proof:
        #     student.payment_proof = payment_proof
            
        # if img:
        #     student.img = img
        
        student.save()
        
        url2 = "/app/student/" + str(student_id)
        
        return redirect(url2)
        
    
    context = {
        'student': student,
    }
    return render(request, 'tuition_app/student_detail.html', context)













    