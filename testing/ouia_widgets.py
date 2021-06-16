from widgetastic.ouia import OUIAGenericView
from widgetastic.ouia import OUIAGenericWidget


class Button(OUIAGenericWidget):
    OUIA_COMPONENT_TYPE = "PF/Button"


class SelectOption(OUIAGenericWidget):
    OUIA_COMPONENT_TYPE = "PF/SelectOption"


class Select(OUIAGenericView):
    OUIA_COMPONENT_TYPE = "PF/Select"
    first_option = SelectOption("first option")
    second_option = SelectOption("second option")

    def choose(self, option):
        getattr(self, option).click()
