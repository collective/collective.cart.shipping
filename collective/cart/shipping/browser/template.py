from collective.cart.shipping.browser.interfaces import ICollectiveCartShippingLayer
from collective.cart.shipping.interfaces import IShippingMethod
from five import grok

import types


grok.templatedir('templates')


class ShippingMethodView(grok.View):
    grok.context(IShippingMethod)
    grok.layer(ICollectiveCartShippingLayer)
    grok.name('view')
    grok.require('zope2.View')
    grok.template('shipping-method')

    def shipping_fee_for_one_kg(self):
        shipping_fee = self.context.getField('shipping_fee').get(self.context)
        if isinstance(shipping_fee, types.FunctionType):
            return shipping_fee(1.0)
        return shipping_fee
