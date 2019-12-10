# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.word_masked = ['_'for _ in range(len(self.word))]
        self.word_tried = []
        self.word_map = {}
        for i, char in enumerate(self.word):
            if char not in self.word_map:
                self.word_map[char] = [i]
            else:
                self.word_map[char].append(i)

    def guess(self, char):
        if self.remaining_guesses < 0 or self.status != STATUS_ONGOING:
            raise ValueError('Remaining geusses off')
        elif char not in self.word_map or char in self.word_tried:
            self.remaining_guesses -= 1
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE
        else:
            for index in self.word_map.get(char):
                self.word_masked[index] = char
            if '_' not in self.word_masked:
                self.status = STATUS_WIN
        self.word_tried.append(char)

    def get_masked_word(self):
        return ''.join(map(str, self.word_masked))

    def get_status(self):
        return self.status
