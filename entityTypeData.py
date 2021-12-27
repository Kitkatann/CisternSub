from entityType import EntityType
import imageUtil

#pre-defined entity assets with set type - read from editorEntitiesData.txt
entityTypes = []
def LoadEntityTypes():
    f = open("data/entitiesData.txt", "r")
    for line in f:
        entityData = []
        for word in line.split():
            entityData.append(word)
        if len(entityData) == 3:
            entityType = EntityType(int(entityData[0]), entityData[2])
            #if image filename to be used, set image to it
            if entityData[1] != "none":
                entityType.image = imageUtil.LoadImage("images/" + entityData[1], True)
            entityTypes.append(entityType)
    f.close()
    
def GetEntityTypeByID(id):
    for e in entityTypes:
        if e.id == id:
            return e