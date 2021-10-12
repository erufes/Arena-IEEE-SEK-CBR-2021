"""sek_supervisor controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Supervisor

class sim_object():
    def __init__(self, obj_node):
        self.obj_node = obj_node
        self.initial_translation = self.get_translation()
        self.initial_rotation = self.get_rotation()
    
    def get_translation(self):
        obj_translation_field = self.obj_node.getField("translation")
        return obj_translation_field.getSFVec3f()
    
    def get_rotation(self):
        obj_rotation_field = self.obj_node.getField("rotation")
        return obj_rotation_field.getSFRotation()
    
    def reset_translation(self):
        self.obj_node.getField("translation").setSFVec3f(self.initial_translation)

      
    def reset_rotation(self):
        self.obj_node.getField("rotation").setSFRotation(self.initial_rotation)
        
                
    def reset_robot(self):
        self.obj_node.restartController()
        supervisor.step(timestep)
        self.obj_node.resetPhysics()
        supervisor.step(timestep)
        self.reset_translation()
        supervisor.step(timestep)
        self.obj_node.resetPhysics()
        supervisor.step(timestep)
        self.reset_rotation()
        supervisor.step(timestep)
        self.obj_node.resetPhysics()
        
# create the Robot instance.
supervisor = Supervisor()
timestep = int(supervisor.getBasicTimeStep())

robo_1 = sim_object(supervisor.getFromDef("ROBO_1"))
robo_2 = sim_object(supervisor.getFromDef("ROBO_2"))

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while supervisor.step(timestep) != -1:
    translation_1 = robo_1.get_translation()
    if(translation_1[0] > 2.5 or translation_1[0] < -2.5 or translation_1[1] < 0 or translation_1[2] > 1.25 or translation_1[2] < -1.25):
        robo_1.reset_robot()
    
    translation_2 = robo_2.get_translation()
    if(translation_2[0] > 2.5 or translation_2[0] < -2.5 or translation_2[1] < 0 or translation_2[2] > 1.25 or translation_2[2] < -1.25):
        robo_2.reset_robot()

# Enter here exit cleanup code.
