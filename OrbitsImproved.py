import numpy as np
import matplotlib.pyplot as plt
from manim import *

#G = 39.478
G = 15
config.frame_rate = 60

m1 = 1.0 
m2 = 1.0  
m3 = 0.1

masses = np.array([1.0,1.0,0.1])

positions = np.array([[1.5, 0.0, 0.0],[-1.5, 0.0, 0.0],[-3.0, -3.0, 9.0]])

velocities = np.array([[0.0, 1.5, 0.0],[0.0, -1.5, 0.0],[0.1, 0.1, -0.3]])

dt = 0.0001 
total_time = 35
n_steps = int(total_time / dt)


def compute_accelerations(positions, masses):
    accelerations = np.zeros_like(positions)
    for i in range(len(masses)):
        for j in range(len(masses)):
            if i != j:
                r = positions[j] - positions[i]
                dist = np.linalg.norm(r)
                accelerations[i] += G * masses[j] * r / dist**3
                
    return accelerations

class Orbits(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES)

        colors = [BLUE_D, ORANGE, GREEN]

        bodies = [Sphere(radius=0.2*m) for m in masses]

        for i in range(len(bodies)):
            bodies[i].set_color(colors[i]) 

        traces = [TracedPath(body.get_center, stroke_color=c, dissipating_time=2.0) for body, c in zip(bodies, colors)]

        box = Cube(6,fill_opacity=0,stroke_width=1.0)

        self.add(*bodies, *traces, box)

        self.begin_ambient_camera_rotation(rate=0.4)
        def update_positions(mob, dt):
            global positions, velocities
            
            accelerations = compute_accelerations(positions, masses)

            new_positions = positions + velocities * dt + 0.5 * accelerations * dt**2
            new_accelerations = compute_accelerations(new_positions, masses)
            velocities += 0.5 * (accelerations + new_accelerations) * dt
            positions = new_positions

            for body, pos in zip(bodies, positions):
                body.move_to(pos)

        for body in bodies:
            body.add_updater(update_positions)

        self.wait(total_time)

        for body in bodies:
            body.clear_updaters()
