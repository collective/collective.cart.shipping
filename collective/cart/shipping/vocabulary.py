from Products.CMFCore.utils import getToolByName
from collective.cart.shipping.interfaces import IShippingMethod
from decimal import Decimal
from decimal import ROUND_HALF_UP
from five import grok
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.component.hooks import getSite
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
                        str(vat), str(vat), vat_percent))

        return SimpleVocabulary(terms)


grok.global_utility(VATsVocabulary, name=u"collective.cart.shipping.vats")


class ShippingMethodsVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        catalog = getToolByName(getSite(), 'portal_catalog')
        brains = catalog({
            'object_provides': IShippingMethod.__identifier__,
        })
        terms = [
        SimpleVocabulary.createTerm(
            brain.UID, brain.UID, brain.Title) for brain in brains]

        return SimpleVocabulary(terms)


grok.global_utility(ShippingMethodsVocabulary, name=u"collective.cart.shipping.methods")
