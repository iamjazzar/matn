from unittest import TestCase

from ddt import data, ddt, unpack

from matn.counters import jummal


@ddt
class TestJummalNormal(TestCase):
    def setUp(self) -> None:
        self.kwargs = {"use_hamza": False, "use_tarkeeb": False}

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
    def test_jummal_single_character(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(
        ["مِنْ غَزَلٍ", 1_127],
        ["مات الشعرُ بعـده", 1_123],
        ["جاء المخصّص يروي أحسنَ الكَلِم", 1_321],
        ["من أنبت الغصن من صمصامة ذكر", 2_990],
    )
    @unpack
    def test_jummal_sentences(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(
        ["رب", 202],
        ["ريح", 218],
        ["شعب", 372],
        ["جمر", 243],
        ["ظن", 950],
    )
    @unpack
    def test_jummal_words(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

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
    def test_jummal_hamza(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(
        ["بكى", 32],
    )
    @unpack
    def test_jummal_alef_maksora(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(
        ["حمزة", 60],
        ["أبكمه", 68],
    )
    @unpack
    def test_jummal_heh_teh_marboota(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(
        ["طغ", 1_009],
        ["بغ", 1_002],
        ["غغ", 2_000],
        ["مرغ", 1_240],
        ["بغي", 1_012],
        ["بغاء", 1_003],
        ["شغل الدموع عن الديار بكاؤنا   لبكاء فاطمــة على أولادها", 2_273],
    )
    @unpack
    def test_jummal_tarkeeb(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(["مــــــــغــــارة", 1_246])
    @unpack
    def test_not_clean(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))


@ddt
class TestJummalUseTarkeeb(TestCase):
    def setUp(self) -> None:
        self.kwargs = {"use_hamza": False, "use_tarkeeb": True}

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
    def test_jummal_single_character(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(
        ["مِنْ غَزَلٍ", 1_127],
        ["مات الشعرُ بعـده", 1_123],
        ["جاء المخصّص يروي أحسنَ الكَلِم", 1_321],
        ["من أنبت الغصن من صمصامة ذكر", 31_960],
    )
    @unpack
    def test_jummal_sentences(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(
        ["رب", 202],
        ["ريح", 218],
        ["شعب", 372],
        ["جمر", 243],
        ["ظن", 950],
    )
    @unpack
    def test_jummal_words(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

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
    def test_jummal_hamza(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(
        ["بكى", 32],
    )
    @unpack
    def test_jummal_alef_maksora(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(
        ["حمزة", 60],
        ["أبكمه", 68],
    )
    @unpack
    def test_jummal_heh_teh_marboota(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(
        ["طغ", 9_000],
        ["بغ", 2_000],
        ["غغ", 1_000_000],
        ["مرغ", 200_040],
        ["بغي", 2_010],
        ["بغاء", 2_001],
        ["شغل الدموع عن الديار بكاؤنا   لبكاء فاطمــة على أولادها", 300_973],
    )
    @unpack
    def test_jummal_tarkeeb(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(["مــــــــغــــارة", 40_206])
    @unpack
    def test_not_clean(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))


@ddt
class TestJummalUseHamza(TestCase):
    def setUp(self) -> None:
        self.kwargs = {"use_hamza": True, "use_tarkeeb": False}

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
    def test_jummal_single_character(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(
        ["مِنْ غَزَلٍ", 1_127],
        ["مات الشعرُ بعـده", 1_123],
        ["جاء المخصّص يروي أحسنَ الكَلِم", 1_322],
        ["من أنبت الغصن من صمصامة ذكر", 2_990],
    )
    @unpack
    def test_jummal_sentences(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(
        ["رب", 202],
        ["ريح", 218],
        ["شعب", 372],
        ["جمر", 243],
        ["ظن", 950],
    )
    @unpack
    def test_jummal_words(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

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
    def test_jummal_hamza(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(
        ["بكى", 32],
    )
    @unpack
    def test_jummal_alef_maksora(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(
        ["حمزة", 60],
        ["أبكمه", 68],
    )
    @unpack
    def test_jummal_heh_teh_marboota(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(
        ["طغ", 1_009],
        ["بغ", 1_002],
        ["غغ", 2_000],
        ["مرغ", 1_240],
        ["بغي", 1_012],
        ["بغاء", 1_004],
        ["شغل الدموع عن الديار بكاؤنا   لبكاء فاطمــة على أولادها", 2_274],
    )
    @unpack
    def test_jummal_tarkeeb(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(["مــــــــغــــارة", 1_246])
    @unpack
    def test_not_clean(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))


@ddt
class TestJummalTarkeebAndHamza(TestCase):
    def setUp(self) -> None:
        self.kwargs = {"use_hamza": True, "use_tarkeeb": True}

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
    def test_jummal_single_character(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(
        ["مِنْ غَزَلٍ", 1_127],
        ["مات الشعرُ بعـده", 1_123],
        ["جاء المخصّص يروي أحسنَ الكَلِم", 1_322],
        ["من أنبت الغصن من صمصامة ذكر", 31_960],
    )
    @unpack
    def test_jummal_sentences(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(
        ["رب", 202],
        ["ريح", 218],
        ["شعب", 372],
        ["جمر", 243],
        ["ظن", 950],
    )
    @unpack
    def test_jummal_words(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

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
    def test_jummal_hamza(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(
        ["بكى", 32],
    )
    @unpack
    def test_jummal_alef_maksora(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(
        ["حمزة", 60],
        ["أبكمه", 68],
    )
    @unpack
    def test_jummal_heh_teh_marboota(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(
        ["طغ", 9_000],
        ["بغ", 2_000],
        ["غغ", 1_000_000],
        ["مرغ", 200_040],
        ["بغي", 2_010],
        ["بغاء", 2_002],
        ["شغل الدموع عن الديار بكاؤنا   لبكاء فاطمــة على أولادها", 300_974],
    )
    @unpack
    def test_jummal_tarkeeb(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))

    @data(["مــــــــغــــارة", 40_206])
    @unpack
    def test_not_clean(self, text, expected):
        self.assertEqual(expected, jummal(text, **self.kwargs))
