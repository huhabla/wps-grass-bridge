import ZOOGrassModuleStarter as zoo
def r_grow_distance(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.grow.distance", inputs, outputs)
    return 1
