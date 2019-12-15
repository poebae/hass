import appdaemon.appapi as appapi
import globals
import flags

#
# Xiaomi Stuff
#
# Args:
#

class xiaomi(appapi.AppDaemon):

    def initialize(self):
          self.listen_event(self.x_button1_single, "click", entity_id = globals.button_bedroom, click_type = "single")
          self.listen_event(self.x_button1_double, "click", entity_id = globals.button_bedroom, click_type = "double")
          self.listen_event(self.x_button1_double, "click", entity_id = globals.button_bedroom, click_type = "double")
          self.listen_event(self.x_button2_single, "click", entity_id = globals.x_switch_2, click_type = "single")
          self.listen_state(self.garage_door, globals.entry_garage, new="on")

    def x_button1_single(self,event_name, data, kwargs):
          self.log("button 1 press...")
          self.toggle("light.hg_office_oh_lights")

    def x_button1_double(self,event_name, data, kwargs):
          self.log("button 1 double click...")

    def x_button2_single(self,event_name, data, kwargs):
          self.log("button 2 press...")
          if self.entities.light.hannahs_br.state == "off":
            self.turn_on("light.hannahs_br")
            self.turn_on("light.hannahs_br")
          else:
            self.turn_off("light.hannahs_br")
            self.turn_off("light.hannahs_br")