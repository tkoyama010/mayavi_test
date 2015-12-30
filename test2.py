
# coding: utf-8

# In[1]:

import numpy as np
from mayavi.api import Engine
from mayavi.sources.vtk_file_reader import VTKFileReader


# In[2]:

e = Engine()
e.start()


# In[3]:

s = e.new_scene()


# In[4]:

r = VTKFileReader()


# In[5]:

r.initialize('heart.vtk')
e.add_source(r)


# In[6]:

from mayavi.modules import api


# In[7]:

o = api.Outline()


# In[8]:

e.add_module(o)


# In[9]:

cgp = api.ContourGridPlane()
e.add_module(cgp)


# In[10]:

cgp.grid_plane.axis = 'x'


# In[11]:

# get_ipython().set_next_input(u'iso = api.IsoSurface');get_ipython().magic(u'pinfo api.IsoSurface')


# In[12]:

iso = api.IsoSurface(compute_normals=True)


# In[13]:

e.add_module(iso)

