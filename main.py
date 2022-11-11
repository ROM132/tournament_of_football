import random


class tournament:

    teams = {
        1: ["Barcelona", "Real Madrid", "Atletico Madrid", "Real Betis", "Osasuna", "Villarreal", "Athletic Bilbao", "Rom team"],
    }

    update_teams = {
        1: []
    }

    def __init__(self):
        # split_teams
        random.shuffle(self.teams[1])

        # Round_one
        self.score_team_one = random.randint(0, 4)
        self.score_team_two = random.randint(0, 4)

        self.team_one_number = 0
        self.team_two_number_ = 1

        # check_winner_Round_one
        self.match_number_index = 0

        # Round_Two
        self.check = False

        # check if the game is final or semi-final
        self.check_semi_final = False
        self.check_final = False

        self.final = None
        self.final_num = 0


    def Round_one(self):
        self.score_team_one = random.randint(0, 4)
        self.score_team_two = random.randint(0, 4)

        if len(self.update_teams[1]) == 2 and self.check is True:
            t.Rest_all()
            exit()


        if len(self.update_teams[1]) == 4:
            self.check = True
            t.Rest_all()

        o1 = self.teams[1][self.team_one_number]
        o2 = self.teams[1][self.team_two_number_]


        while True:
            if self.score_team_one > self.score_team_two:
                t.check_winner_Round_one(o1, o2)

            elif self.score_team_one < self.score_team_two:
                t.check_winner_Round_one(o2, o1)

            elif self.score_team_one == self.score_team_two:
                t.check_winner_Round_one(o1, o2)

    def Rest_all(self):
        self.check_semi_final = True
        random.shuffle(self.teams[1])
        self.teams[1] = self.update_teams[1]
        self.score_team_one = random.randint(0, 4)
        self.score_team_two = random.randint(0, 4)
        self.team_one_number = 0
        self.team_two_number_ = 1
        self.match_number_index = 0
        self.update_teams[1] = []
        if self.check_final is True:
            print(
                f"\nOk this is the teams that made it to the final are:\n{self.teams[1][0]}, {self.teams[1][1]}\n")
            self.match_number_index = 4
            self.check_semi_final = False
        if self.check_semi_final is True:
            self.check_final = True
            print(f"\nOk this is the teams that goes to the semi final are:\n{self.teams[1][0]}, {self.teams[1][1]}, {self.teams[1][2]}, {self.teams[1][3]}\n")
        t.Round_one()

    def check_winner_Round_one(self, winner, loser):
        match_number = ["First", "Second", "Third", "Fourth", "Last"]
        winner_loser_randomize = [winner, loser]
        random.shuffle(winner_loser_randomize)
        self.final = winner

        input(f"\nOk the {match_number[self.match_number_index]} Game is Between\n{winner_loser_randomize[0]} Vs {winner_loser_randomize[1]}\nPress enter to see the result: ")
        if self.score_team_one == self.score_team_two:
            input(f"The result of the {match_number[self.match_number_index]} Game is:\n{self.score_team_one} - {self.score_team_two} So its a Draw\nPress enter to do a Rematch game: ")
            self.score_team_one = random.randint(1, 3)
            self.score_team_two = random.randint(1, 3)
            t.Round_one()
        else:
            print(f"The result of the {match_number[self.match_number_index]} Game is:\n{self.score_team_one} - {self.score_team_two} To {winner}")
            t.winner_check()
            self.match_number_index += 1
            self.team_one_number += 2
            self.team_two_number_ += 2
            self.update_teams[1].append(winner)
            self.final_num += 1
            t.Round_one()

    def winner_check(self):
        if self.check_final is True and self.match_number_index == 4 and self.final_num == 6:
            print(f"The big winner is:\n{self.final}!!")
            exit()


t = tournament()
t.Round_one()
