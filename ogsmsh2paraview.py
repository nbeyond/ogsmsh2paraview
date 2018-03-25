from paraview import vtk
import os
# Set your OpenGeoSys .msh file here.
filename = os.path.normcase("./examples/daejeon-ogs-final.msh")
f = open(filename)
output = self.GetOutput()
 
# Read everything with no line break but with space. IMPORTANT
contents = f.read().replace('\n', ' ')
words = contents.split()
 
# Now read point(node) info
numPoints = int(words[words.index('$NODES')+1])
#print (numPoints)
pts = vtk.vtkPoints()
 
pos1 = words.index('$NODES')+2
for node in range(numPoints):
#    node_idx = words[pos+node*4]
    x = float(words[pos1+node*4+1])
    y = float(words[pos1+node*4+2])
    z = float(words[pos1+node*4+3])
    pts.InsertNextPoint(x,y,z)
 
#   print x, y, z
 
output.SetPoints(pts)
 
 
# Now read element(cell) info
numCells = int(words[words.index('$ELEMENTS')+1])
#print (numCells)
output.Allocate(numCells, 1000)
pos2 = words.index('$ELEMENTS')+2
celltype = words[pos2+2] 
 
 
# Write off to find cell type and the number of points in a cell
def findCellType(celltype):
  if "line" in [celltype]:
    ctype = 3
    numCellPoints = 2
  elif "tri" in [celltype]:
    ctype = 5
    numCellPoints = 3
  elif "quad" in [celltype]:
    ctype = 9
    numCellPoints = 4
  elif "tet" in [celltype]:
    ctype = 10
    numCellPoints = 4
  elif "hex" in [celltype]:
    ctype = 12
    numCellPoints = 8
  elif "pris" in [celltype]:
    ctype = 13
    numCellPoints = 6
  else:
    ctype = 0
    numCellPoints = 0
    print "Failed to identify element type"
    
  return ctype, numCellPoints
# function ends here
 
ctype, numCellPoints = findCellType(celltype)
#print ctype, numCellPoints 
 
 
for cell in range(numCells):
  celltype = words[pos2+cell*(numCellPoints+3)+2] 
  pos_this_cell = pos2+cell*(numCellPoints+3)+3
  ctype, numCellPoints = findCellType(celltype)
  pointIds = vtk.vtkIdList()
  for pointId in range(numCellPoints):
    pointIds.InsertId(pointId, int(words[pos_this_cell+pointId]))
  output.InsertNextCell(ctype, pointIds)
 
# For Material properties of cell
numberOfComponents = 1  # For .msh material property by default it is 1
dataArray = vtk.vtkDoubleArray()
output.GetCellData().AddArray(dataArray)
dataArray.SetNumberOfComponents(numberOfComponents)
dataArray.SetName('matgroup')
for cell in range(numCells):
  matgroup = words[pos2+cell*(numCellPoints+3)+1] 
  dataArray.InsertNextValue(float(matgroup))