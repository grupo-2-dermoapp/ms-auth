import enum

class EyesColor(enum.Enum):
    LIGHT_BLUE_GREEN_GREY = 0
    BLUE_GREEN_GREY = 1
    DARK_BLUE_GREEN_LIGHT_BROWN = 2
    DARK_BROWN = 3
    BROWISH_BLACK = 4

class HairColor(enum.Enum):
    RED = 0
    BLONDIE = 1
    CHESNUT_DARK_BLONDIE = 2
    DARK_BROWN = 3
    BLACK = 4

class SkinColor(enum.Enum):
    PINK = 0
    VERY_PALE = 1
    LIGHT_BROWN_OLIVE = 2
    BROWN = 3
    DARK_BROWN = 4

class Freckles(enum.Enum):
    MANY = 0
    SEVERAL = 1
    FEW = 2
    RARE = 3
    NONE = 4

class SkinStayInTheSun(enum.Enum):
    SEVERE_BURNS = 0
    MODERATE_BURNS = 1
    SOMETIME_BURNS = 2
    RARE_BURNS = 3
    NO_BURNS = 4

class TurnBrown(enum.Enum):
    NEVER = 0
    RARELY = 1
    SOMETHIMES = 2
    OFTEN = 3
    ALWAYS = 4

class HowBrown(enum.Enum):
    HARLY = 0
    LIGHT_TAN = 1
    MEDIUM_TAN = 2
    DARK_TAN = 3
    VERY_DARK_TAN = 4

class FaceSensitive(enum.Enum):
    VERY_SENSITIVE = 0
    SENSITIVE = 1
    MILDLY_SENSITIVE = 2
    RESISTANT = 3
    VERY_RESISTANT = 4

class HowOftenTan(enum.Enum):
    NEVER = 0
    RERELY = 1
    SOMETIMES = 2
    OFTEN = 3
    ALWAYS = 4

class ArtificialTimeExpose(enum.Enum):
    MORE_THREE_MONTHS = 0
    LAST_TWO_THREE_MONTHS = 1
    LAST_ONE_TWO_MONTS = 2
    LAST_WEEK = 3
    LAST_DAY = 4