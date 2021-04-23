"""
文本标准化
"""

from opencc import OpenCC

from utils.dat.dat import DoubleArrayTrie


opencc_tool = OpenCC('t2s')


def traditional2simple(self, text):
    """ 繁体转简体 """
    return opencc_tool.convert(text)


def DBC2SBC(ustring):
    """ 全角转半角 """
    rstring = ''
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 0x3000:
            inside_code = 0x0020
        else:
            inside_code -= 0xfee0
        if not (0x0021 <= inside_code and inside_code <= 0x7e):
            rstring += uchar
            continue
        rstring += chr(inside_code)
    return rstring


def SBC2DBC(ustring):
    """ 半角转全角 """
    rstring = ''
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 0x0020:
            inside_code = 0x3000
        else:
            if not (0x0021 <= inside_code and inside_code <= 0x7e):
                rstring += uchar
                continue
        inside_code += 0xfee0
        rstring += chr(inside_code)
    return rstring


class Deformation:

    def __init__(self):
        self.digit_dat = self._set_dat(
            filename="./resources/digit_deformation.txt")
        self.alpha_dat = self._set_dat(
            filename="./resources/alpha_deformation.txt")
        # self.chaizi_dat = self._set_dat(
        #     filename="./resources/alpha_deformation.txt")

    def digit_normalization(self, text):
        return self.digit_dat.match_replace(text)

    def alpha_normalization(self, text):
        return self.alpha_dat.match_replace(text)
    
    # def chaizi_normalization(self, text):
    #     return self.chaizi_dat.match_replace(text)

    def _set_dat(self, filename):
        patterns = {}
        with open(filename) as fr:
            for line in fr:
                arr = line.strip().split(' ')
                if len(arr) == 2 and arr[0].strip() != '' and arr[1].strip() != "":
                    patterns[arr[0].strip()] = arr[1].strip()
        pattern_dat = DoubleArrayTrie()
        pattern_dat.mapbuild(patterns)
        return pattern_dat
