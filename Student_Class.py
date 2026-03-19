class Student:
    def __init__(self, name, number_of_scores):
        self.name = name
        self.test_scores = [0] * number_of_scores

    def getName(self):
        return self.name

    def getScore(self, position):
        if 1 <= position <= len(self.test_scores):
            return self.test_scores[position - 1]
        return None

    def setScore(self, position, value):
        if 1 <= position <= len(self.test_scores):
            self.test_scores[position - 1] = value

    def getHighestScore(self):
        if self.test_scores:
            return max(self.test_scores)
        return 0

    def getAverageScore(self):
        if self.test_scores:
            return sum(self.test_scores) / len(self.test_scores)
        return 0

    def __str__(self):
        return f"Student Name: {self.name}\nTests: {self.test_scores}"

if __name__ == "__main__":
    s1 = Student("Alice", 3)
    s1.setScore(1, 85)
    s1.setScore(2, 92)
    s1.setScore(3, 88)
    print(s1)
    print("Highest Score:", s1.getHighestScore())
    print("Average Score:", s1.getAverageScore())
