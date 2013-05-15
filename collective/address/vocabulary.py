from plone.memoize import forever
from zope.interface import directlyProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
import pycountry
from Products.CMFPlone.utils import safe_unicode


@forever.memoize
def CountryVocabulary(context):
    """Vocabulary factory for countries regarding to ISO3166.
    """
    items = [SimpleTerm(value=it.numeric, title=safe_unicode(it.name))
             for it in pycountry.countries]
    return SimpleVocabulary(items)
directlyProvides(CountryVocabulary, IVocabularyFactory)


def get_pycountry_name(country_id):
    country = pycountry.countries.get(numeric=country_id)
    return country.name
