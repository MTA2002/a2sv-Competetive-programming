class Solution:
    def bestClosingTime(self, customers: str) -> int:
        customer_count = customers.count('Y')
        min_ = float('inf')
        min_idx = -1

        for i in range(len(customers)):
            if min_ > customer_count:
                min_ = customer_count
                min_idx = i

            if customers[i] == 'Y':
                customer_count -= 1
            else:
                customer_count += 1

        if min_ > customer_count:
            min_ = customer_count
            min_idx = len(customers)

        return min_idx
