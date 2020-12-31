from chin_text_processor.sent_cutter import SentCutter


class TestSentCutter:

    def setup_class(cls):
        cls.sc = SentCutter()

    def test_split_by_slide_window(self):
        text = "0123456789"
        sc = SentCutter()
        assert sc.split_by_slide_window(text, stride=2, max_length=3) == ["012", "234", "567", "789"]
        assert sc.split_by_slide_window(text, stride=3, max_length=3) == ["012", "345", "456", "789"]
        assert sc.split_by_slide_window(text, stride=4, max_length=4) == ["0123", "2345", "6789"]
        assert sc.split_by_slide_window(text, stride=4, max_length=5) == ["01234", "56789"]
        assert sc.split_by_slide_window(text, stride=2, max_length=7) == ['0123456', '3456789']
