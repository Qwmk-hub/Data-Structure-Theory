class TreeNode:
    def __init__(self, score):
        self.score = score
        self.count = 1
        self.size = 1
        self.left = None
        self.right = None

class LeaderboardTree:
    def __init__(self):
        self.root = None

    def _size(self, node):
        return node.size if node else 0

    def _update(self, node):
        node.size = node.count + self._size(node.left) + self._size(node.right)

    def insert(self, node, score):
        if node is None:
            return TreeNode(score)

        diff = score - node.score

        if diff > 0:
            node.left = self.insert(node.left, score)
        elif diff < 0:
            node.right = self.insert(node.right, score)
        else:
            node.count += 1

        self._update(node)
        return node

    def delete(self, node, score):
        if node is None:
            return None

        diff = score - node.score

        if diff > 0:
            node.left = self.delete(node.left, score)
        elif diff < 0:
            node.right = self.delete(node.right, score)
        else:
            if node.count > 1:
                node.count -= 1
            elif node.left and node.right:
                predecessor = node.left
                while predecessor.right:
                    predecessor = predecessor.right
                node.score = predecessor.score
                node.count = predecessor.count
                predecessor.count = 1
                node.left = self.delete(node.left, predecessor.score)
            else:
                return node.left or node.right

        self._update(node)
        return node

    def rank(self, node, score):
        if node is None:
            return 1

        diff = score - node.score
        left_size = self._size(node.left)

        if diff > 0:
            return self.rank(node.left, score)
        elif diff < 0:
            return left_size + node.count + self.rank(node.right, score)
        else:
            return left_size + 1

    def score_by_rank(self, node, rank):
        if node is None:
            return -1

        left_size = self._size(node.left)

        if rank <= left_size:
            return self.score_by_rank(node.left, rank)
        elif rank <= left_size + node.count:
            return node.score
        else:
            return self.score_by_rank(node.right, rank - left_size - node.count)

    def add(self, score):
        self.root = self.insert(self.root, score)

    def remove(self, score):
        self.root = self.delete(self.root, score)

    def get_rank(self, score):
        return self.rank(self.root, score)

    def get_score_by_rank(self, rank):
        return self.score_by_rank(self.root, rank)

    def total(self):
        return self._size(self.root)

class Leaderboard:
    def __init__(self):
        self.tree = LeaderboardTree()
        self.players = {}

    def add_score(self, player_id, score):
        if player_id in self.players:
            current_score = self.players[player_id]
            if score <= current_score:
                return self.tree.get_rank(current_score)
            self.tree.remove(current_score)

        self.players[player_id] = score
        self.tree.add(score)
        return self.tree.get_rank(score)

    def get_rank(self, player_id):
        if player_id not in self.players:
            return -1
        return self.tree.get_rank(self.players[player_id])

    def get_score_by_rank(self, rank):
        if rank <= 0 or rank > self.tree.total():
            return -1
        return self.tree.get_score_by_rank(rank)

def main():
    import sys
    input = sys.stdin.readline
    write = sys.stdout.write

    leaderboard = Leaderboard()

    while True:
        line = input()
        if not line:
            break
        tokens = line.strip().split()
        try:
            if tokens[0] == "add_score":
                result = leaderboard.add_score(int(tokens[1]), int(tokens[2]))
            elif tokens[0] == "get_rank":
                result = leaderboard.get_rank(int(tokens[1]))
            elif tokens[0] == "get_score_by_rank":
                result = leaderboard.get_score_by_rank(int(tokens[1]))
            else:
                result = -1
        except:
            result = -1
        write(str(result) + '\n')

if __name__ == "__main__":
    main()
