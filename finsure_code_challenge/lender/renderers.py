from rest_framework_csv.renderers import CSVRenderer

class LenderCsvRenderer(CSVRenderer):

    header = ['name', 'code', 'upfront_commission_rate', 'trial_commission_rate', 'active']
    media_type = 'text/csv'