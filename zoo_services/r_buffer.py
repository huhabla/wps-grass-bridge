import ZOOGrassModuleStarter as zoo
def r_buffer(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("r.buffer", inputs, outputs)
    return 1
