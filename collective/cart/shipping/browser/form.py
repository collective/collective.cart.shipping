from collective.cart.shipping.schema import IShippingMethodSchema
from five import grok
from plone.directives import form
from zope.interface import Interface
from z3c.form import button
from collective.cart.shipping import _


class ShippingMethodForm(form.SchemaForm):
    grok.context(Interface)
    grok.name('shipping-method-form')
    grok.require('zope2.View')

    ignoreContext = True
    schema = IShippingMethodSchema

    @button.buttonAndHandler(_(u'Update'))
    def handleApply(self, action):
        data, errors = self.extractData()
