    def cheapest_insertion(self):
        best_tour, best_length = None, float('inf')
        # store intermediate tours for visualization purposes
        best_tours, best_lengths = [], []
        city = randrange(1, self.size)
        # we start the tour with one node I
        tour, tours, tour_lengths = [city], [], []
        # we find the closest node R to the first node
        neighbor, length = self.closest_neighbor(tour, city)
        tour_length = length
        tour_lengths.append(length)
        tour.append(neighbor)
        while len(tour) != len(self.cities):
            length, tour = self.add_closest_to_tour(tour)
            tour_length += length
            tours.append(tour)
            tour_lengths.append(tour_length)
        tour_length += self.distances[tour[-1]][tour[0]]
        tour_lengths.append(tour_length)
        lengths = [sum(tour_lengths[:3])] + tour_lengths[3:]
        return [self.format_solution(step) for step in tours], lengths