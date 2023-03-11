from email.policy import default
from rest_framework.pagination import LimitOffsetPagination

class MyOffSetPagination(LimitOffsetPagination):
    default_limit=5
    limit_query_param='mylimit'
    offset_query_param='myoffset'
    max_limit=7