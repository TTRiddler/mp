from django.core.paginator import Paginator


def pagination(queryset, page_number, item_per_page):
    item_per_page = item_per_page
    paginator = Paginator(queryset, item_per_page)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page=%s' % page.previous_page_number()
    else:
        prev_url = '' 
    
    if page.has_next():
        next_url = '?page=%s' % page.next_page_number()
    else:
        next_url = '' 

    return is_paginated, page, next_url, prev_url