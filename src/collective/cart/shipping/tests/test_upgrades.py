from collective.cart.shipping.tests.base import IntegrationTestCase
from collective.cart.shipping.upgrades import PROFILE_ID

import mock


class TestCase(IntegrationTestCase):
    """TestCase for upgrade steps."""

    def setUp(self):
        self.portal = self.layer['portal']

    @mock.patch('collective.cart.shipping.upgrades.getToolByName')
    def test_reimport_registry(self, getToolByName):
        from collective.cart.shipping.upgrades import reimport_registry
        reimport_registry(self.portal)
        getToolByName().runImportStepFromProfile.assert_called_with(
            PROFILE_ID, 'plone.app.registry', run_dependencies=False, purge_old=False)
