from game.scripting.action import Action


# TODO: Implement MoveActorsAction class here! 

# Override the execute(cast, script) method as follows:
class MoveActorsAction(Action):
    
    def execute(self, cast, script):
        actors = cast.get_actors(script)
        for i in actors:
            i.move_next()

# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor 