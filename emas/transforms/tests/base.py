from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import quickInstallProduct

from plone.testing import z2

PROJECTNAME = "emas.transforms"

class TestCase(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import emas.transforms
        self.loadZCML(package=emas.transforms)

    def setUpPloneSite(self, portal):
        quickInstallProduct(portal, 'emas.transforms')

    def tearDownZope(self, app):
        z2.uninstallProduct(app, PROJECTNAME)

FIXTURE = TestCase()
INTEGRATION_TESTING = IntegrationTesting(bases=(FIXTURE,), name="fixture:Integration")
