from Products.PloneTestCase import ptc
import collective.testcaselayer.ptc

ptc.setupPloneSite()


class IntegrationTestLayer(collective.testcaselayer.ptc.BasePTCLayer):

    def afterSetUp(self):
        self.addProfile('collective.geo.zugmap:default')

Layer = IntegrationTestLayer([collective.testcaselayer.ptc.ptc_layer])
