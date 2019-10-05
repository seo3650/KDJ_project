import konlpy

#test: input string is came

title = '안녕하세요'
body = '인생 족같다'

key_list = ['loss', 'marketing', 'love']
loss_list = [u'분실', u'습득', u'잃다', u'잃어버리다', u'찾다', u'ㅠㅠ', u'ㅠㅠ', u'ㅠ']
market_list = [u'월', u'일', u'시', u'모집', u'면접', u'행사', u'오전', u'오후']
love_list = [u'좋다', u'좋아하다', u'사랑', u'짝사랑', u'연애', u'썸', u'심장']

word_dict = {'loss': loss_list, 'marketing': market_list, 'love': love_list}

def score_with_word(title, body, keyword):
    """
    :param title: The title of an article
    :param body: The body of an article
    :param keyword: The category which user interests in
    :return:
    """

    pro_title, pro_body = preprocess(title, body)

    word2index = {}
    bow = []
    for voca in pro_body:
        if voca not in word2index.keys():
            word2index[voca] = len(word2index)
            # token을 읽으면서, word2index에 없는 (not in) 단어는 새로 추가하고, 이미 있는 단어는 넘깁니다.
            bow.insert(len(word2index) - 1, 1)
        # BoW 전체에 전부 기본값 1을 넣어줍니다. 단어의 개수는 최소 1개 이상이기 때문입니다.
        else:
            index = word2index.get(voca)
            # 재등장하는 단어의 인덱스를 받아옵니다.
            bow[index] = bow[index] + 1
    for voca in pro_title
        if voca in word2index.keys():
            index = word2index.get(voca)
            bow[index] = bow[index] + 1

    word_list = word_dict[keyword]

    score = 0
    for word in word_list:
        if word in word2index:
            score += word2index[word]

    return score



def preprocess(title, body):
    """
    :param title: The title of an article
    :param body: The body of an article
    :return: processed inputs
    """
    okt = konlpy.tag.Okt()
    pro_title = okt.morphs(title, norm=True, stem=True)
    pro_body = okt.morphs(body, norm=True, stem=True)
    return pro_title, pro_body


if __name__ == '__main__':
    score_with_word(title, body, keyword='차')