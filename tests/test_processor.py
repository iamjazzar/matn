from unittest import TestCase

from ddt import data, ddt, unpack

from jummal.processor import jummal_counter


@ddt
class TestJummalNormal(TestCase):
    def wrapper(self, text):
        return jummal_counter(text)

    @data(
        ["أ", 1],
        ["ب", 2],
        ["ج", 3],
        ["د", 4],
        ["ه", 5],
        ["و", 6],
        ["ز", 7],
        ["ح", 8],
        ["ط", 9],
        ["ي", 10],
        ["ك", 20],
        ["ل", 30],
        ["م", 40],
        ["ن", 50],
        ["س", 60],
        ["ع", 70],
        ["ف", 80],
        ["ص", 90],
        ["ق", 100],
        ["ر", 200],
        ["ش", 300],
        ["ت", 400],
        ["ث", 500],
        ["خ", 600],
        ["ذ", 700],
        ["ض", 800],
        ["ظ", 900],
        ["غ", 1_000],
    )
    @unpack
    def test_jummal_counter_single_character(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["مِنْ غَزَلٍ", 1_127],
        ["مات الشعرُ بعـده", 1_123],
        ["جاء المخصّص يروي أحسنَ الكَلِم", 1_321],
        ["من أنبت الغصن من صمصامة ذكر", 2_990],
    )
    @unpack
    def test_jummal_counter_sentences(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["رب", 202],
        ["ريح", 218],
        ["شعب", 372],
        ["جمر", 243],
        ["ظن", 950],
    )
    @unpack
    def test_jummal_counter_words(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["ء", 0],
        ["بهاء", 8],
        ["إيهاب", 19],
        ["بؤبؤ", 16],
        ["سائق", 171],
        ["أنس", 111],
        ["ًرمى القضاء بعيني جؤذر أسدا", 2_299],
    )
    @unpack
    def test_jummal_counter_hamza(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["بكى", 32],
    )
    @unpack
    def test_jummal_counter_alef_maksora(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["حمزة", 60],
        ["أبكمه", 68],
    )
    @unpack
    def test_jummal_counter_heh_teh_marboota(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["طغ", 1_009],
        ["بغ", 1_002],
        ["غغ", 2_000],
        ["مرغ", 1_240],
        ["بغي", 1_012],
        ["بغاء", 1_003],
    )
    @unpack
    def test_jummal_counter_tarkeeb(self, text, expected):
        assert expected == self.wrapper(text), text


@ddt
class TestJummalUseTarkeeb(TestCase):
    def wrapper(self, text):
        return jummal_counter(text, use_tarkeeb=True)

    @data(
        ["أ", 1],
        ["ب", 2],
        ["ج", 3],
        ["د", 4],
        ["ه", 5],
        ["و", 6],
        ["ز", 7],
        ["ح", 8],
        ["ط", 9],
        ["ي", 10],
        ["ك", 20],
        ["ل", 30],
        ["م", 40],
        ["ن", 50],
        ["س", 60],
        ["ع", 70],
        ["ف", 80],
        ["ص", 90],
        ["ق", 100],
        ["ر", 200],
        ["ش", 300],
        ["ت", 400],
        ["ث", 500],
        ["خ", 600],
        ["ذ", 700],
        ["ض", 800],
        ["ظ", 900],
        ["غ", 1_000],
    )
    @unpack
    def test_jummal_counter_single_character(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["مِنْ غَزَلٍ", 1_127],
        ["مات الشعرُ بعـده", 1_123],
        ["جاء المخصّص يروي أحسنَ الكَلِم", 1_321],
        ["من أنبت الغصن من صمصامة ذكر", 31_960],
    )
    @unpack
    def test_jummal_counter_sentences(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["رب", 202],
        ["ريح", 218],
        ["شعب", 372],
        ["جمر", 243],
        ["ظن", 950],
    )
    @unpack
    def test_jummal_counter_words(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["ء", 0],
        ["بهاء", 8],
        ["إيهاب", 19],
        ["بؤبؤ", 16],
        ["سائق", 171],
        ["أنس", 111],
        ["ًرمى القضاء بعيني جؤذر أسدا", 2_299],
    )
    @unpack
    def test_jummal_counter_hamza(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["بكى", 32],
    )
    @unpack
    def test_jummal_counter_alef_maksora(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["حمزة", 60],
        ["أبكمه", 68],
    )
    @unpack
    def test_jummal_counter_heh_teh_marboota(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["طغ", 9_000],
        ["بغ", 2_000],
        ["غغ", 1_000_000],
        ["مرغ", 200_040],
        ["بغي", 2_010],
        ["بغاء", 2_001],
    )
    @unpack
    def test_jummal_counter_tarkeeb(self, text, expected):
        assert expected == self.wrapper(text), text


