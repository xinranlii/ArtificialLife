import mujoco
import mujoco_viewer
import numpy as np

model = mujoco.MjModel.from_xml_path('door.xml')
data = mujoco.MjData(model)

viewer = mujoco.viewer.launch_passive(model, data)

door_angle = 0
handle_angle = 0

# Simulation loop
for i in range(10000):
    if viewer.is_alive:
        if i % 100 == 0:
            door_angle = -door_angle  # Oscillate door angle
            handle_angle = (handle_angle + 30) % 60  # Rotate handle within 0-60 degrees

        data.ctrl[model.get_actuator('door_hinge')] = door_angle

        data.ctrl[model.get_actuator('handle_hinge')] = handle_angle

        mujoco.mj_step(model, data)

        viewer.render()
    else:
        break

# Close the viewer
viewer.close()