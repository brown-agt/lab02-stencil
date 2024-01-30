from agt_server.agents.base_agents.bosii_agent import BOSIIAgent
from agt_server.local_games.bosii_arena import BOSIIArena

class ReluctantAgent(BOSIIAgent):
    def setup(self):
        self.COMPROMISE, self.STUBBORN = 0, 1
        self.GOOD_MOOD, self.BAD_MOOD = 0, 1
        self.actions = [self.COMPROMISE, self.STUBBORN]
        self.curr_state = 0

    def get_action(self):
        if self.curr_state in [0, 1, 2]:
            return self.STUBBORN
        else:
            return self.COMPROMISE

    def update(self):
        opp_last_move = self.get_opp_last_action()
        if self.curr_state < 3:
            if opp_last_move == self.STUBBORN:
                self.curr_state += 1
            else:
                self.curr_state = 0
        else:
            self.curr_state = 0

if __name__ == "__main__":
    agent_name = ... # Please give your agent a name

    agent = ReluctantAgent(agent_name)
    arena = BOSIIArena(
        num_rounds=1000,
        timeout=1,
        players=[
            agent,
            ReluctantAgent("Agent_1"),
            ReluctantAgent("Agent_2"),
            ReluctantAgent("Agent_3"),
            ReluctantAgent("Agent_4")
        ]
    )
    arena.run()
