import copy
from Calculations import *

def whereCanIGetTo1(self, sprite):
    movementToTry_x = sprite.x - object.oldPos.x
    movementToTry_y = sprite.y - object.oldPos.y
    furthestAvailableLocationSoFar_x = 0
    furthestAvailableLocationSoFar_y = 0
    furthestAvailableLocationSoFar_x = object.oldPos_x
    furthestAvailableLocationSoFar_x = object.oldPos_y

    tempObject = copy.sprite

    length  = calculateDistance(0, 0, movementToTry.x, movementToTry.y)

    numberOfStepsToBreakMovementInto = Floor(length  # * 2) + 1
    oneStep as position
    oneStep.x = movementToTry.x / numberOfStepsToBreakMovementInto
    oneStep.y = movementToTry.y / numberOfStepsToBreakMovementInto

    for i = 1 to  numberOfStepsToBreakMovementInto
        positionToTry as position
        positionToTry.x = object.oldPos.x + (oneStep.x * i)
        positionToTry.y = object.oldPos.y + (oneStep.y * i)
        SetSpritePosition(object.sprite, positionToTry.x, positionToTry.y)

        if (checkTileCollisions(object, 1) = 0)
            furthestAvailableLocationSoFar = positionToTry
            break

return furthestAvailableLocationSoFar