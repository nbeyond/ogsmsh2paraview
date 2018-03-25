# ogsmsh2paraview
I have been amazed by many features given by ParaView and using OpenGeoSys for scientific simulations. To have them together working for my work, I have written a Programmable Source Script for importing  OpenGeoSys meshes on ParaView. Thus, I can use ParaView as pre- and post- processors.

# How to use the script?
1. Select Programmable Source in ParaView.
2. Set Output Data Set Type to vtkUnstructuredGrid.
3. Copy and paste the following python code to Script.
4. Change filename to be your OpenGeoSys mesh file (a mesh for the city of Daejeon added for your test in examples).
5. Click Apply button on ParaView.

Note: The script needs some polishment for including various other elements used in OpenGeoSys. It should not be difficult to revise as you like to suit your need. Any revision will be welcome.

