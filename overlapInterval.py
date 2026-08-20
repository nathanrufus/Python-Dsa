"""
Overlapping Interval Problems - Easy to Hard
Common in code interviews
"""

# ============================================================================
# EASY: Merge Intervals
# ============================================================================
# Problem: Given intervals, merge overlapping ones
# Example: [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]

def merge_intervals(intervals):
    """
    Time: O(n log n), Space: O(1) or O(n) depending on sorting
    """
    if not intervals:
        return []
    
    intervals.sort()
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        # If current overlaps with last interval
        if current[0] <= last[1]:
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            merged.append(current)
    
    return merged


# Test
print("Merge Intervals:")
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
print(merge_intervals([[1,4],[4,5]]))  # [[1,5]]
print()


# ============================================================================
# EASY: Interval List Intersections
# ============================================================================
# Problem: Find intersection of two interval lists
# Example: firstList=[[0,2],[5,10]], secondList=[[1,3],[7,9]] -> [[1,2],[5,7],[9,10]]

def interval_intersection(firstList, secondList):
    """
    Two pointers approach
    Time: O(m + n), Space: O(1)
    """
    result = []
    i, j = 0, 0
    
    while i < len(firstList) and j < len(secondList):
        a_start, a_end = firstList[i]
        b_start, b_end = secondList[j]
        
        # Calculate intersection
        inter_start = max(a_start, b_start)
        inter_end = min(a_end, b_end)
        
        # If there's an intersection
        if inter_start <= inter_end:
            result.append([inter_start, inter_end])
        
        # Move pointer of interval that ends first
        if a_end < b_end:
            i += 1
        else:
            j += 1
    
    return result


# Test
print("Interval Intersection:")
print(interval_intersection([[0,2],[5,10]], [[1,3],[7,9]]))  # [[1,2],[5,7],[9,10]]
print(interval_intersection([[0,5],[1,6]], [[2,3],[5,6]]))  # [[2,3],[5,5]]
print()


# ============================================================================
# MEDIUM: Insert Interval
# ============================================================================
# Problem: Given sorted non-overlapping intervals, insert new interval and merge
# Example: intervals=[[1,5]], newInterval=[2,7] -> [[1,7]]

def insert_interval(intervals, newInterval):
    """
    Time: O(n), Space: O(n)
    """
    result = []
    new_start, new_end = newInterval
    i = 0
    
    # Add all intervals that end before new interval starts
    while i < len(intervals) and intervals[i][1] < new_start:
        result.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals with new interval
    while i < len(intervals) and intervals[i][0] <= new_end:
        new_start = min(new_start, intervals[i][0])
        new_end = max(new_end, intervals[i][1])
        i += 1
    
    result.append([new_start, new_end])
    
    # Add remaining intervals
    while i < len(intervals):
        result.append(intervals[i])
        i += 1
    
    return result


# Test
print("Insert Interval:")
print(insert_interval([[1,5]], [2,7]))  # [[1,7]]
print(insert_interval([[1,2],[3,5],[6,9]], [4,8]))  # [[1,2],[3,8],[6,9]]
print(insert_interval([[1,2],[3,5],[6,9]], [10,12]))  # [[1,2],[3,5],[6,9],[10,12]]
print()


# ============================================================================
# MEDIUM: Meeting Rooms (Check if person can attend all meetings)
# ============================================================================
# Problem: Given list of meeting intervals, check if person can attend all
# Example: [[0,30],[5,10],[15,20]] -> False (overlaps)

def can_attend_all_meetings(intervals):
    """
    Sort and check for overlaps
    Time: O(n log n), Space: O(1)
    """
    intervals.sort()
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    
    return True


# Test
print("Can Attend All Meetings:")
print(can_attend_all_meetings([[0,30],[5,10],[15,20]]))  # False
print(can_attend_all_meetings([[7,10],[2,4]]))  # True
print()


# ============================================================================
# MEDIUM: Meeting Rooms II (Minimum meeting rooms needed)
# ============================================================================
# Problem: Find minimum number of conference rooms needed
# Example: [[0,30],[5,10],[15,20]] -> 2

