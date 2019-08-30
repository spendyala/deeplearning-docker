class node:
    def __init__(self, node, dist):
        self.node = node
        self.dist = dist

def if_valid_move(node, move):
    new_vertical_count = node + (8*move[0])
    if new_vertical_count < 0:
        return (False, None)
    vertical_mod = new_vertical_count % 8
    val = True
    if vertical_mod in [0, 1]:
        if move[1] > 0:
            val = True
        else:
            if vertical_mod == 1 and move[1] == -1:
                val = True
            else:
                val = False
    if vertical_mod in [6, 7]:
        if move[1] < 0:
            val = True
        else:
            if vertical_mod == 6 and move[1] == 1:
                val = True
            else:
                val = False
    new_node = new_vertical_count+move[1]
    if val and 0 <= new_node <=63:
        return (True, new_node)
    return (False, None)


def solution(src, dest):
    #Your code here
    horse_moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
    nodes_visited = {x: False for x in range(64)}
    queue = []
    nodes_visited[src] = True
    queue.append(node(src, 0))
    while(len(queue)):
        tmp_node = queue.pop(0)
        if tmp_node.node == dest:
            return tmp_node.dist
        for each_move in horse_moves:
            valid_move_res = if_valid_move(tmp_node.node, each_move)
            if valid_move_res[0]:
                if not nodes_visited[valid_move_res[1]]:
                    nodes_visited[valid_move_res[1]] = True
                    queue.append(node(valid_move_res[1], tmp_node.dist+1))
    return -1

print(solution(0, 1))
Success! You've managed to infiltrate Commander Lambda's evil organization, and finally earned yourself an entry-level position as a Minion on her space station. From here, you just might be able to subvert her plans to use the LAMBCHOP doomsday device to destroy Bunny Planet. Problem is, Minions are the lowest of the low in the Lambda hierarchy. Better buck up and get working, or you'll never make it to the top...

Why did you sign up for infiltration duty again? The pamphlets from Bunny HQ promised exotic and interesting missions, yet here you are drudging in the lowest level of Commander Lambda's organization. Hopefully you get that promotion soon...

You survived a week in Commander Lambda's organization, and you even managed to get yourself promoted. Hooray! Henchmen still don't have the kind of security access you'll need to take down Commander Lambda, though, so you'd better keep working. Chop chop!

You got the guards to teach you a card game today, it's called Fizzbin. It's kind of pointless, but they seem to like it and it helps you pass the time while you work your way up to Commander Lambda's inner circle.

Rumor has it the prison guards are inexplicably fond of bananas. You're an apple person yourself, but you file the information away for future reference. You never know when you might need to bribe a guard (or three)...

Awesome! Commander Lambda was so impressed by your efforts that she's made you her personal assistant. You'll be helping her directly with her work, which means you'll have access to all of her files-including the ones on the LAMBCHOP doomsday device. This is the chance you've been waiting for. Can you use your new access to finally topple Commander Lambda's evil empire?
