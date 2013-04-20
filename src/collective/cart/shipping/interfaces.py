from collective.cart.shipping.schema import OrderShippingMethodSchema
from collective.cart.shipping.schema import ShippingMethodContainerSchema
from collective.cart.shipping.schema import ShippingMethodSchema
from plone.dexterity.interfaces import IDexterityContainer
from zope.interface import Attribute


class IShippingMethodContainer(ShippingMethodContainerSchema, IDexterityContainer):
    """Interface for content type: collective.cart.shipping.ShippingMethodContainer"""


class IShippingMethod(ShippingMethodSchema):
    """Interface for content type: ShippingMethod"""


class IOrderShippingMethod(OrderShippingMethodSchema, IDexterityContainer):
    """Interface for content type: collective.cart.shipping.OrderShippingMethod"""

    title = Attribute(u'Title')
    min_delivery_days = Attribute(u"Minimum Delivery Days")
    max_delivery_days = Attribute(u"Maximum Delivery Days")
    gross = Attribute(u'Gross Fee')
    net = Attribute(u'Net Fee')
    vat = Attribute(u'VAT Fee')
    vat_rate = Attribute(u'VAT Rate')
    weight_dimension_rate = Attribute(u'Weight Dimension Rate')
