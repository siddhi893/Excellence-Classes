# tuition_app/views.py
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from .models import StudentRegistration

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
            'name', 'phone', 'address', 'branch', 'standard', 
            'board', 'subject', 'school', 'fees', 'payment_mode', 'payment_proof'
        ))
        for student in students_list:
            if student['payment_proof']:
                # Convert the relative file path to an absolute URL
                student['payment_proof'] = request.build_absolute_uri('/media/' + student['payment_proof'])
        return JsonResponse({'students': students_list})

    context = {
        'students': students,
        'total_students': total_students,
    }
    return render(request, 'tuition_app/filter_students.html', context)