import ZOOGrassModuleStarter as zoo
def r_shaded_relief(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.shaded.relief", inputs, outputs)
    return 1
