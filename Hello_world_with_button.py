import ui
import ui

def hello_world_touch_up_inside(sender):
    #print ('Hello, World!')
    view['hello_world_label'].text = ("Hello, World!")
  
view = ui.load_view()
view.present('sheet')
