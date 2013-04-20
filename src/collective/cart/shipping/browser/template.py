from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

import types


class ShippingMethodView(BrowserView):
    """View for content type: ShippingMethod"""

    __call__ = ViewPageTemplateFile('templates/shipping-method.pt')

    def shipping_fee_for_one_kg(self):
        shipping_fee = self.context.getField('shipping_fee').get(self.context)
        if isinstance(shipping_fee, types.FunctionType):
            return shipping_fee(1.0)
        return shipping_fee
