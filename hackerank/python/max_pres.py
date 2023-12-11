def maxPresentations(scheduleStart, scheduleEnd):
    presentations = list(zip(scheduleStart, scheduleEnd))
    presentations.sort(key=lambda x: x[1])  # Sort by end times in ascending order

    selected_presentations = 0
    last_end_time = 0

    for start, end in presentations:
        if start >= last_end_time:
            # Presentation doesn't overlap with previous ones
            selected_presentations += 1
            last_end_time = end

    return selected_presentations

if __name__ == '__main__':
    scheduleStart_count = int(input().strip())
    scheduleStart = [int(input().strip()) for _ in range(scheduleStart_count)]

    scheduleEnd_count = int(input().strip())
    scheduleEnd = [int(input().strip()) for _ in range(scheduleEnd_count)]

    result = maxPresentations(scheduleStart, scheduleEnd)

    print(result)
