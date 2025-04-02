# tuition_app/views.py
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import StudentRegistration
from django.shortcuts import get_object_or_404


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
        

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'tuition_app/success.html')
    else:
        form = StudentRegistrationForm()
    return render(request, 'tuition_app/registration.html', {'form': form})

@login_required
def filter_students(request):
    standard = request.GET.get('standard', '')
    board = request.GET.get('board', '')
    school = request.GET.get('school', '')
    branch = request.GET.get('branch', '')

    students = StudentRegistration.objects.all()

    if standard:
        students = students.filter(standard=standard)
    if board:
        students = students.filter(board=board)
    if school:
        students = students.filter(school=school)
    if branch:
        students = students.filter(branch=branch)

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