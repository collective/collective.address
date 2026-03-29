from collective.address import _
from collective.address.vocabulary import get_pycountry_name
from plone.app.content.interfaces import INameFromTitle
from plone.autoform import directives as form
from plone.autoform.interfaces import IFormFieldProvider
from plone.indexer import indexer
from plone.supermodel import model
from Products.CMFPlone import PloneMessageFactory as _PMF
from Products.CMFPlone.utils import safe_unicode
from z3c.form.interfaces import IAddForm
from z3c.form.interfaces import IEditForm
from zope import schema
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import provider

import six


class IAddressable(Interface):
    """Abstract marker interface."""


@provider(IFormFieldProvider)
class IAddress(model.Schema, IAddressable):
    """Address schema."""

    street = schema.TextLine(
        title=_("label_street", default="Street"),
        description=_("help_street", default="Enter the street and number."),
        required=False,
    )
    zip_code = schema.TextLine(
        title=_("label_zip_code", default="Postal Code"),
        description=_("help_zip_code", default="Enter the postal code."),
        required=False,
    )
    city = schema.TextLine(
        title=_("label_city", default="City"),
        description=_("help_city", default="Enter the city."),
        required=False,
    )
    country = schema.Choice(
        title=_("label_country", default="Country"),
        description=_("help_country", default="Select the country from the list."),
        required=False,
        vocabulary="collective.address.CountryVocabulary",
    )


@provider(IFormFieldProvider)
class IContact(model.Schema, IAddressable):
    """Contact schema."""

    email = schema.TextLine(
        title=_("label_email", default="Email"),
        description=_("help_email", default="Enter the email address."),
        required=False,
    )
    website = schema.URI(
        title=_("label_website", default="Website"),
        description=_("help_website", default="Enter the website URL."),
        required=False,
    )
    phone = schema.TextLine(
        title=_("label_phone", default="Phone"),
        description=_("help_phone", default="Enter the phone number."),
        required=False,
    )
    mobile = schema.TextLine(
        title=_("label_mobile", default="Mobile"),
        description=_("help_mobile", default="Enter the mobile phone number."),
        required=False,
    )
    fax = schema.TextLine(
        title=_("label_fax", default="Fax"),
        description=_("help_fax", default="Enter the fax number."),
        required=False,
    )


@provider(IFormFieldProvider)
class IPerson(model.Schema, IAddressable):
    """Person schema."""

    first_name = schema.TextLine(
        title=_("label_first_name", default="First Name"),
        description=_("help_first_name", default="Enter the first name."),
        required=False,
    )
    last_name = schema.TextLine(
        title=_("label_last_name", default="Last Name"),
        description=_("help_last_name", default="Enter the last name."),
        required=True,
    )
    academic_title = schema.TextLine(
        title=_("label_academic_titel", default="Academic title"),
        description=_("help_academic_title", default="Enter the academic title."),
        required=False,
    )

    title = schema.TextLine(
        title=_PMF("label_title", default="Title"), required=False, missing_value=""
    )
    description = schema.Text(
        title=_PMF("label_description", default="Summary"),
        description=_PMF(
            "help_description", default="Used in item listings and search results."
        ),
        required=False,
        missing_value="",
    )
    form.omitted("title", "description")
    form.no_omit(IEditForm, "description")
    form.no_omit(IAddForm, "description")


@provider(IFormFieldProvider)
class ISocial(model.Schema, IAddressable):
    """Social media schema."""

    facebook_url = schema.URI(
        title=_("label_facebook_url", default="Facebook URL"),
        description=_("help_facebook_url", default="Enter the Facebook URL."),
        required=False,
    )
    twitter_url = schema.URI(
        title=_("label_twitter_url", default="Twitter URL"),
        description=_("help_twitter_url", default="Enter the Twitter URL."),
        required=False,
    )
    google_plus_url = schema.URI(
        title=_("label_google_plus_url", default="Google Plus URL"),
        description=_("help_google_plus_url", default="Enter the Google Plus URL."),
        required=False,
    )
    instagram_url = schema.URI(
        title=_("label_instagram_url", default="Instagram URL"),
        description=_("help_instagram_url", default="Enter the Instagram URL."),
        required=False,
    )


@implementer(INameFromTitle)
@adapter(IPerson)
class NameFromPerson:
    """Adapter to generate a title from a person's name."""

    def __new__(cls, context):
        title = "{}{}{}".format(
            context.last_name, ", " if context.first_name else "", context.first_name
        )
        instance = super().__new__(cls)
        instance.title = title
        context.title = title
        return instance

    def __init__(self, context):
        pass


def _concat_and_utf8(*args):
    """Concats args with spaces between and returns utf-8 string, it does not
    matter if input was unicode or str.
    Taken from ``plone.app.contenttypes.indexers``
    """
    result = ""
    for value in args:
        if six.PY2 and isinstance(value, str):
            value = value.encode("utf-8", "replace")
        if value:
            result = " ".join((result, value))
    return result


# Text indexing
def searchable_text(obj):
    """Create a searchable text from addressable behavior fields."""
    items = []

    acc = IAddress(obj, None)
    if acc:
        items += [
            safe_unicode(acc.street) or "",
            safe_unicode(acc.zip_code) or "",
            safe_unicode(acc.city) or "",
            (
                safe_unicode(get_pycountry_name(acc.country)) if acc.country else ""
            ),  # noqa
        ]

    acc = IContact(obj, None)
    if acc:
        items += [
            safe_unicode(acc.email) or "",
            safe_unicode(acc.website) or "",
            safe_unicode(acc.phone) or "",
            safe_unicode(acc.mobile) or "",
            safe_unicode(acc.fax) or "",
        ]

    acc = IPerson(obj, None)
    if acc:
        items += [safe_unicode(acc.first_name) or "", safe_unicode(acc.last_name) or ""]

    ret = _concat_and_utf8(*items)
    return ret


@indexer(IAddressable)
def searchable_text_indexer(obj):
    return searchable_text(obj)
