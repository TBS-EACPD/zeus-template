from zeus.i18n import WatchingTextMakerCreator

en_global_keys = {}

fr_global_keys = {}

text_files = [
    "proj/main.text.yaml",
]


def tdt(text, *args, **kwargs):
    """
    To Do Text

    Use this while prototyping to avoid spreading easily forgotten string accross the app
    When you're finished, it's easy to search for all `tdt` instances
    """
    return text


tm = WatchingTextMakerCreator(
    {"en": en_global_keys, "fr": fr_global_keys}, text_files
).get_tm_func()
