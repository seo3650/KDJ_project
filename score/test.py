import unittest
from konlpy.tag import Okt


'''class MyTestCase(unittest.TestCase):
    def test(self):
        okt = Okt()
        self.assertEqual(u'잃' in okt.morphs(u'잃어버리다'), True)


if __name__ == '__main__':
    unittest.main()'''

okt = Okt()
print(okt.morphs(u'9/21~9/22에 열립니다', norm=True, stem=True))
