class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        # 1 4
        # 4 6
        # 7 8
        # 10 10 -> 1

        # 4 1 0 7 
        # 5 3 2 8
        # 6 5 4 9
        # 7 7(x) 6 10(O)
        # 8 - 8(x) 10(O)
        # 9 - - 10(O)
        # 10(O) - - 10(O)

        # 7 4 1 0 
        # 3 3 5 10


        for i in range(len(position)):
            cars.append((position[i], speed[i])) # posi , speed
        cars.sort(key=lambda car: car[0], reverse=True)
        
        count = 0
        if len(cars) <= 1:
            count += len(cars)
            return count

        tmp = []
        for posi, speed in cars:
            time = (target-posi) / speed
            if len(tmp) <1 or time > tmp[-1]:
                tmp.append(time)
            # print(tmp)
                
        return len(tmp)                    