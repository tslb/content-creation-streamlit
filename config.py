import os
from enum import Enum


class LLMFamily(Enum):
    """
    LLM family enum
    """
    OPEN_AI = "OPEN_AI"
    ANTHROPIC = "ANTHROPIC"

class DataStyle(Enum):
    """
    Choropleth or data cluster
    """
    CHOROPLETH = "CHOROPLETH"
    DATA_CLUSTER = "DATA_CLUSTER"

class PathsShowText(Enum):
    ship = "SHIPPING"
    road = "ROAD"
    plane = "FLIGHT"
    dot = "DOTTED"
    line = "LINE"
class MapsShowText(Enum):
    """
    Maps text enum
    """
    LABEL = "SHOW_LABEL"
    SUB_LABEL = "SHOW_SUB_LABEL"

class SpeedOutput(Enum):
    slow = "SLOW"
    fast = "FAST"
    medium = "MEDIUM"
class ColourConfigOutput(Enum):
    smooth = "PROGRESS"
    fade = "FADE_IN"
    image = "IMAGE"

class LabelsOutput(Enum):
    pin = "DEFAULT"
    flag = "FLAGS"
                    
class AnimationMappingOutput(Enum):
    """
    Used for mapping the llm input to the output
    """
    flyto = "FLY_TO"
    colour = "REGION_FILL"
    border = "BOUNDARY_HIGHLIGHT"
    rotate = "ROTATION"
    tilt = "TILT"
    tiltback = "TILT"
    zoomin = "ZOOM"
    zoomout = "ZOOM"
    marker = "MARKER"
    paths = "PATHS"
    pause = "PAUSE"
    label = "SHOW_LABEL"
    sublabel = "SHOW_SUB_LABEL"

animation_mapping_output = {
    "flyto": "FLY_TO",
    "colour": "REGION_FILL",
    "border": "BOUNDARY_HIGHLIGHT",
    "rotate": "ROTATION",
    "tilt": "TILT",
    "zoomin": "ZOOM",
    "zoomout": "ZOOM",
    "marker": "MARKER",
    "paths": "PATHS",
    "pause": "PAUSE",
    "label": "SHOW_LABEL",
    "sublabel": "SHOW_SUB_LABEL"
}   
class DirectionMapping(Enum):
    """
    This is used to get the direction for rotate,
    """
    anticlockwise = "ANTI_CLOCKWISE"
    clockwise = "CLOCKWISE"

class EasingFunction(Enum):
    """
    Used to map the code of the easing function to the actual name
    """
    EIOQ = "easeInOutQuad"
    EIOC = "easeInOutCubic"
    EIOE = "easeInOutExpo"
    EIOS = "easeInOutSine"
    
class LabelSublabelAnimationMapping(Enum):
    """
    Used to map the animation function to the output name
    """
    label = MapsShowText.LABEL.value
    sublabel = MapsShowText.SUB_LABEL.value

LLM_RETRIES = 2

# region OpenAI
OPENAI_GPT3_5_MODEL = "gpt-3.5-turbo"
OPENAI_GPT_16K_MODEL = "gpt-3.5-turbo-16k"
OPENAI_TEMPERATURE_MAPS = 0.7
OPENAI_GPT_4O_MODEL = "gpt-4o-2024-05-13"
OPENAI_TEMPERATURE_MAPS_GPT3_5 = 0.1
OPENAI_TEMPERATURE_SUBLABELS = 0.7
OPENAI_TEMPERATURE_MAPS_VALIDATION = 0.2
TEMPERATURE_SCREENPLAY_MAPS = 0.7
OPENAI_REQUEST_TIMEOUT_MAPS = 120
OPENAI_CHAT_MODEL = "gpt-4-turbo"
MAX_TOKEN_LENGTH_OPENAI = 4095
MAX_TOKEN_LENGTH_16K = 8000
MAX_TOKEN_LENGTH_VALIDATION = 2000
MAX_TOKEN_LENGTH_SUBLABEL = 2000
OPENAI_RETRY_LIMIT = 2
# endregion

# region Anthropic
ANTHROPIC_MODEL = "claude-2.1"
ANTHROPIC_SONNET_MODEL = "claude-3-sonnet-20240229"
ANTHROPIC_HAIKU_MODEL = "claude-3-haiku-20240307"
ANTHROPIC_SONNET_3_5_MODEL = "claude-3-5-sonnet-20240620"
MAX_TOKEN_LENGTH_ANTHROPIC_CLAUDE = 4000
ANTHROPIC_RETRY_LIMIT = 3
ANTHROPIC_TEMPERATURE_MAPS = 0.7
ANTHROPIC_REQUEST_TIMEOUT_MAPS = 120
ANTHROPIC_TEMPERATURE_SUBLABELS = 0.7
# endregion

