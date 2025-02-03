# Gets the elevation of the selected nodes from the USGS 3D Elevation Program Data
#

import math
import json

from java.io import BufferedReader
from java.io import DataOutputStream
from java.io import InputStreamReader
from java.net import HttpURLConnection
from java.net import URL
from java.net import URLEncoder

from javax.swing import JOptionPane

from org.openstreetmap.josm.gui import MainApplication;

# ref: https://docs.oracle.com/javase/8/docs/api/overview-summary.html
#      https://josm.openstreetmap.de/wiki/DevelopersGuide/DevelopingPlugins
#      https://josm.openstreetmap.de/doc/overview-summary.html
#      http://locationtech.github.io/jts/javadoc/index.html
#
FEET_PER_METER = 3.28084

# Get the easting and northing of the selected node
active_dataset = MainApplication.getLayerManager().getActiveDataSet()
selected_nodes = active_dataset.getSelectedNodes()
for node in selected_nodes:
	selected_node = node 
	east_north = selected_node.getEastNorth()
	east = east_north.east()
	north = east_north.north()
	url = URL('https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer/identify')
	con = url.openConnection()
	con.setRequestMethod('GET')
	con.setDoOutput(True)
	out = DataOutputStream(con.getOutputStream())
	geometry = URLEncoder.encode(json.dumps({"x":east,"y":north,"spatialReference":{"wkid":102100}}))
	rendering_rules = URLEncoder.encode(json.dumps([{"rasterFunction": "Height Ellipsoidal"}]))
	parameters = 'geometry=' + geometry + '&geometryType=esriGeometryPoint&returnGeometry=false&returnCatalogItems=false&renderingRules=' + rendering_rules + '&f=json&wab_dv=1.5'
	out.writeBytes(parameters)
	out.flush()
	out.close()
	in_ = BufferedReader(InputStreamReader(con.getInputStream()))
	input_line = in_.readLine()
	in_.close()
	con.disconnect()
	height = str(int(round(float(json.loads(input_line)['value']))))
	UndoRedoHandler.getInstance().add(ChangePropertyCommand(selected_node, 'ele',height));
