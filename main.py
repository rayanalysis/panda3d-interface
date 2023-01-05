from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence, Func, Wait
from panda3d.core import load_prc_file_data
from panda3d.core import TransparencyAttrib, SamplerState, Texture
from panda3d.core import NodePath, AmbientLight, Vec3
from panda3d.core import LineSegs
from panda3d.core import TextNode
import sys
import random
import gamedef
import importlib

load_prc_file_data("",
"""
window-title Your Default Game
win-size 1280 720
framebuffer-srgb true
textures-power-2 none
texture-minfilter nearest
texture-magfilter nearest
text-scale-factor 1
hardware-animated-vertices true
simple-shaders-only false
cull-bin true
""")

nl = '\n'
base_gdf_1 = str('import random' + nl +
    'def interaction_2D():' + nl +
    '    m_poslist = [base.mouseWatcherNode.get_mouse_x(),base.mouseWatcherNode.get_mouse_y()]' + nl +
    '    print(m_poslist)' + nl +
    '    if round(m_poslist[0] < 0.2):' + nl +
    '        base.set_background_color(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),1)' + nl +
    'def start_up_active():' + nl +
    '    print("Default game state set.")' + nl)

def interaction_2D():
    gamedef.interaction_2D()

def build_gamedef_file():
    file_1 = open('gamedef.py','a')  # just open it in append mode
    file_1.write('def start_up_active():' + '\n' + '    print("Startup mode active.")' + '\n')  # inject the function
    file_1.close()

def call_inject_test():
    importlib.reload(gamedef)  # Python 3 has the importlib module to reload modules live
    try:
        gamedef.start_up_active()
    except:
        print("You probably haven't injected your function yet.")
    
def clean_exit():
    file_1 = open('gamedef.py','w')
    file_1.write(base_gdf_1)
    file_1.close()
    
    sys.exit()[0]

def setup_interface():
    base = ShowBase()
    base.camLens.set_fov(80)
    base.set_background_color(0,0,1,1)

    base.accept('c',interaction_2D)
    base.accept('r',build_gamedef_file)
    base.accept('o',call_inject_test)
    base.accept('q',clean_exit)

    text_1 = TextNode('startup_text')
    startup_text = 'Press "c" to test color change cursor hovering left screen only' + nl + 'Press "r" to inject gamedef module' + nl + 'Press "o" to call the injected function' + nl + 'Press "q" to clean exit.'
    text_1.set_text(startup_text)
    text_1_node = base.a2dTopLeft.attach_new_node(text_1)
    text_1_node.set_scale(0.039)
    text_1_node.set_pos(.051,0,-.11)

setup_interface()
base.run()
