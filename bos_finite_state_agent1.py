from agt_server.agents.base_agents.bosii_agent import BOSIIAgent
from agt_server.local_games.bos_arena import BOSArena
from bos_reluctant import ReluctantAgent

class BoSFSAgent1(BOSIIAgent):
    def setup(self):
        self.COMPROMISE, self.STUBBORN = 0, 1
        self.actions = [self.COMPROMISE, self.STUBBORN]
        self.curr_state = 0
    
    def get_action(self):
        """
        Return either self.STUBBORN or self.COMPROMISE based on the current state of the 
        game, as stored in the instance variable this.currentState. Note that this.currentState is initialized to 0, 
        which represents your initial state.
        """
        #TODO: Implement this section
        raise NotImplementedError

    def update(self):
        """
        This should, based on your current state, and the actions taken by each player in the previous round of the 
        game (which are derived from the game report received after each round), updates self.curr_state to reflect
        the new state of the game.
        """
        my_last_move = self.get_last_action()
        opp_last_move = self.get_opp_last_action()
        #TODO: Implement this section
        raise NotImplementedError
        

if __name__ == "__main__":
    agent_name = ... # Please give your agent a name

    agent = BoSFSAgent1(agent_name)
    arena = BOSArena(
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
