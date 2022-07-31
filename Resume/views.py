from django.shortcuts import render

from about.models import About
from achievement.models import Achievement, ExtraCurricular
from education.models import Education
from experience.models import Experience
from portfolio.models import Portfolio
from skills.models import Skills


def home(request):
    abouts = About.objects.first()
    education = Education.objects.all().order_by('-id')
    skills = Skills.objects.all().order_by('-id')
    experience = Experience.objects.all().order_by('-id')
    achievements = Achievement.objects.all().order_by('-id')
    extracurriculars = ExtraCurricular.objects.all().order_by('-id')
    portfolio = Portfolio.objects.all().order_by('-id')

    context = {
        'education': education,
        'skills': skills,
        'experiences': experience,
        'achievements': achievements,
        'extracurriculars': extracurriculars,
        'about': abouts,
        'portfolios': portfolio
    }

    return render(request, 'index.html', context)
