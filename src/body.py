from vector import Vector


class Body:
    def __init__(
        self,
        displacement,
        velocity=None,
        acceleration=None,
        jerk=None,
        time=0,
    ):
        self.displacement = displacement
        self.velocity = velocity
        self.acceleration = acceleration
        self.jerk = jerk
        self.time = time

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

    def try_bounce(self):
        if self.displacement.vector[1] >= 400:
            self.velocity.vector[1] *= -1
            self.velocity = self.velocity * 0.9

    def __str__(self):
        return f"""@ {self.time:2.2f}s:\ndisp: {self.displacement}\n vel: {self.velocity}\n acc: {self.acceleration}\njerk: {self.jerk}"""
