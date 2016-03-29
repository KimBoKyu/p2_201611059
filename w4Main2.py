
# coding: utf-8

# In[2]:

get_ipython().magic(u'pwd')
mydir = get_ipython().magic(u'pwd')
mydir


# In[3]:

import os
myplantdir=os.path.join(mydir,'lib')
myplantdir


# In[4]:

get_ipython().magic(u'cd {myplantdir}')
mydot="C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe"


# In[5]:

mydot


# In[6]:

get_ipython().magic(u'install_ext https://raw.githubusercontent.com/sberke/ipython-plantuml/master/plantuml_magics.py')


# In[7]:

get_ipython().magic(u'load_ext plantuml_magics')


# In[8]:

import glob
get_ipython().magic(u'cd {myplantdir}')
glob.glob(r'./*.jar')


# In[9]:

import os
os.environ['GRAPHVIZ_DOT']=mydot
print os.environ['GRAPHVIZ_DOT']
get_ipython().system(u'java -jar {plantdir}/plantuml.jar -testdot')


# In[10]:

get_ipython().magic(u'install_ext https://raw.githubusercontent.com/sberke/ipython-plantuml/master/plantuml_magics.py')


# In[11]:

get_ipython().magic(u'load_ext plantuml_magics')


# In[12]:

get_ipython().run_cell_magic(u'plantuml', u'', u'@startuml\nstart\n:set how many turns;\n:set how much to grow bigger;\n:set angle;\n:set start size;\nrepeat\nif (i is divided by 2) then\n    :grow bigger;\nendif\n:draw;\nrepeat while(turns)\nstop\n@enduml')

