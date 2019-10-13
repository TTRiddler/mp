from contacts.models import Phone, Social, Address, Email


def context_info(request):
    phone = Phone.objects.first()
    address = Address.objects.first()
    email = Email.objects.first()
    socials = Social.objects.all()

    context = {
        'phone': phone,
        'address': address,
        'email': email,
        'socials': socials,
    }

    return context