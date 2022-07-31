from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import render_to_string


def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        mobile = request.POST.get('mobile', None)
        message = request.POST.get('message', None)
        if not email or not message or not mobile:
            return redirect('home')
        else:
            merge_data = {
                'name': name, 'email': email, 'message': message, 'mobile': mobile
            }
            subject = f"Email Send By {name}:{email}"
            html_body = render_to_string("email/send_contact_email.html", merge_data)
            msg = EmailMultiAlternatives(subject=subject, from_email=settings.EMAIL_HOST_USER,
                                         to=[email])
            msg.attach_alternative(html_body, "text/html")
            msg.send(fail_silently=True)
        return redirect('thank_you')


def thank_you(request):
    return render(request, 'pages/thankyou.html')
