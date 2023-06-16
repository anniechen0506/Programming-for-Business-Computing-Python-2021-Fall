class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank   

    #規則a
    def is_A_or_not(self):
        if 'A' in self.rank:
            return True
        else:
            return False

#rule b: 如果你打出一對，也就是有兩張相同點數的牌，每對可以獲得10分
#數有幾個一對
    def count_pair(self):
        temp_set = set(self.rank)
        temp_list = list(temp_set)
        card_pair_score = 0

        # if len(temp_set) == 5:
        #     return 0
        # elif len(temp_set) == 4:
        #     return 10
        # elif len(temp_set) == 1:
        #     return 100    

        if len(temp_set) == 5:
            return 0
        elif len(temp_set) == 4:
            return 10
        elif len(temp_set) == 1:
            return 100  
      
        for i in temp_list:
            if len(temp_set) == 2:
                if self.rank.count(i) == 3 or self.rank.count(i) == 2: 
                    return 40
                else:
                    return 60
            elif len(temp_set) == 3:
                number = max(self.rank ,key = self.rank.count)
                if self.rank.count(number) == 3:
                    return 30
                else:
                    return 20

# rule b: 如果你打出一對，也就是有兩張相同點數的牌，每對可以獲得10分   
    def the_same_suit(self):
        temp_set = set(self.suit)
        temp_list = list(temp_set)
        if len(temp_list) == 1:
            return True
        else:
            return False


# rule d: 如果你打出順子，也就是五張順連的牌，你可以獲得50分。順連與否不考慮花色，也不因點數而中斷，比如說黑桃 、梅花 、方塊 、梅花 、黑桃  這種組合也算順連。換言之，不考慮花色的話，共有 13 種順連的方式。

    def straight_yes(self):
        if self.count_pair() != 0:
            return False
        temp_list = self.rank

        for the_index, letter in enumerate(temp_list):
          if letter == 'A':
              temp_list[the_index] = 1
          if letter == 'J':
              temp_list[the_index] = 11
          if letter == 'Q':
              temp_list[the_index] = 12
          if letter == 'K':
              temp_list[the_index] = 13

        for i in range(len(temp_list)):
            temp_list[i] = int(temp_list[i])
        temp_list.sort()

        if max(temp_list) - min(temp_list) == 4:
            return True
        elif (temp_list == [1,10,11,12,13] or temp_list == [1,2,11,12,13]
             or temp_list == [1,2,3,12,13] or temp_list == [1,2,3,4,13]):
            return True
        else:
            return False

#rule e: 如果你打出葫蘆，也就是三張同一點數的牌，加一對其他點數的牌，你可以獲得80分。

    def there_is_fullhouse(self):
        if self.count_pair() == 0:
            return False
        temp_set = set(self.rank)
        if len(temp_set) != 2:
            return False
        temp_list = list(temp_set)

        for i in temp_list:
            if (self.rank.count(i) == 3) or (self.rank.count(i) == 2):
                return True
            else:
                return False

#rule f: 如果你打出四條，也就是四張同一點數的牌，你可以獲得100分。
    def there_is_four(self):
        temp_set = set(self.rank)
        if len(temp_set) > 2:
            return False
        temp_list = list(temp_set)
        for i in temp_list:
            if len(temp_set) == 2:
                if (self.rank.count(i) == 1) or (self.rank.count(i) == 4):
                        return True
            elif len(temp_set) == 1:
                return True
            else:
                return False

#rule g 
    def there_is_straightflush(self):
        if (self.straight_yes() == True) and (self.the_same_suit() == True):
            return True
        else:
            return False

# 一個人所拿到的牌組叫做Deck，一個 Deck 中會有許多張Card
class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self,card):
        self.cards.append(card)

    def the_card_they_have(self):
        player_number = int(input())
    
        for i in range(player_number):
            the_player_deck = input().split(',')
            the_suit = []
            the_rank = []
            the_suit_rank = []
            for j in range(len(the_player_deck)):
                the_suit.append(the_player_deck[j][0:1])
                the_rank.append(the_player_deck[j][1:])
                the_suit_rank.append(the_suit)
                the_suit_rank.append(the_rank)
            final_player_deck = Card(the_suit_rank[0],the_suit_rank[1])
            self.cards.append(final_player_deck)

    def the_score_player_got(self):   
        score_list = []
        winner = []
        final_answer = ''
        for i in range(len(self.cards)):
            the_score = 0
            if self.cards[i].the_same_suit() == True:
                the_score += 30
            if self.cards[i].is_A_or_not() == True:
                the_score += self.cards[i].rank.count('A') * 5
            if self.cards[i].straight_yes() == True:
                the_score += 50
            if self.cards[i].there_is_fullhouse() == True:
                the_score += 80
            if self.cards[i].there_is_four() == True:
                if len(set(self.cards[i].rank)) == 1:
                    the_score += 500
                else:
                    the_score += 100
            if self.cards[i].there_is_straightflush() == True:
                the_score += 300
            the_score += self.cards[i].count_pair()
            score_list.append(the_score)    
        winner_get_score = max(score_list)

        for i in range(len(score_list)):
            if score_list[i] == winner_get_score:
                winner.append(i+1)

        for i in range(len(winner)):
            if i < len(winner) - 1:
                final_answer += (str(winner[i]) + ',')
            else:
                final_answer += str(winner[i])
        return final_answer


the_card_game = Deck()
the_card_game.the_card_they_have()
print(the_card_game.the_score_player_got())
