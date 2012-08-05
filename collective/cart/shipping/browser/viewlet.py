from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.cart.shipping.browser.form import ShippingMethodForm
from collective.cart.shipping.browser.interfaces import ICollectiveCartShippingLayer
from five import grok
from plone.app.layout.globals.interfaces import IViewView
from plone.app.layout.viewlets.interfaces import IAboveContent
from plone.z3cform.layout import FormWrapper
from zope.interface import Interface


grok.templatedir('viewlets')


class ShippingMethodFormWrapper(FormWrapper):

    form = ShippingMethodForm
    index = ViewPageTemplateFile("viewlets/formwrapper.pt")


class ShippingMethodViewlet(grok.Viewlet):
    """Viewlet to show updating shipping method form."""
    grok.context(Interface)
    grok.layer(ICollectiveCartShippingLayer)
    grok.name('collective.cart.shipping.shipping-method')
    grok.require('zope2.View')
    grok.template('shipping-method')
    grok.view(IViewView)
    grok.viewletmanager(IAboveContent)

    def form(self):
        return ShippingMethodFormWrapper(self.context, self.request)()
