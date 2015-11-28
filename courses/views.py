from django.shortcuts import render, get_object_or_404
from courses.models import Course, Lesson

def detail(request, course_id):
    courses = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.all()
    return render (request, 'courses/detail.html',{'courses':courses,'lessons':lessons})