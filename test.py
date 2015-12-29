from os.path import join, dirname

from mayavi.scripts import mayavi2
from mayavi.sources.vtk_file_reader import VTKFileReader
from mayavi.filters.threshold import Threshold
from mayavi.modules.api import Outline, GridPlane, ContourGridPlane, IsoSurface, ScalarCutPlane

def contour():
    mayavi.new_scene()

    r = VTKFileReader()
    r.initialize('heart.vtk')
    mayavi.add_source(r)

    o = Outline()
    mayavi.add_module(o)

    gp = GridPlane()
    mayavi.add_module(gp)
    gp = GridPlane()
    mayavi.add_module(gp)
    gp.grid_plane.axis = 'y'
    gp = GridPlane()
    mayavi.add_module(gp)
    gp.grid_plane.axis = 'z'

    cgp = ContourGridPlane() 
    mayavi.add_module(cgp)
    cgp.grid_plane.position = 15

    cgp = ContourGridPlane() 
    mayavi.add_module(cgp)
    cgp.grid_plane.axis = 'y'
    cgp.grid_plane.position = 15
    cgp.contour.filled_contours = True

    iso = IsoSurface(compute_normals=True)
    mayavi.add_module(iso)
    iso.contour.contours = [220.0]

    cp = ScalarCutPlane()
    mayavi.add_module(cp)
    cp.implicit_plane.normal = 0, 0, 1

@mayavi2.standalone
def main():
    contour()
    
if __name__ == '__main__':
    main()
