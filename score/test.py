import unittest
from konlpy.tag import Okt


'''class MyTestCase(unittest.TestCase):
    def test(self):
        okt = Okt()
        self.assertEqual(u'잃' in okt.morphs(u'잃어버리다'), True)


if __name__ == '__main__':
    unittest.main()'''

okt = Okt()
print(okt.morphs(u'9 월 22 일에 아이패드를 잃어버렸어요..... 찾게 도와주세요 ㅠㅠㅠㅠㅠㅠ', norm=True, stem=True))
