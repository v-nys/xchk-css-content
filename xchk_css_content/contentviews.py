from xchk_core.contentviews import ContentView
from xchk_core.strats import *

class PageFooterView(ContentView):
     
    uid = 'css_page_footer'
    template = 'xchk_css_content/css_page_footer.html'
    strat = Strategy(refusing_check=TrueCheck(),
                     accepting_check=Negation(TrueCheck()))
