import random
def interaction_2D():
    m_poslist = [base.mouseWatcherNode.get_mouse_x(),base.mouseWatcherNode.get_mouse_y()]
    print(m_poslist)
    if round(m_poslist[0] < 0.2):
        base.set_background_color(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),1)
