from dateutil.parser import parse


def convert_to_iso_date(date_str):
    """
    The date format sent from the API is in the from dd/mm/yyyy but it is
    required to be in the form YYYY-mm-dd by `iso-8601`. This function assists
    to do the convertions.
    """
    return parse(date_str, dayfirst=True).strftime('%Y-%m-%d')
