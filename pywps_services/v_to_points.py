# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class v_to_points(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'v.to.points', title = 'Creates points along input lines in new vector map with 2 layers.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'vector'}, {'type': 'simple', 'title': 'geometry'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/v.to.points.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'input', title = 'Data source for OGR access', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'application/dgn', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/shp', 'schema': 'None', 'encoding': 'None'}, {'mimeType': 'application/x-zipped-shp', 'schema': 'None', 'encoding': 'None'}])
    self.addLiteralInput(identifier = 'llayer', title = 'A single vector map can be connected to multiple database tables. This number determines which table to use. Layer name for OGR access.', minOccurs = 1, maxOccurs = 1, type = type("string"), default = "1")
    self.addLiteralInput(identifier = 'type', title = 'Feature type', minOccurs = 0, maxOccurs = 1024, type = type("string"), default = "point,line,boundary,centroid", allowedValues = ['point', 'line', 'boundary', 'centroid', 'area'])
    self.addLiteralInput(identifier = 'dmax', title = 'Maximum distance between points in map units', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 100.0)
    self.addLiteralInput(identifier = '-n', title = 'Write line nodes', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-v', title = 'Write line vertices', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-i', title = 'Interpolate points between line vertices', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-t', title = 'Do not create attribute table', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])

    # complex outputs
    self.addComplexOutput(identifier = 'output', title = 'Name for output vector map where points will be written', formats = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}, {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/kml/2.2.0/ogckml22.xsd', 'encoding': 'UTF-8'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.to.points", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = v_to_points()
  process.execute()
