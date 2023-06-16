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

the_cards = Card(input().split(','), input().split(','))
the_score = 0

# rule a: 如果你打出一張A，你可以獲得5分
if the_cards.is_A_or_not() == True:
    the_score += the_cards.rank.count('A') * 5

#rule b: 如果你打出一對，也就是有兩張相同點數的牌，每對可以獲得10分
the_score += the_cards.count_pair()

#rule c: 如果你打出同花，也就是五張同一花色的牌，你可以獲得30分。
if the_cards.the_same_suit() == True:
    the_score += 30

if the_cards.straight_yes() == True:
    the_score += 50

if the_cards.there_is_fullhouse() == True:
    the_score += 80

if the_cards.there_is_four() == True:
    if len(set(the_cards.rank)) == 1: 
        the_score += 500
    else:
        the_score += 100

if the_cards.there_is_straightflush() == True:
    the_score += 300

print(the_score) 
