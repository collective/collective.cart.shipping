from collective.cart.shipping.tests.base import IntegrationTestCase


class ShippingMethodTestCase(IntegrationTestCase):

    def setUp(self):
        self.portal = self.layer['portal']
        from plone.app.testing import TEST_USER_ID
        from plone.app.testing import setRoles
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_subclass(self):
        from Products.ATContentTypes.content.base import ATCTContent
        from collective.cart.shipping.content.shipping import ShippingMethod
        self.assertTrue(issubclass(ShippingMethod, ATCTContent))

    def create_instance(self):
        instance = self.portal[self.portal.invokeFactory('ShippingMethod', 'shipping-method',
            title=u'Shipping Method', description=u'Description of Shipping Method',
             to_country=u'FI', min_delivery_days=5, max_delivery_days=10)]
        instance.reindexObject()
        return instance

    def test_instance(self):
        from collective.cart.shipping.content.shipping import ShippingMethod
        instance = self.create_instance()
        self.assertIsInstance(instance, ShippingMethod)

    def test_id(self):
        instance = self.create_instance()
        self.assertEqual(instance.id, 'shipping-method')

    def test_title(self):
        instance = self.create_instance()
        self.assertEqual(instance.Title(), u'Shipping Method')

    def test_description(self):
        instance = self.create_instance()
        self.assertEqual(instance.Description(), u'Description of Shipping Method')

    def test_to_country(self):
        instance = self.create_instance()
        self.assertEqual(instance.to_country, ('FI',))

    def test_min_delivery_days(self):
        instance = self.create_instance()
        self.assertEqual(instance.min_delivery_days, 5)

    def test_max_delivery_days(self):
        instance = self.create_instance()
        self.assertEqual(instance.max_delivery_days, 10)

    def test_shipping_fee(self):
        instance = self.create_instance()
        self.assertEqual(instance.shipping_fee()(7.0), 7.0)

    def test_shipping_fee_update(self):
        instance = self.create_instance()
        script = """
def shipping_fee(weight):
    return weight * 2

return shipping_fee
"""
        instance.getField('shipping_fee').set(instance, script)
        self.assertEqual(instance.shipping_fee()(7.0), 14.0)
