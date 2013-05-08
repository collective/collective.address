from plone.memoize import instance
from zope.interface import directlyProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
import pycountry
from Products.CMFPlone.utils import safe_unicode


@instance.memoize
def CountryVocabulary(context):
    """Vocabulary factory for countries regarding to ISO3166.
    """
    items = [(safe_unicode(it), it.numeric) for it in pycountry.countries]
    return SimpleVocabulary.fromItems(items)
directlyProvides(CountryVocabulary, IVocabularyFactory)
