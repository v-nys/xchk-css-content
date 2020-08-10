from xchk_core import contentviews as basecv
from xchk_core.courses import Course
from .contentviews import *

course = Course('css',
                'CSS',
                [(DemoCSSView,[])],
                "git@github.com:v-nys/xchk-css-model-solutions.git")
