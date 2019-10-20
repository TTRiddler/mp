from contacts.models import Phone, Social, Address, Email
from documents.models import DocumentCategory
from pages.models import Page


def context_info(request):
    phone = Phone.objects.first()
    address = Address.objects.first()
    email = Email.objects.first()
    socials = Social.objects.all()

    main_doc_category = DocumentCategory.objects.filter(is_active=True).first()

    pages = Page.objects.filter(is_active=True).exclude(action='home')

    all_docs = DocumentCategory.objects.filter(is_active=True)

    context = {
        'phone': phone,
        'address': address,
        'email': email,
        'socials': socials,
        'main_doc_category': main_doc_category,
        'pages': pages,
        'all_docs': all_docs,
    }

    return context