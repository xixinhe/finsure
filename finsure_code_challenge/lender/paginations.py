from rest_framework_json_api.pagination import JsonApiPageNumberPagination

class LenderPagination(JsonApiPageNumberPagination):
    page_size = 5
    page_query_param = 'page_number'
    max_page_size = 5