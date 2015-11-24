# -*- coding: utf-8 -*- 
from django.shortcuts import render
from courses.models import Course, Lesson
from django.http import HttpResponse

def detail(request, course_id):
	cour = Course.objects.get(id = course_id)
	lesn = Lesson.objects.filter(course = course_id)
	return render(request, 'courses/detail.html', {'course': cour, 'lesson': lesn})

