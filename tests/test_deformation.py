from text_preprocess.text_normalization import Deformation


class TestTextNormalization:

    def setup_class(cls):
        cls.deform = Deformation()

    def test_digit_normalization(self):
        text = "①②③④⑤⑥⑦⑧⑨"
        assert self.deform.digit_normalization(text) == "123456789"

    def test_alpha_normalization(self):
        text = "ⓐⓑⓒⓓⓔⓕⓖⓗ"
        assert self.deform.alpha_normalization(text) == "abcdefgh"
