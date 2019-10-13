from contacts.models import Phone, Social, Address, Email
from documents.models import DocumentCategory


def context_info(request):
    phone = Phone.objects.first()
    address = Address.objects.first()
    email = Email.objects.first()
    socials = Social.objects.all()

    main_doc_category = DocumentCategory.objects.filter(is_active=True).first()

    context = {
        'phone': phone,
        'address': address,
        'email': email,
        'socials': socials,
        'main_doc_category': main_doc_category,
    }

    return context