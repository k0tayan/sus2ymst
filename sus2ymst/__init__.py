from sus2ymst.convert import *


def load(sus_file: str) -> [str, ErrorMessage]:
    sus2ymst = Sus2Ymst()
    return sus2ymst.load(sus_file), sus2ymst.get_error_messages()


def loads(sus_text: str) -> [str, ErrorMessage]:
    sus2ymst = Sus2Ymst()
    return sus2ymst.loads(sus_text), sus2ymst.get_error_messages()
