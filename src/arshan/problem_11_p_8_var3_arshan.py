from protocol.problem_11_p_8_var3 import Problem11P8Var3


class Problem11P8Var3Arshan(Problem11P8Var3):
    def place_the_mailbox(self, buildings):
        return self.better_solution(buildings)
        return self.brute_force(buildings)

    def brute_force(self, buildings):
        max_distance = max([b.distance for b in buildings])
        min_cost, min_places = float('inf'), []
        for i in range(max_distance + 1):
            cost = 0
            for b in buildings:
                cost += b.num_of_residents * abs(b.distance - i)
            if min_cost == cost:
                min_places.append(i)
            if cost < min_cost:
                min_cost, min_places = cost, [i]
        return min_places[0]

    def better_solution(self, buildings):
        total_residents = sum([b.num_of_residents for b in buildings])
        buildings = sorted(buildings, key=lambda b: b.distance)
        residents_to_left = 0
        for i, b in enumerate(buildings):
            residents_to_right = total_residents - residents_to_left - b.num_of_residents
            if residents_to_right <= residents_to_left:
                return i
            residents_to_left += b.num_of_residents
        return buildings[-1].distance
