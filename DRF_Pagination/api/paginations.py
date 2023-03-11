from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size=5
    page_query_param='p'
    page_size_query_param='records'
    max_page_size=8
    # last_page_strings='end'