class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        l = 0
        count = {}
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            
            values = sorted(list(count.values()), reverse=True)
            max_count = values[0]
            # print(l, r)
            if len(values) >= 2 and sum(values) - max_count > k:
                # Go next
                while l < r and len(values) >= 2 and sum(values) - max_count > k:
                    count[s[l]] -= 1                    
                    l += 1
                    values = sorted(list(count.values()), reverse=True)
                    max_count = values[0]
                    # print(f"move l to {l} since {sum(values)} - {max_count} > {k}")

            else:
                max_len = max(max_len, r-l+1) 

        return max_len
        # test_ = {"A": 3, "B": 5}
        # print(sorted(list(test_.values()), reverse=True))
        # print(sum(test_.values()))
            

    # X Y Y X A B C
    # * - - *
    # * - - * /
    #   * * - * /
    
    # A A A B A B B
    # * * * - * /
    #   * * - * - / -> 2 vs 2

    # if Most + others (<= k)

                


