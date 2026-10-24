class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def date_to_day(date_str):
            month = int(date_str[:2])
            day = int(date_str[3:])
            return sum(days_in_months[:month - 1]) + day
        start_alice = date_to_day(arriveAlice)
        end_alice = date_to_day(leaveAlice)
        start_bob = date_to_day(arriveBob)
        end_bob = date_to_day(leaveBob)
        start_overlap = max(start_alice, start_bob)
        end_overlap = min(end_alice, end_bob)
        start_overlap = max(start_alice, start_bob)
        end_overlap = min(end_alice, end_bob)
        return max(0, end_overlap - start_overlap + 1)
        