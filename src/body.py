from vector import Vector


class Body:
    registry = []

    def __init__(
        self,
        displacement,
        velocity=None,
        acceleration=None,
        jerk=None,
        time=0,
        radius=0.01,
    ):
        Body.registry.append(self)
        self.displacement = displacement
        self.velocity = velocity
        self.acceleration = acceleration
        self.jerk = jerk
        self.time = time
        self.radius = radius

        dimensionality = self.displacement.len
        if not velocity:
            self.velocity = Vector([0] * dimensionality)
        if not acceleration:
            self.acceleration = Vector([0] * dimensionality)
        if not jerk:
            self.jerk = Vector([0] * dimensionality)

    def timestep(self, time):

        self.displacement += (
            self.velocity * time
            + (0.5 * self.acceleration * time**2)
            + ((1 / 3) * self.jerk * time**3)
        )
        self.velocity += self.acceleration * time + 0.5 * self.jerk * time**2

        self.acceleration += self.jerk * time
        self.time += time

    def bounce(self, dimension):
        friction = 0.9
        compression = 0.8
        mini = 1e-7
        self.velocity.vector[dimension] *= -1
        # print(f"before: {(self.velocity.vector[dimension]):.0f}")

        self.velocity.vector[dimension] = self.velocity.vector[dimension] * compression

        # if abs(self.velocity.vector[dimension]) < mini:
        #     self.velocity.vector[dimension] = 0
        # if dimension == 1:
        #     other = 0
        # else:
        #     other = 1
        # if abs(self.velocity.vector[other]) < mini:
        #     self.velocity.vector[other] = 0
        # self.velocity.vector[other] *= friction
        # print(f"after: {(self.velocity.vector[dimension]):.0f}")

    def try_bounce(self):
        # print(self.velocity.x)
        offset = 0
        if self.displacement.z > (2 - offset):
            self.bounce(2)
            self.displacement.z = 2 - offset
        if self.displacement.z < (0 + offset):
            self.bounce(2)
            self.displacement.z = 0 + offset

        if self.displacement.y > (2 - offset):
            self.bounce(1)
            self.displacement.y = 2 - offset

        if self.displacement.y < (0 + offset):
            self.bounce(1)
            self.displacement.y = 0 + offset

        if self.displacement.x > (2 - offset):
            self.bounce(0)
            self.displacement.x = 2 - offset

        if self.displacement.x < (0 + offset):
            self.bounce(0)
            self.displacement.x = 0 + offset

    def __str__(self):
        return f"""@ {self.time:2.2f}s:\ndisp: {self.displacement}\n vel: {self.velocity}\n acc: {self.acceleration}\njerk: {self.jerk}"""

    @property
    def screen_size(self):
        depth = self.displacement.z
        return self.radius * (1 / (depth + 0.5))
