from xchk_core.contentviews import ContentView
from xchk_core.strats import *

class DemoCSSView(ContentView):
     
    uid = 'xchk_css_content_demo'
    template = 'xchk_css_content/xchk_css_content_demo.html'
    strat = Strategy(refusing_check=TrueCheck(),
                     accepting_check=Negation(TrueCheck()))
