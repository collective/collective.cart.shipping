from collective.cart.shipping.content import ShippingMethodContainer
from collective.cart.shipping.content import OrderShippingMethod
from collective.cart.shipping.interfaces import IShippingMethodContainer
from collective.cart.shipping.interfaces import IOrderShippingMethod
from plone.dexterity.content import Container
from plone.dexterity.interfaces import IDexterityContainer
from zope.interface.verify import verifyObject

import unittest


class ShippingMethodContainerTestCase(unittest.TestCase):
    """TestCase for content type: collective.cart.shipping.ShippingMethodContainer"""

    def test_subclass(self):
        from collective.cart.shipping.schema import ShippingMethodContainerSchema
        self.assertTrue(issubclass(ShippingMethodContainer, Container))
        self.assertTrue(issubclass(IShippingMethodContainer, (ShippingMethodContainerSchema, IDexterityContainer)))

    def test_instance__verifyObject(self):
        self.assertTrue(verifyObject(IShippingMethodContainer, ShippingMethodContainer()))


class OrderShippingMethodTestCase(unittest.TestCase):
    """TestCase for content type: collective.cart.shipping.OrderShippingMethod"""

    def test_subclass(self):
        from collective.cart.shipping.schema import OrderShippingMethodSchema
        self.assertTrue(issubclass(OrderShippingMethod, Container))
        self.assertTrue(issubclass(IOrderShippingMethod, (OrderShippingMethodSchema, IDexterityContainer)))

    def test_instance__verifyObject(self):
        self.assertTrue(verifyObject(IOrderShippingMethod, OrderShippingMethod()))
