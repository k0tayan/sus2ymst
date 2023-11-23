from sus2ymst.convert import *


def load(sus_file: str, lane_offset: int = 2) -> [str, ErrorMessage]:
    sus2ymst = Sus2Ymst()
    return sus2ymst.load(sus_file, lane_offset), sus2ymst.get_error_messages()


def loads(sus_text: str, lane_offset: int = 2) -> [str, ErrorMessage]:
    sus2ymst = Sus2Ymst()
    return sus2ymst.loads(sus_text, lane_offset), sus2ymst.get_error_messages()
