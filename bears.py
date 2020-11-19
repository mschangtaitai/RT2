from raytracer import *
from sphere import *

r = Raytracer(1200, 1000)
r.light = Light(
	position=V3(10,10,20),
	intensity=1
)

#Materials
eye = Material(diffuse = color(0,0,0), albedo = (1,1), spec = 90)
whiteStuffed = Material(diffuse = color(255,255,255), albedo = (1,1), spec = 10)
brownStuffed = Material(diffuse = color(254,229,202), albedo = (0.8,0.8), spec = 30)
darkBrownStuffed = Material(diffuse = color(191,94,41), albedo = (1,1), spec = 15)
whiteSmooth = Material(diffuse = color(255,255,255), albedo = (0.8,0.8), spec = 100)
brownSmooth = Material(diffuse = color(218,47,38), albedo = (1,1), spec = 100)

#Brown bear
r.scene.append(Sphere(V3(2,0,-10), 1.5, brownSmooth))
r.scene.append(Sphere(V3(2,1.7,-9), 1, brownStuffed))
r.scene.append(Sphere(V3(2.9,2.3,-8.8), 0.5, darkBrownStuffed))
r.scene.append(Sphere(V3(1.1,2.3,-8.8), 0.5, darkBrownStuffed))
r.scene.append(Sphere(V3(2,1.4,-8.5), 0.55, darkBrownStuffed))
r.scene.append(Sphere(V3(2.3,2,-8.4), 0.1, eye))
r.scene.append(Sphere(V3(1.7,2,-8.4), 0.1, eye))
r.scene.append(Sphere(V3(2,1.4,-8), 0.1, eye))
r.scene.append(Sphere(V3(3.1,0.8,-9), 0.5, brownStuffed))
r.scene.append(Sphere(V3(0.9,0.8,-9), 0.5, brownStuffed))
r.scene.append(Sphere(V3(3,-1,-9), 0.5, brownStuffed))
r.scene.append(Sphere(V3(1,-1,-9), 0.5, brownStuffed))

#White bear
r.scene.append(Sphere(V3(-2,0,-10), 1.5, whiteSmooth))
r.scene.append(Sphere(V3(-2,1.7,-9), 1, whiteStuffed))
r.scene.append(Sphere(V3(-1.1,2.3,-8.8), 0.5, whiteStuffed))
r.scene.append(Sphere(V3(-2.9,2.3,-8.8), 0.5, whiteStuffed))
r.scene.append(Sphere(V3(-2,1.4,-8.5), 0.55, whiteStuffed))
r.scene.append(Sphere(V3(-1.7,2,-8.4), 0.1, eye))
r.scene.append(Sphere(V3(-2.3,2,-8.4), 0.1, eye))
r.scene.append(Sphere(V3(-2,1.4,-8), 0.1, eye))
r.scene.append(Sphere(V3(-0.9,0.8,-9), 0.5, whiteStuffed))
r.scene.append(Sphere(V3(-3.1,0.8,-9), 0.5, whiteStuffed))
r.scene.append(Sphere(V3(-1,-1,-9), 0.5, whiteStuffed))
r.scene.append(Sphere(V3(-3,-1,-9), 0.5, whiteStuffed))

r.render()
r.write("bears.bmp")