from Products.CMFCore.utils import getToolByName
from collective.cart.shipping.tests.base import IntegrationTestCase


class TestSetup(IntegrationTestCase):

    def setUp(self):
        self.portal = self.layer['portal']

    def test_collective_cart_shipping_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('collective.cart.shipping'))

    def test_Products_ATCountryWidget_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('Products.ATCountryWidget'))

    def test_collective_behavior_vat_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('collective.behavior.vat'))

    def test_installed__plone_app_dexterity(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('plone.app.dexterity'))

    def test_browserlayer(self):
        from collective.cart.shipping.browser.interfaces import ICollectiveCartShippingLayer
        from plone.browserlayer import utils
        self.assertIn(ICollectiveCartShippingLayer, utils.registered_layers())

    def test_factorytool__ShippingMethod(self):
        factory = getToolByName(self.portal, 'portal_factory')
        self.assertTrue(factory.getFactoryTypes()['ShippingMethod'])

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-collective.cart.shipping:default'), u'0')

    def get_record(self, name):
        """Get record by name.
        :param name: Name of record.
        :type name: basestring

        :rtype: instance"""
        from plone.registry.interfaces import IRegistry
        from zope.component import getUtility
        return getUtility(IRegistry).records.get(name)

    def test_registry_record__collective_behavior_vat_VAT__field__instance(self):
        from plone.registry.field import List
        record = self.get_record('collective.behavior.vat.VAT')
        self.assertIsInstance(record.field, List)

    def test_registry_record__collective_behavior_vat_VAT__field__title(self):
        record = self.get_record('collective.behavior.vat.VAT')
        self.assertEqual(record.field.title, u'VAT')

    def test_registry_record__collective_behavior_vat_VAT__field__description(self):
        record = self.get_record('collective.behavior.vat.VAT')
        self.assertEqual(record.field.description, u'A list of VAT in %.')

    def test_registry_record__collective_behavior_vat_VAT__field__value_type(self):
        from plone.registry.field import Float
        record = self.get_record('collective.behavior.vat.VAT')
        self.assertIsInstance(record.field.value_type, Float)

    def test_registry_record__collective_behavior_vat_VAT__value(self):
        record = self.get_record('collective.behavior.vat.VAT')
        self.assertEqual(record.value, [23.0, 13.0, 9.0, 0.0])

    def test_rolemap__collective_cart_shipping_AddShippingMethod__rolesOfPermission(self):
        permission = "collective.cart.shipping: Add ShippingMethod"
        roles = [
            item['name'] for item in self.portal.rolesOfPermission(
                permission) if item['selected'] == 'SELECTED']
        roles.sort()
        self.assertEqual(roles, [
            'Contributor',
            'Manager',
            'Site Administrator'])

    def test_rolemap__collective_cart_shipping_AddShippingMethod__acquiredRolesAreUsedBy(self):
        permission = "collective.cart.shipping: Add ShippingMethod"
        self.assertEqual(
            self.portal.acquiredRolesAreUsedBy(permission), 'CHECKED')

    def test_site_properties__types_not_searchable__ShippingMethod(self):
        properties = getToolByName(self.portal, 'portal_properties')
        site_properties = getattr(properties, 'site_properties')
        self.assertIn(
            'ShippingMethod',
            site_properties.getProperty('types_not_searched'))

    def test_site_properties__types_not_searchable__collective_cart_shipping_CartShippingMethod(self):
        properties = getToolByName(self.portal, 'portal_properties')
        site_properties = getattr(properties, 'site_properties')
        self.assertIn(
            'collective.cart.shipping.CartShippingMethod',
            site_properties.getProperty('types_not_searched'))

    def test_propertiestool__navtree_properties__metaTypesNotToList__ShippingMethod(self):
        properties = getToolByName(self.portal, 'portal_properties')
        navtree_properties = getattr(properties, 'navtree_properties')
        self.assertIn(
            'ShippingMethod',
             navtree_properties.getProperty('metaTypesNotToList'))

    def test_propertiestool__navtree_properties__metaTypesNotToList__collective_cart_shipping_CartShippingMethod(self):
        properties = getToolByName(self.portal, 'portal_properties')
        navtree_properties = getattr(properties, 'navtree_properties')
        self.assertIn(
            'collective.cart.shipping.CartShippingMethod',
             navtree_properties.getProperty('metaTypesNotToList'))

    def get_type(self, name):
        types = getToolByName(self.portal, 'portal_types')
        return types.getTypeInfo(name)

    def test_types__ShippingMethod__meta_type(self):
        ctype = self.get_type('ShippingMethod')
        self.assertEqual(
            ctype.meta_type, 'Factory-based Type Information with dynamic views')

    def test_types__ShippingMethod__i18n_domain(self):
        ctype = self.get_type('ShippingMethod')
        self.assertEqual(
            ctype.i18n_domain, 'collective.cart.shipping')

    def test_types__ShippingMethod__title(self):
        ctype = self.get_type('ShippingMethod')
        self.assertEqual(
            ctype.title, 'Shipping Method')

    def test_types__ShippingMethod__description(self):
        ctype = self.get_type('ShippingMethod')
        self.assertEqual(
            ctype.description, '')

    def test_types__ShippingMethod__content_icon(self):
        ctype = self.get_type('ShippingMethod')
        self.assertEqual(
            ctype.icon_expr, 'string:${portal_url}/++resource++collective.cart.shipping/shipping.png')

    def test_types__ShippingMethod__content_meta_type(self):
        ctype = self.get_type('ShippingMethod')
        self.assertEqual(
            ctype.content_meta_type, 'ShippingMethod')

    def test_types__ShippingMethod__product(self):
        ctype = self.get_type('ShippingMethod')
        self.assertEqual(
            ctype.product, 'collective.cart.shipping')

    def test_types__ShippingMethod__factory(self):
        ctype = self.get_type('ShippingMethod')
        self.assertEqual(
            ctype.factory, 'addShippingMethod')

    def test_types__ShippingMethod__immediate_view(self):
        ctype = self.get_type('ShippingMethod')
        self.assertEqual(
            ctype.immediate_view, 'view')

    def test_types__ShippingMethod__global_allow(self):
        ctype = self.get_type('ShippingMethod')
        self.assertTrue(ctype.global_allow)

    def test_types__ShippingMethod__filter_content_types(self):
        ctype = self.get_type('ShippingMethod')
        self.assertFalse(ctype.filter_content_types)

    def test_types__ShippingMethod__allowed_content_types(self):
        ctype = self.get_type('ShippingMethod')
        self.assertEqual(
            ctype.allowed_content_types, ())

    def test_types__ShippingMethod__allow_discussion(self):
        ctype = self.get_type('ShippingMethod')
        self.assertFalse(ctype.allow_discussion)

    def test_types__ShippingMethod__default_view(self):
        ctype = self.get_type('ShippingMethod')
        self.assertEqual(
            ctype.default_view, 'view')

    def test_types__ShippingMethod__view_methods(self):
        ctype = self.get_type('ShippingMethod')
        self.assertEqual(
            ctype.view_methods, ('view',))

    def test_types__ShippingMethod__default_aliases(self):
        ctype = self.get_type('ShippingMethod')
        self.assertEqual(ctype.aliases, {
            'sharing': 'folder_localrole_form',
            'gethtml': '',
            '(Default)': '(dynamic view)',
            'edit': 'base_edit',
            'mkdir': '',
            'properties': 'base_metadata',
            'view': '(selected layout)'
        })

    def test_types__ShippingMethod__action__view__title(self):
        ctype = self.get_type('ShippingMethod')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.title, 'View')

    def test_types__ShippingMethod__action__view__condition(self):
        ctype = self.get_type('ShippingMethod')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.condition, '')

    def test_types__ShippingMethod__action__view__url_expr(self):
        ctype = self.get_type('ShippingMethod')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.getActionExpression(), 'string:${object_url}')

    def test_types__ShippingMethod__action__view__visible(self):
        ctype = self.get_type('ShippingMethod')
        action = ctype.getActionObject('object/view')
        self.assertTrue(action.visible)

    def test_types__ShippingMethod__action__view__permissions(self):
        ctype = self.get_type('ShippingMethod')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.permissions, (u'View',))

    def test_types__ShippingMethod__action__edit__title(self):
        ctype = self.get_type('ShippingMethod')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.title, 'Edit')

    def test_types__ShippingMethod__action__edit__condition(self):
        ctype = self.get_type('ShippingMethod')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.condition, '')

    def test_types__ShippingMethod__action__edit__url_expr(self):
        ctype = self.get_type('ShippingMethod')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.getActionExpression(), 'string:${object_url}/edit')

    def test_types__ShippingMethod__action__edit__visible(self):
        ctype = self.get_type('ShippingMethod')
        action = ctype.getActionObject('object/edit')
        self.assertTrue(action.visible)

    def test_types__ShippingMethod__action__edit__permissions(self):
        ctype = self.get_type('ShippingMethod')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.permissions, (u'Modify portal content',))

    def test_types__collective_cart_shipping_CartShippingMethod__i18n_domain(self):
        ctype = self.get_type('collective.cart.shipping.CartShippingMethod')
        self.assertEqual(ctype.i18n_domain, 'collective.cart.shipping')

    def test_types__collective_cart_shipping_CartShippingMethod__meta_type(self):
        ctype = self.get_type('collective.cart.shipping.CartShippingMethod')
        self.assertEqual(ctype.meta_type, 'Dexterity FTI')

    def test_types__collective_cart_shipping_CartShippingMethod__title(self):
        ctype = self.get_type('collective.cart.shipping.CartShippingMethod')
        self.assertEqual(ctype.title, 'CartShippingMethod')

    def test_types__collective_cart_shipping_CartShippingMethod__description(self):
        ctype = self.get_type('collective.cart.shipping.CartShippingMethod')
        self.assertEqual(ctype.description, '')

    def test_types__collective_cart_shipping_CartShippingMethod__content_icon(self):
        ctype = self.get_type('collective.cart.shipping.CartShippingMethod')
        self.assertEqual(ctype.getIcon(), '')

    def test_types__collective_cart_shipping_CartShippingMethod__allow_discussion(self):
        ctype = self.get_type('collective.cart.shipping.CartShippingMethod')
        self.assertFalse(ctype.allow_discussion)

    def test_types__collective_cart_shipping_CartShippingMethod__global_allow(self):
        ctype = self.get_type('collective.cart.shipping.CartShippingMethod')
        self.assertFalse(ctype.global_allow)

    def test_types__collective_cart_shipping_CartShippingMethod__filter_content_types(self):
        ctype = self.get_type('collective.cart.shipping.CartShippingMethod')
        self.assertTrue(ctype.filter_content_types)

    def test_types__collective_cart_shipping_CartShippingMethod__allowed_content_types(self):
        ctype = self.get_type('collective.cart.shipping.CartShippingMethod')
        self.assertEqual(ctype.allowed_content_types, ())

    def test_types__collective_cart_shipping_CartShippingMethod__schema(self):
        ctype = self.get_type('collective.cart.shipping.CartShippingMethod')
        self.assertEqual(
            ctype.schema, 'collective.cart.shipping.interfaces.ICartShippingMethod')

    def test_types__collective_cart_shipping_CartShippingMethod__klass(self):
        ctype = self.get_type('collective.cart.shipping.CartShippingMethod')
        self.assertEqual(ctype.klass, 'plone.dexterity.content.Container')

    def test_types__collective_cart_shipping_CartShippingMethod__add_permission(self):
        ctype = self.get_type('collective.cart.shipping.CartShippingMethod')
        self.assertEqual(
            ctype.add_permission, 'collective.cart.shipping.AddCartShippingMethod')

    def test_uninstall_package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.cart.shipping'])
        self.assertFalse(installer.isProductInstalled('collective.cart.shipping'))

    def test_uninstall_browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.cart.shipping'])
        from collective.cart.shipping.browser.interfaces import ICollectiveCartShippingLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveCartShippingLayer, utils.registered_layers())

    def test_uninstall_registry(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.cart.shipping'])
        from plone.registry.interfaces import IRegistry
        from zope.component import getUtility
        with self.assertRaises(KeyError):
            getUtility(IRegistry)['collective.behavior.vat.VAT']
