from urllib.parse import parse_qs, urlencode

from django import template
from django.urls import reverse
from django.utils.translation import activate, get_language

from proj.text import tm as text_maker

register = template.Library()


@register.filter()
@register.simple_tag()
def tm(key, **kwargs):
    return text_maker(key, extra_keys=kwargs)


@register.simple_tag(takes_context=True)
def other_lang_href(context):
    cur_url = context.request.resolver_match
    querystring = ""
    # Temporary solution for reverse()
    if cur_url.namespace:
        cur_url.url_name = f"{cur_url.namespace}:{cur_url.url_name}"
    if context.request.GET:
        # need to mutate it, QueryDict is immutable
        params = context.request.GET.dict()
        if params.get("next"):
            params["next"] = "/fr/".join(params["next"].split("/en/"))
        querystring = f"?{urlencode(params)}"
    if get_language() == "en":
        activate("fr")
        url = reverse(cur_url.url_name, kwargs=cur_url.kwargs) + querystring
        activate("en")
    else:
        activate("en")
        url = reverse(cur_url.url_name, kwargs=cur_url.kwargs) + querystring
        activate("fr")
    return url