# region Maps
MAPS_EXTRACTION_RETRIES = 4
# map extraction has two prompts right now, 1st one is to classify, 2nd to extract the locations
MAP_CLASSIFICATION_MAX_TOKENS = 1000
MAP_LOCATIONS_EXTRACTION_MAX_TOKENS = 4000
MIN_DURATION_OF_FIRST_LOCATION_CLIP = 5  # how many seconds first location should be rendered
MIN_DURATION_OF_SECOND_LOCATION_CLIP = 4  # how many seconds second location should be rendered
LOCATION_INDEX_BUFFER_CHARACTERS_COUNT = 30  # how many characters before we should start showing the map
MAX_TOKEN_LENGTH_SCREENPLAY = 4000
MAX_TOKEN_LENGTH_SCREENPLAY_GPT_3_5 = 8000
SCREENPLAY_EXTRACTION_RETRIES = 3
# after how many characters we should start showing the map in case of first sentence of first block
LOCATION_INDEX_BUFFER_CHARACTERS_COUNT_FIRST_SENTENCE = 30
LOCATIONS_DIFFERENCE_DELTA = 40  # character difference between two locations for considering them sequential maps
MIN_HOLD_DURATION = 1  # default hold duration for maps
MIN_FLY_TO_DURATION = 2  # default intro duration for maps
MAPS_LABEL_APPEARANCE_BUFFER = 0  # seconds after any animation starts, the label should appear
MAPS_LABEL_DURATION = 0  # duration for the label animation
GEOLOCATION_API_KEY = os.getenv("GEOLOCATION_API_KEY")
# endregion

# status codes
class StatusCode(Enum):
    """
    We send 200 status code for successful screenplay generation.
    We send 400 in case of prompt is wrong from the user end or the locations list is empty
    For status code 500 and 501 there is some error in the code and hence we do not need any status as valid and invalid.
    Args:
        Enum
    """
    SUCCESS = 200
    BAD_REQUEST = 400
    INTERNAL_SERVER_ERROR = 500
    CODE_NOT_IMPLEMENTED = 501
# endregion

# region Maps timestamps and duration


class AnimationDuration(Enum):
    """
    Parent animation class to encapsulate different types of animations and their durations.
    """
    FLY_TO = (3, 5)
    ANGLE = (3, 4)
    ROTATION = (3, 8)
    REGION_FILL = (2, 3)
    BOUNDARY_HIGHLIGHT = (2, 3)
    SCENE_HOLD = (2, 4)

    def __init__(self, min_duration, max_duration):
        self.min_duration = min_duration
        self.max_duration = max_duration

# endregion

# region priority Tags
class PriorityTags(Enum):
    """
    This contains all the priority tags
    """
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

# endRegion

#region FlyTO Types

class FlyToPaths(Enum):
    """
    This class contains all the flyto supported by us
    """
    PARABOLIC = "PARABOLA"
    SQUARE = "SQUARE"

#endRegion

#region Choropleth
CHOROPLETH_PARAMS_TOKENS = 2500 

class AnimationMappingChoropleth(Enum):
    """
    Used to map the input name to the output name 
    """
    flyto = "FLY_TO"
    colour = "REGION_FILL"
    stay = ""
#endRegion

# region Elastic Search

USERNAME = os.getenv("ES_USERNAME")
PASSWORD = os.getenv("ES_PASSWORD")
URL = os.getenv("ES_URL")

ADDRESS_PRIORITY = {
            'locality': -1,
            'continent': 0,
            'country': 1,
            'administrative_area_level_1': 2,
            'administrative_area_level_2': 3,
            'administrative_area_level_3': 4,
            'administrative_area_level_4': 5,
            'administrative_area_level_5': 6
        }

#endregion

# messages

LOCATION_NOT_FOUND_ERROR_MESSAGE = "Currently the location(s) mentioned are not supported from our end, please try with some other locations"
NO_AMBIQUOUS_LOCATION_MESSAGE = """\nEven if previously mentioned do not use global, world, earth or any similar words as a location name, instead give the animation for all the locations that are mentioned in the screenplay simultaneously. Please do not use zoomout/zoomin functions"""
# Currently we are not supporting Asia as it is not present geocode API hence, asking the LLM to not show this location.

#end region

#Geocode api

GEOCODE_API_URL = os.getenv("GEOCODE_API_URL")

#endregion

# Global variable for total_cost
LLM_USAGE_COST = 0
# End region