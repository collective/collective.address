# -*- coding: utf-8 -*-
from collective.address import _pycountry
from Products.CMFPlone.utils import safe_unicode
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

import pycountry


@implementer(IVocabularyFactory)
class CountryVocabulary(object):
    """Vocabulary factory for countries regarding to ISO3166.
    """

    def __call__(self, context, query=None):
        items = [
                    SimpleTerm(value=it.numeric, title=safe_unicode(it.name))
                    for it in pycountry.countries
                    if query is None
                    or safe_unicode(query.lower()) in safe_unicode(it.name.lower())  # noqa
                ]
        return SimpleVocabulary(items)


CountryVocabularyFactory = CountryVocabulary()


def get_pycountry_name(country_id):
    if not country_id:
        return None
    country = pycountry.countries.get(numeric=country_id)
    return _pycountry(country.name)
