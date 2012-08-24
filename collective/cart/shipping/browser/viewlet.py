from collective.cart.shipping.browser.interfaces import ICollectiveCartShippingLayer
from collective.cart.shipping.browser.wrapper import ShippingMethodFormWrapper
from five import grok
from plone.app.layout.globals.interfaces import IViewView
from plone.app.layout.viewlets.interfaces import IAboveContent
from zope.component import getUtility
from zope.interface import Interface
from zope.schema.interfaces import IVocabularyFactory


grok.templatedir('viewlets')


class ShippingMethodViewlet(grok.Viewlet):
    """Viewlet to show updating shipping method form."""
    grok.context(Interface)
    grok.layer(ICollectiveCartShippingLayer)
    grok.name('collective.cart.shipping.shipping-method')
    grok.require('zope2.View')
    grok.template('shipping-method')
    grok.view(IViewView)
    grok.viewletmanager(IAboveContent)

    _form_wrapper = ShippingMethodFormWrapper

    def form(self):
        return self._form_wrapper(self.context, self.request)()

    def available(self):
        return len(getUtility(
            IVocabularyFactory,
            name="collective.cart.shipping.methods").__call__(self.context))