def min_meeting_rooms(intervals):
    """
    Using min-heap to track room availability
    Time: O(n log n), Space: O(n)
    """
    import heapq
    
    if not intervals:
        return 0
    
    intervals.sort()
    rooms = [intervals[0][1]]  # Track end times of meetings in each room
    heapq.heapify(rooms)
    
    for i in range(1, len(intervals)):
        start, end = intervals[i]
        # If earliest room is free, reuse it
        if rooms[0] <= start:
            heapq.heapreplace(rooms, end)
        else:
            heapq.heappush(rooms, end)
    
    return len(rooms)


# Test
print("Minimum Meeting Rooms:")
print(min_meeting_rooms([[0,30],[5,10],[15,20]]))  # 2
print(min_meeting_rooms([[7,10],[2,4]]))  # 1
print(min_meeting_rooms([[1,5],[1,5],[1,5]]))  # 3
print()


# ============================================================================
# HARD: Teemo Attacking (Total damage with attack cooldown)
# ============================================================================
# Problem: Calculate total damage dealt with cooldown period between hits
# Example: timeSeries=[1,4], damage=3, cooldown=2 -> 6
# Hits at 1,4. Cooldown after each hit is 2, so hits at 1 and 4 are valid.

def teemo_attacking(timeSeries, damage, cooldown):
    """
    Simulate attack sequence with cooldown
    Time: O(n), Space: O(1)
    """
    if not timeSeries:
        return 0
    
    total_damage = 0
    last_hit_time = -float('inf')
    
    for current_time in timeSeries:
        # If enough time has passed since last hit
        if current_time - last_hit_time > cooldown:
            total_damage += damage
            last_hit_time = current_time
    
    return total_damage


# Test
print("Teemo Attacking:")
print(teemo_attacking([1,4], 3, 2))  # 6
print(teemo_attacking([1,1,1,1], 3, 0))  # 12
print(teemo_attacking([1,2,3,4,5], 1, 3))  # 2
print()


# ============================================================================
# HARD: Skyline Problem
# ============================================================================
# Problem: Given buildings, draw skyline profile
# Example: [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

def skyline(buildings):
    """
    Using events and heap
    Time: O(n log n), Space: O(n)
    """
    import heapq
    from collections import defaultdict
    
    events = []
    
    # Create events for building starts and ends
    for left, right, height in buildings:
        events.append((left, 0, height))  # 0 = start
        events.append((right, 1, height))  # 1 = end
    
    events.sort()
    
    result = []
    heights = defaultdict(int)
    heights[0] = 1
    max_heap = [0]
    
    i = 0
    while i < len(events):
        curr_x = events[i][0]
        
        # Process all events at same x coordinate
        while i < len(events) and events[i][0] == curr_x:
            x, event_type, h = events[i]
            
            if event_type == 0:  # Start
                heights[h] += 1
            else:  # End
                heights[h] -= 1
                if heights[h] == 0:
                    del heights[h]
            
            i += 1
        
        # Get current max height
        max_height = max(heights.keys())
        
        # If height changed, add to result
        if not result or result[-1][1] != max_height:
            result.append([curr_x, max_height])
    
    return result


# Test
print("Skyline Problem:")
buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
print(skyline(buildings))
print()


# ============================================================================
# HARD: Employee Free Time
# ============================================================================
# Problem: Find common free time across all employees' schedules
# Example: schedule=[[[1,3],[4,6]],[[2,5]],[[7,9]]] -> [[5,7]]

def employee_free_time(schedule):
    """
    Merge all intervals and find gaps
    Time: O(n log n), Space: O(n)
    """
    # Flatten all intervals
    all_intervals = []
    for employee_schedule in schedule:
        all_intervals.extend(employee_schedule)
    
    if not all_intervals:
        return []
    
    # Sort intervals
    all_intervals.sort()
    
    # Merge overlapping intervals
    merged = [all_intervals[0]]
    for current in all_intervals[1:]:
        if current[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], current[1])
        else:
            merged.append(current)
    
    # Find gaps between merged intervals
    free_time = []
    for i in range(len(merged) - 1):
        free_time.append([merged[i][1], merged[i+1][0]])
    
    return free_time


# Test
print("Employee Free Time:")
schedule = [[[1,3],[4,6]],[[2,5]],[[7,9]]]
print(employee_free_time(schedule))  # [[5,7]]
