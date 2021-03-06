from django.db.models import get_model


def import_model(path):
    """
    Passed a string "app.Model", will return Model registered inside app.
    """
    split = path.split('.')
    return get_model(split[0], split[-1]) # <app>.contrib[.bla].<model>
