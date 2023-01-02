import collections
def solution(participant, completion):
    participant = collections.Counter(participant)
    completion = collections.Counter(completion)
    result = participant-completion
    return "".join(result)