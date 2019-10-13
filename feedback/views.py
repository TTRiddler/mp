from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from feedback.forms import FeedBackForm
from feedback.models import FeedBack
from core.models import MailToString


class FeedBackView(View):
    def post(self, request):
        feedback_form = FeedBackForm(request.POST)
        sended = 0

        if feedback_form.is_valid():
            if request.recaptcha_is_valid:
                current_site = get_current_site(request)
                mail_subject = 'Новое сообщение на сайте: ' + current_site.domain
                message = render_to_string('feedback/feedback_message.html', {
                    'domain': current_site.domain,
                    'email': request.POST.get('email'),
                    'name': request.POST.get('name'),
                    'text': request.POST.get('text'),
                })
                to_email = MailToString.objects.first().email
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                feedback_form.save()
                sended = 1 
        else:
            sended = None
            
        context = {
            'sended': sended,
        }

        return JsonResponse(context)
