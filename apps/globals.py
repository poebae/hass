# Global variables

import secrets
import random


def get_arg(args, key):
        key = args[key]
        if type(key) is str and key.startswith("secret_"):
            if key in secrets.secret_dict:
                return secrets.secret_dict[key]
            else:
                raise KeyError("Could not find {} in secret_dict".format(key))
        else:
            return key


def get_arg_list(args, key):
    arg_list = []
    if isinstance(args[key], list):
        arg = args[key]
    else:
        arg = (args[key]).split(",")
    for key in arg:
        if type(key) is str and key.startswith("secret_"):
            if key in secrets.secret_dict:
                arg_list.append(secrets.secret_dict[key])
            else:
                raise KeyError("Could not find {} in secret_dict".format(key))
        else:
            arg_list.append(key)
    return arg_list


def random_arg(argList):
    ############################################
    # pick a random text from a list
    ############################################
    if isinstance(argList, list):
        text = random.choice(argList)
    else:
        text = argList
    return text


# motion_living_room = "binary_sensor.motion_living_occupancy"
# motion_dining_room = "binary_sensor.motion_study_occupancy"
# motion_kitchen = "binary_sensor.motion_kitchen_occupancy"

# door_bedroom = "binary_sensor.door_bedroom"

# wall_bedroom = "sensor.0x00158d000183b707"
# wall_living = "sensor.0x00158d0001712e06"
# wall_kitchen = "sensor.0x00158d000183df47"
# wall_study = "sensor.0x00158d000183bde7"

# button_bedroom = "sensor.0x00158d0001b12769"