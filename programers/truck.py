bridge_length = 3
weight = 10
truck_weights = [7, 4, 5, 6]


def solution(bridge_length, weight, truck):
    answer = 0
    queue = [0]*bridge_length
    seconds = 0
    while queue:
        seconds += 1
        queue.pop(0)
        if truck:
            if sum(queue) + truck[0] <= weight:
                queue.append(truck.pop(0))
            else:
                queue.append(0)

    answer = seconds

    return answer


solution(2, 10, truck_weights)
