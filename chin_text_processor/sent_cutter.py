

class SentCutter:

    def __init__(self):
        pass

    def segment(self, text, max_length=125):
        """
        :param text: string
        :return: list of short strings
        """
        punc_tokens = ["。", "？", "！", "?", "，", "℃", "；", "、", "："]
        sub_texts = []
        tmp_sent = text
        while tmp_sent:
            if len(tmp_sent) <= max_length:
                sub_texts.append(tmp_sent)
                break
            else:
                for idx in range(max_length - 1, -1, -1):
                    wd = tmp_sent[idx]
                    if wd in punc_tokens:
                        sub_texts.append(tmp_sent[:idx+1])
                        tmp_sent = tmp_sent[idx+1:]
                        break
                else:
                    sub_texts.append(tmp_sent[:max_length])
                    tmp_sent = tmp_sent[max_length:]

        return sub_texts

    def split_by_slide_window(self, text, stride=100, max_length=128):
        """
        :param text: string
        :param stride: stride should be less than max_length
        :param max_length: 
        :return: list of short strings
        """
        text_length = len(text)
        if text_length <= max_length:
            return [text]

        left_pos, right_pos = 0, text_length - max_length
        sub_texts = []
        while left_pos < right_pos:
            sub_texts.append(text[left_pos: left_pos + max_length])
            if left_pos + max_length >= right_pos:
                break
            left_pos += stride
            right_pos -= stride
        while right_pos <= text_length - max_length:
            sub_texts.append(text[right_pos: right_pos + max_length])
            right_pos += stride

        return sub_texts
