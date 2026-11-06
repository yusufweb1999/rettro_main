from  datetime import datetime

def global_wb_info(request):
    """
    Adds global context variables to the template context.
    """
    return {
        'site_name': 'Zay Shop',
        'current_year': datetime.now().year,
    }