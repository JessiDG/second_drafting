#the purpose of this program is to help me find trouble spots in my writing

class SecondDrafting:

    def __init__(self, text):
        self._text = text

    def check_repetition(self, text):
        word_list = []
        common_word_list = ['and', 'the', 'or', 'is', 'of', 'was', 'if', 'her', 'hers', 'she',
                            'he', 'his', 'him', 'they', 'them', 'their']
        updated_sentence = ""
        for word in text.split():
            if word in word_list and word not in common_word_list:
                new_word = "**"+str(word)+"**"
                updated_sentence += new_word + " "
            else:
                word_list.append(word)
                updated_sentence += word + " "
        return updated_sentence

    def check_repetitive_punctuation(self, text, punctuation):
        updated_sentence = ""
        for i in text:
            if i == punctuation:
                new_punctuation = '**' + str(punctuation) + "**"
                updated_sentence += new_punctuation
            else:
                updated_sentence += i
        return updated_sentence

    def check_adverbs(self, text):
        updated_sentence = ""
        for word in text.split():
            # print()
            # print(word[(len(word) - 2):(len(word))])
            if word[(len(word) - 2):(len(word))] == 'ly':
                new_word = '**'+word+'**'
                updated_sentence += new_word +' '
            else:
                updated_sentence += word + ' '
        return updated_sentence

    def check_gerunds(self, text):
        updated_sentence = ""
        for word in text.split():
            if word[(len(word) - 3):(len(word))] == 'ing':
                new_word = '**' + word + '**'
                updated_sentence += new_word + ' '
            else:
                updated_sentence += word + ' '
        return updated_sentence

    def check_infinitives(self, text):
        updated_sentence = ""
        for word in text.split():
            if word == 'to':
                new_word = '**' + word + '**'
                updated_sentence += new_word + ' '
            else:
                updated_sentence += word + ' '
        return updated_sentence

    def check_everything(self, text, punct0=';', punct1='—', punct2='–'):
        text_no_repetition = self.check_repetition(text)
        text_repetitive_punctuation0 = self.check_repetitive_punctuation(text_no_repetition, punct0)
        text_repetitive_punctuation1 = self.check_repetitive_punctuation(text_repetitive_punctuation0, punct1)
        text_repetitive_punctuation2 = self.check_repetitive_punctuation(text_repetitive_punctuation1, punct2)
        text_adverbs = self.check_adverbs(text_repetitive_punctuation2)
        text_gerunds = self.check_gerunds(text_adverbs)
        text_infinitives = self.check_infinitives(text_gerunds)
        return text_infinitives

    def chat_bot(self):
        usr = input('what text would you like to check?\n')
        return self.check_everything(usr)

    def __str__(self):
        return self._text

# class byParagraph:

if __name__ == "__main__":
    string0 = "and and ; ; — —. happily singing singer to dance"
    sd = SecondDrafting(string0)
    # print(sd)
    # print(sd.check_repetition(string0))
    # print(sd.check_repetitive_punctuation(string0, ';'))
    # print(sd.check_repetitive_punctuation(string0, '—'))
    #print(sd.check_adverbs(string0))
    # print(sd.check_gerunds(string0))
    # print(sd.check_infinitives(string0))
    # print(sd.check_everything(string0))
    # string1 = "The en dash is used to represent a span or range of numbers, dates, or time. There should be no space between the en dash and the adjacent material. Depending on the context, the en dash is read as “to” or “through.”"
    # print(sd.check_everything(string1))
    # string2 = "The other young man nodded. Brian wondered if the utter silence of the three hour drive from the Idaho Falls Greyhound station was part of the Basic Military Training now or whether this Airman was just the silent type. Brian had gone through BMT five years ago, about six months after Hiroshima and Nagasaki. His instructors had been so shell-shocked, he had no idea if they’d covered protocol for situations like this."
    # print(sd.check_everything(string2))
    # string3 = "Brian held himself stiffly in the pre-war era Ford’s backseat as they bumped along the ill-paved county road. Every jerking pothole yanked the barely-scabbed over belt marks on his back. His face was stony where the Junior Airman driver could see, but his hand was digging new bruises over the old ones on his knees, fingers tucked between the perfect creases of his dress uniform. His first day at work and he wouldn't be able to sit back in any chair he was offered. Not that the world’s first nuclear power plant’s new Security Director will have a lot of sitting to do. About five minutes left, Staff Sergeant Flinn. Thank you, Airman. The other young man nodded. Brian wondered if the utter silence of the three " \
    # "hour drive from the Idaho Falls Greyhound station was part of the Basic Military Training now or whether this Airman was just the silent type. Brian had gone through BMT five years ago, about six months after Hiroshima and Nagasaki. His instructors had been so shell-shocked, he had no idea if they’d covered protocol for situations like this. Brian kept his eyes on the impossibly-flat, horizon-daring high desert of central Idaho. There was scrub here, a bit greener than what he'd grown-up with on the blue-red mesas of southeastern New Mexico. The mountains here looked like weapons, holding none of the softening of arroyos of his home. Just saw-toothed peaks and man-eating snow drifts. He could see their destination on the horizon; there wasn\'t anything else to look at in the ' \
    #                                                      'middle distance. The Experimental Breeder Reactor (EBR-1) was big cinderblock cube in the middle of the desert. Site chosen because if we all blow ourselves up tomorrow, it\'ll be a thousand years of poisoned water for the cows rather than a real metropolitan area."
    # print(sd.check_everything(string3))
    print(sd.chat_bot())

