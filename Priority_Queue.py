class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __repr__(self):
        return f"Task(ID: {self.task_id}, Priority: {self.priority})"



class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        self.heap.append(task)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        min_task = self.heap[0]
        last_task = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_task
            self._bubble_down(0)
        return min_task

    def decrease_key(self, task_id, new_priority):
        for i in range(len(self.heap)):
            if self.heap[i].task_id == task_id:
                self.heap[i].priority = new_priority
                self._bubble_up(i)
                break

    def is_empty(self):
        return len(self.heap) == 0

    # Helper function to maintain min-heap property by bubbling up
    def _bubble_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index].priority < self.heap[parent_index].priority:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    # Helper function to maintain min-heap property by bubbling down
    def _bubble_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left].priority < self.heap[smallest].priority:
            smallest = left
        if right < len(self.heap) and self.heap[right].priority < self.heap[smallest].priority:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)

            

# Usage
pq = PriorityQueue()
pq.insert(Task(1, 7, '9:00', '10:30'))
pq.insert(Task(2, 9, '9:10', '10:35'))
pq.insert(Task(3, 4, '10:15', '11:00'))



print("Min Priority Task:", pq.extract_min())  # Task with the lowest priority value
print("Is Empty:", pq.is_empty())
pq.decrease_key(3, 1)
print("After Decreasing Priority:", pq.extract_min())
