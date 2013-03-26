from five import grok
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


class VATRatesVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        terms = []

        for term in getUtility(IVocabularyFactory, name=u"collective.behavior.vat.rates")(context)._terms:
            terms.append(SimpleVocabulary.createTerm(str(term.value), term.token, term.title))

        return SimpleVocabulary(terms)


grok.global_utility(VATRatesVocabulary, name=u"collective.cart.shipping.rates")
