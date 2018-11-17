from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django_countries import countries
from .models import Guest, Activity, RSVP, INVITED_THRESHOLD
from .forms import RSVPForm  # noqa


class InvitedFilter(admin.SimpleListFilter):
    title = _('Invited Status')
    parameter_name = 'invited'

    def lookups(self, request, model_admin):
        return (
            ('yes', _('Invited')),
            ('no', _('Not Invited')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(percentile__gte=INVITED_THRESHOLD)
        if self.value() == 'no':
            return queryset.filter(percentile__lt=INVITED_THRESHOLD)


class PartyRoleFilter(admin.SimpleListFilter):
    title = _('Party Role')
    parameter_name = 'party_role'

    def lookups(self, request, model_admin):
        return (
            ('leader', _('Leader')),
            ('partner', _('Partner')),
            ('child', _('Child')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'leader':
            return queryset.filter(lead_partner=None, parent=None)
        if self.value() == 'partner':
            return queryset.filter(lead_partner__isnull=False)
        if self.value() == 'child':
            return queryset.filter(parent__isnull=False)


class CountryFilter(admin.SimpleListFilter):
    title = _('Country')
    parameter_name = 'country'

    def lookups(self, request, model_admin):
        c_dict = dict(countries)
        g_countries = set(g.country for g in model_admin.model.objects.all())
        country_list = [(c, c_dict[c]) for c in g_countries if c in c_dict]
        special_filters = [
            ('none', _('No Country')),
            ('no_kw', _('Not Kuwait')),
            ('no_us_kw', _('Not US or Kuwait')),
        ]
        return special_filters + country_list

    def queryset(self, request, queryset):
        if self.value():
            if self.value() == 'none':
                return queryset.filter(country="")
            if self.value() == 'no_us_kw':
                return queryset.exclude(
                    country='US').exclude(country='KW')
            if self.value() == 'no_kw':
                return queryset.exclude(country='KW')
            return queryset.filter(country=self.value())


class AddressFilter(admin.SimpleListFilter):
    title = _('Complete Address')
    parameter_name = 'complete_address'

    def lookups(self, request, model_admin):
        return (
            ('yes', _('Complete')),
            ('no', _('Incomplete')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.exclude(thoroughfare="")
        if self.value() == 'no':
            return queryset.filter(thoroughfare="")


class RSVPFilter(admin.SimpleListFilter):
    title = _('RSVP Status')
    parameter_name = 'rsvp'

    def lookups(self, request, model_admin):
        return (
            ('accepted', _('Accepted')),
            ('declined', _('Declined')),
            ('no_reply', _('No Reply')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'no_reply':
            return queryset.filter(rsvp__isnull=True)

        # We're not looking for blank RSVPs, so can filter them out
        queryset = queryset.filter(rsvp__isnull=False)
        if self.value() == 'accepted':
            return queryset.filter(rsvp__attending=True)
        if self.value() == 'declined':
            return queryset.filter(rsvp__attending=False)


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'invited', 'username', 'is_lead', )
    list_per_page = 1000
    list_filter = (
        InvitedFilter,
        PartyRoleFilter,
        RSVPFilter,
        CountryFilter,
        AddressFilter, )
    search_fields = [
        'username',
        'first_name', 'last_name',
        'lead_partner__first_name', 'lead_partner__last_name',
        'parent__first_name', 'parent__last_name',
    ]


@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    form = RSVPForm
    list_display = ('__str__', 'attending', 'party_size', 'nights_onsite',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    pass
