import ZOOGrassModuleStarter as zoo
def v_class(m, inputs, outputs):
    service = zoo.ZOOGrassModuleStarter()
    service.fromMaps("v.class", inputs, outputs)
    return 1