@ddt
class TestJummalUseHamza(TestCase):
    def wrapper(self, text):
        return jummal_counter(text, use_hamza=True)

    @data(
        ["أ", 1],
        ["ب", 2],
        ["ج", 3],
        ["د", 4],
        ["ه", 5],
        ["و", 6],
        ["ز", 7],
        ["ح", 8],
        ["ط", 9],
        ["ي", 10],
        ["ك", 20],
        ["ل", 30],
        ["م", 40],
        ["ن", 50],
        ["س", 60],
        ["ع", 70],
        ["ف", 80],
        ["ص", 90],
        ["ق", 100],
        ["ر", 200],
        ["ش", 300],
        ["ت", 400],
        ["ث", 500],
        ["خ", 600],
        ["ذ", 700],
        ["ض", 800],
        ["ظ", 900],
        ["غ", 1_000],
    )
    @unpack
    def test_jummal_counter_single_character(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["مِنْ غَزَلٍ", 1_127],
        ["مات الشعرُ بعـده", 1_123],
        ["جاء المخصّص يروي أحسنَ الكَلِم", 1_322],
        ["من أنبت الغصن من صمصامة ذكر", 2_990],
    )
    @unpack
    def test_jummal_counter_sentences(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["رب", 202],
        ["ريح", 218],
        ["شعب", 372],
        ["جمر", 243],
        ["ظن", 950],
    )
    @unpack
    def test_jummal_counter_words(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["ء", 1],
        ["بهاء", 9],
        ["إيهاب", 19],
        ["بؤبؤ", 16],
        ["سائق", 171],
        ["أنس", 111],
        ["ًرمى القضاء بعيني جؤذر أسدا", 2_300],
    )
    @unpack
    def test_jummal_counter_hamza(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["بكى", 32],
    )
    @unpack
    def test_jummal_counter_alef_maksora(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["حمزة", 60],
        ["أبكمه", 68],
    )
    @unpack
    def test_jummal_counter_heh_teh_marboota(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["طغ", 1_009],
        ["بغ", 1_002],
        ["غغ", 2_000],
        ["مرغ", 1_240],
        ["بغي", 1_012],
        ["بغاء", 1_004],
    )
    @unpack
    def test_jummal_counter_tarkeeb(self, text, expected):
        assert expected == self.wrapper(text), text


@ddt
class TestJummalTarkeebAndHamza(TestCase):
    def wrapper(self, text):
        return jummal_counter(text, use_hamza=True, use_tarkeeb=True)

    @data(
        ["أ", 1],
        ["ب", 2],
        ["ج", 3],
        ["د", 4],
        ["ه", 5],
        ["و", 6],
        ["ز", 7],
        ["ح", 8],
        ["ط", 9],
        ["ي", 10],
        ["ك", 20],
        ["ل", 30],
        ["م", 40],
        ["ن", 50],
        ["س", 60],
        ["ع", 70],
        ["ف", 80],
        ["ص", 90],
        ["ق", 100],
        ["ر", 200],
        ["ش", 300],
        ["ت", 400],
        ["ث", 500],
        ["خ", 600],
        ["ذ", 700],
        ["ض", 800],
        ["ظ", 900],
        ["غ", 1_000],
    )
    @unpack
    def test_jummal_counter_single_character(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["مِنْ غَزَلٍ", 1_127],
        ["مات الشعرُ بعـده", 1_123],
        ["جاء المخصّص يروي أحسنَ الكَلِم", 1_322],
        ["من أنبت الغصن من صمصامة ذكر", 31_960],
    )
    @unpack
    def test_jummal_counter_sentences(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["رب", 202],
        ["ريح", 218],
        ["شعب", 372],
        ["جمر", 243],
        ["ظن", 950],
    )
    @unpack
    def test_jummal_counter_words(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["ء", 1],
        ["بهاء", 9],
        ["إيهاب", 19],
        ["بؤبؤ", 16],
        ["سائق", 171],
        ["أنس", 111],
        ["ًرمى القضاء بعيني جؤذر أسدا", 2_300],
    )
    @unpack
    def test_jummal_counter_hamza(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["بكى", 32],
    )
    @unpack
    def test_jummal_counter_alef_maksora(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["حمزة", 60],
        ["أبكمه", 68],
    )
    @unpack
    def test_jummal_counter_heh_teh_marboota(self, text, expected):
        assert expected == self.wrapper(text), text

    @data(
        ["طغ", 9_000],
        ["بغ", 2_000],
        ["غغ", 1_000_000],
        ["مرغ", 200_040],
        ["بغي", 2_010],
        ["بغاء", 2_002],
    )
    @unpack
    def test_jummal_counter_tarkeeb(self, text, expected):
        assert expected == self.wrapper(text), text
