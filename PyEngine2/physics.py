try:
    from PyEngine2.libs import BaseLibrary, DYNAMIC
except ModuleNotFoundError:
    from libs import BaseLibrary, DYNAMIC


class Physics():

    def __init__(self, gravity = [0, 1000], fps = 60):

        self.__space__ = basephysicsengine.Space()
        self.__space__.gravity = gravity
        self.__objectList__ = []
        self.fps = fps

    class RectRigitBody():

        def __init__(self, space, obj, body_type = DYNAMIC, mass = 1, elasticity = .9):

            self.__sprite__ = obj
            self.coords = self.__sprite__.coords[0], self.__sprite__.coords[1]
            self.body_type = body_type
            self.__sprite__.RigitBody = self
            self.width = self.__sprite__.coords[2]
            self.height = self.__sprite__.coords[3]
            self.angle = 0
            self.mass = mass
            self.moment = basephysicsengine.moment_for_box(self.mass, [self.width, self.height])
            self.elasticity = elasticity

            self.body = basephysicsengine.Body(self.mass, self.moment, self.body_type)
            self.body.position = self.coords
            self.body.angle = math.radians(self.angle)

            self.poly = basephysicsengine.Poly.create_box(self.body, (self.width, self.height))
            self.poly.elasticity = self.elasticity
            self.space = space
            self.space.__objectList__.append(self)

            self.space.__space__.add(self.body, self.poly)

    class CircleRigitBody():

        def __init__(self, space, obj, body_type = DYNAMIC, mass = 1, elasticity = .9):

            self.__sprite__ = obj
            self.coords = self.__sprite__.coords
            self.body_type = body_type
            self.__sprite__.RigitBody = self
            self.radius = self.__sprite__.radius
            self.angle = 0
            self.mass = mass
            self.moment = basephysicsengine.moment_for_circle(self.mass, 0, self.radius)
            self.elasticity = elasticity

            self.body = basephysicsengine.Body(self.mass, self.moment, self.body_type)
            self.body.position = self.coords
            self.body.angle = math.radians(self.angle)

            self.poly = basephysicsengine.Circle(self.body, self.radius)
            self.poly.elasticity = self.elasticity
            self.space = space
            self.space.__objectList__.append(self)

            self.space.__space__.add(self.body, self.poly)

    class SegmentRigitBody():

        def __init__(self, space, obj, body_type = DYNAMIC, mass = 1, elasticity = .9):

            self.__sprite__ = obj
            self.coords = self.__sprite__.coords
            self.body_type = body_type
            self.__sprite__.RigitBody = self
            self.radius = self.__sprite__.border
            self.angle = 0
            self.mass = mass
            self.moment = basephysicsengine.moment_for_circle(self.mass, 0, self.radius)
            self.elasticity = elasticity

            self.body = basephysicsengine.Body(self.mass, self.moment, self.body_type)
            self.body.position = 0, 0
            self.body.angle = math.radians(self.angle)

            self.poly = basephysicsengine.Segment(self.body, [self.coords[0], self.coords[1]], [self.coords[2], self.coords[3]], self.radius)
            self.poly.elasticity = self.elasticity
            self.space = space
            self.space.__objectList__.append(self)

            self.space.__space__.add(self.body, self.poly)
            
    class PolygonRigitBody():

        def __init__(self, space, obj, body_type = DYNAMIC, mass = 1, elasticity = .9):

            self.__sprite__ = obj
            self.coords = []
            for i in range(len(self.__sprite__.coords)-1):
                if i%2 == 0: self.coords.append([self.__sprite__.coords[i], self.__sprite__.coords[i+1]])
                
            self.body_type = body_type
            self.__sprite__.RigitBody = self
            self.radius = self.__sprite__.border
            self.angle = 0
            self.mass = mass
            self.moment = basephysicsengine.moment_for_circle(self.mass, 0, self.radius)
            self.elasticity = elasticity

            self.body = basephysicsengine.Body(self.mass, self.moment, self.body_type)
            self.body.position = 0, 0
            self.body.angle = math.radians(self.angle)

            self.poly = basephysicsengine.Poly(self.body, self.coords, None, self.radius)
            self.poly.elasticity = self.elasticity
            self.space = space
            self.space.__objectList__.append(self)

            self.space.__space__.add(self.body, self.poly)


    def updatePhysics(self):
        
        for obj in self.__objectList__:
            if obj.__class__ == Physics.RectRigitBody or obj.__class__ == Physics.CircleRigitBody:
                obj.coords = obj.body.position
            elif obj.__class__ == Physics.SegmentRigitBody:
                obj.coords = [obj.poly.a[0], obj.poly.a[1], obj.poly.b[0], obj.poly.b[1]]
            elif obj.__class__ == Physics.PolygonRigitBody:
                vertices = obj.poly.get_vertices()
                for i in range(vertices.__len__()):
                    vertices[i] = [vertices[i][0]+obj.body.position[0], vertices[i][1]+obj.body.position[1]]
                obj.coords = vertices
                
            obj.angle = obj.body.angle

            if obj.__class__ == self.RectRigitBody:
                obj.__sprite__.set_position({0:obj.coords[0], 1:obj.coords[1]})
                obj.__sprite__.value_change(angle = math.degrees(obj.angle))

            elif obj.__class__ == self.CircleRigitBody:
                obj.__sprite__.set_position([obj.coords[0], obj.coords[1]])

            elif obj.__class__ == self.SegmentRigitBody or obj.__class__ == self.PolygonRigitBody:
                obj.__sprite__.value_change(coords = obj.coords)
                

        self.__space__.step(1/self.fps)