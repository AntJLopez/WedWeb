from guests.models import Guest
from slugify import slugify
from django.db.utils import IntegrityError


def run(*args):
    for guest in Guest.objects.all():
        if (guest.username and len(guest.username) == 10 and
                guest.username.isupper()):
            guest.username = None
        if all(not v for v in [
                guest.username, guest.lead_partner, guest.parent]):
            # Guest needs a username and has none
            unum = 0
            trying = True
            while(trying):
                try:
                    guest.username = guest.first_name.lower()
                    if unum > 0:
                        guest.username += str(unum)
                    trying = False
                    guest.save()
                except IntegrityError:
                    unum += 1
        if guest.username:
            guest.username = slugify(guest.username)
        guest.save()
