from django.shortcuts import render
from django.views import View
from contacts.models import Schedule, MapCode, Phone, Address, Email
from feedback.forms import FeedBackForm
from pages.models import Page


class ContactsView(View):
    def get(self, request):
        map_code = MapCode.objects.first()
        shedule = Schedule.objects.all()
        phones = Phone.objects.all()
        addresses = Address.objects.all()
        emails = Email.objects.all()

        feedback_form = FeedBackForm()

        contacts_page = Page.objects.filter(is_active=True, action='contacts').first()

        context = {
            'map_code': map_code,
            'shedule': shedule,
            'phones': phones,
            'addresses': addresses,
            'emails': emails,
            'feedback_form': feedback_form,
            'contacts_page': contacts_page,
        }

        lo = 'lo/' if request.session.get('is_lo') else ''
        return render(request, lo + 'contacts/contacts.html', context)