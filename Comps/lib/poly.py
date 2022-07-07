import warnings
from shapely.errors import ShapelyDeprecationWarning

from shapely.geometry import Point
import geopandas as gpd
import numpy as np
warnings.filterwarnings("ignore", category=ShapelyDeprecationWarning)

def change_points(comp, points):
  str = ""
  
  for x, y in points:
    str += f"{{ X = {x}, Y = {y}}},\n"
  
  comp.Execute(f"""-- create a new PolylineMask
  mask = comp.PolylineMask()
  ct = comp.CurrentTime -- KeyFrames will have this index, when we create the Polyline!
  -- copy the tool, so we can modify the entire table shizbang
  maskTool = comp:CopySettings(mask)
  maskPoly = mask.Polyline:GetConnectedOutput():GetTool()
  polyName = maskPoly:GetAttrs().TOOLS_Name

  NewPoints = {{
    {str}
  }}

  maskTool.Tools[polyName].KeyFrames[ct].Value['Closed'] = true
  maskTool.Tools[polyName].KeyFrames[ct].Value.Points = NewPoints

  mask:Delete()
  comp:Paste(maskTool)""")
  
  
def get_diff_points(x, y, s):

  x -= 0.5
  y -= 0.5

  s = 1 / s

  x *= -s
  y *= -s

  p1 = Point((0,0))
  p2 = Point((x,y))

  gp1 = gpd.GeoSeries(p1)
  gp2 = gpd.GeoSeries(p2)

  # Buffer the points using a square cap style
  # Note cap_style: round = 1, flat = 2, square = 3
  b1 = gp1.buffer(0.5, cap_style = 3)
  b2 = gp2.buffer(s/2, cap_style = 3)


  diff = b2.difference(b1)
  odiff = b1.difference(b2)
  
  diff_points = []
  try:
    for b in diff[0].boundary: # for first feature/row
      coords = np.dstack(b.coords.xy).tolist()
      diff_points.append(*coords) 
  except:
    diff_points = np.dstack(diff.boundary[0].coords.xy).tolist()
    
  
  if len(diff_points) == 1:
    all_diff_points = diff_points[0][:-1]
  elif len(diff_points) == 2:
    all_diff_points = diff_points[0][:3] + diff_points[1] + diff_points[0][2:-1]
  else:
    print("more than 2 shapes inside")
    exit()
  
  odiff_points = []
  try:
    for b in odiff[0].boundary: # for first feature/row
      coords = np.dstack(b.coords.xy).tolist()
      odiff_points.append(*coords) 
  except:
    odiff_points = np.dstack(odiff.boundary[0].coords.xy).tolist()
  
  if len(odiff_points) == 1:
    all_odiff_points = odiff_points[0][:-1]
  elif len(odiff_points) == 2:
    all_odiff_points = odiff_points[0][:3] + odiff_points[1] + odiff_points[0][2:-1]
  elif len(odiff_points) == 0:
    all_odiff_points = []
  else:
    print("more than 2 shapes inside")
    exit()
  
  return all_diff_points, all_odiff_points