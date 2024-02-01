from agt_server.agents.base_agents.bosii_agent import BOSIIAgent
from agt_server.local_games.bos_arena import BOSArena

class BoSComp(BOSIIAgent):
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
    #TODO: Please fill out the following section
    agent_name = ... # Please give your agent a name
    ip = ... # Please write the ip as a string
    port = ... # Please write the port as an int 
    join_server = False # Please set this to True when you want to join the server

    agent = BoSComp(agent_name)
    
    if join_server:
        agent.connect(ip=ip, port=port)
    else: 
        arena = BOSArena(
            num_rounds=1000,
            timeout=1,
            players=[
                agent,
                BoSComp("Agent_1"),
                BoSComp("Agent_2"),
                BoSComp("Agent_3"),
                BoSComp("Agent_4")
            ]
        )
        arena.run()
