from django.template.defaultfilters import register


@register.filter(name='get_from_dict')
def get_from_dict(dictionary, key):
    return dict.get(dictionary, key)

