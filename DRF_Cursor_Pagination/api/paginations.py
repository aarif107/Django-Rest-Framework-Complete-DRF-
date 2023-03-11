from email.policy import default
from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):
    page_size=7
    ordering='name'
    cursor_query_param='cu'