import logging
import typing

from white_queen_nlp import jieba_utils
from white_queen_nlp.jieba_utils import load_word_cls, DiseaseCutV3

jieba_obj = jieba_utils.load_jieba()

class DiseaseCut(DiseaseCutV3):
    def __init__(self, logger: logging.Logger, jieba=None):
        super(DiseaseCutV3, self).__init__(logger=logger, jieba=jieba)
        self.disease_word_set = load_0_medicine_word_upper()

    def parse_disease_words(self, sentence_list: typing.List[str]) -> typing.List[typing.List[str]]:
        """ """
        result_list = []
        for q in sentence_list:
            _disease_word_set = set()
            try:
                word_list = self.jieba.cut(q)
                for word in word_list:
                    if word in self.stop_word_set:
                        continue

                    if word.upper() in self.disease_word_set:
                        _disease_word_set.add(word)
            except Exception as e:
                self.logger.error(f"[parse_disease_words] sentence {q}, error is {e}", exc_info=True)
                raise
            if list(_disease_word_set):
                result_list.append(list(_disease_word_set))

        return result_list


def load_0_medicine_word_upper(min_word_count: int = 2) -> typing.Set[str]:
    """
    只过滤病症

    :param min_word_count:
    :return:
    """
    tmp_dict = load_word_cls()
    word_set = set()
    cls_index_set = {0, }
    for word, cls_index in tmp_dict.items():
        if cls_index not in cls_index_set:
            continue
        if len(word) < min_word_count:
            continue
        word_set.add(word.upper())
    return word_set
