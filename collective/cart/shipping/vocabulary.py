from decimal import Decimal
from decimal import ROUND_HALF_UP
from five import grok
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


class VATsVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        registry = getUtility(IRegistry)
        vats = registry['collective.behavior.vat.VAT']
        terms = []

        if vats:
            for vat in vats:
                vat = Decimal(vat).quantize(
                    Decimal('.01'), rounding=ROUND_HALF_UP)
                vat_percent = '{} %'.format(str(vat))
                terms.append(
                    SimpleVocabulary.createTerm(
                        str(vat), vat, vat_percent))

        return SimpleVocabulary(terms)


grok.global_utility(VATsVocabulary, name=u"collective.cart.shipping.vats")
