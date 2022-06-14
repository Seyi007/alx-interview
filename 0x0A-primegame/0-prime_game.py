#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    players = ('Maria', 'Ben')
    winners = []
    if type(x) != int or x <= 0 or type(nums) != list:
        return None
    nums_len = len(nums) if nums else 0
    for i in range(x):
        n = nums[i % nums_len] if nums else 0
        if type(n) != int:
            continue
        n_nums = list(range(1, n + 1, 1))
        prime = 2
        turns = 0
        while True:
            removal_ocurred = False
            p_multiples = list(range(prime, n + 1, prime))
            for p_multiple in p_multiples:
                if p_multiple in n_nums and prime in n_nums:
                    n_nums.remove(p_multiple)
                    removal_ocurred = True
            if removal_ocurred:
                turns += 1
                for val in n_nums:
                    if val > prime:
                        prime = val
                        break
            else:
                break
        winners.append(players[(turns + 1) % 2])
    marias_wins = winners.count(players[0])
    bens_wins = winners.count(players[1])
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
