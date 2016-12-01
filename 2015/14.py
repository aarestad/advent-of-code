import re

parser = re.compile(r'([A-Za-z]+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.')

reindeer = []

class Reindeer:
	def __init__(self, name, speed, flight_time, rest_time):
		self.name = name
		self.speed = speed
		self.flight_time = flight_time
		self.rest_time = rest_time
		self.distance_traveled = 0
		self.score = 0

	def __str__(self):
		return "%s: speed %s, flight time %s, rest time %s, distance %s, score %s" % (
		self.name, self.speed, self.flight_time, self.rest_time, self.distance_traveled, self.score)

	def __repr__(self): return self.__str__()

with open('input_14.txt') as input_14:
	for line in input_14:
		match = parser.match(line)
		reindeer.append(Reindeer(match.group(1), int(match.group(2)), int(match.group(3)), int(match.group(4))))

def distance_traveled_by_reindeer(reindeer, time_to_travel):
	distance = 0
	traveling_speed = reindeer.speed
	traveling_time = reindeer.flight_time
	rest_time = reindeer.rest_time

	while time_to_travel > 0:
		if time_to_travel >= traveling_time:
			distance += traveling_time * traveling_speed
			time_to_travel -= traveling_time
		else:
			distance += time_to_travel * traveling_speed
			time_to_travel = 0

		if time_to_travel >= rest_time:
			time_to_travel -= rest_time
		else:
			time_to_travel = 0

	return distance

# flight_time = 10
# rest_time = 5
# flight_second if flight_second % 15 < 10

def simulate_second(current_second, reindeer):
	top_distance = 0

	for r in reindeer:
		total_interval = r.flight_time + r.rest_time

		if current_second % total_interval < r.flight_time: r.distance_traveled += r.speed

		if r.distance_traveled > top_distance: top_distance = r.distance_traveled

	for r in reindeer:
		if r.distance_traveled == top_distance: r.score += 1

	#for r in reindeer: print(r)

for r in reindeer:
	print("%s travelled %s km" % (r.name, distance_traveled_by_reindeer(r, 2503)))

for second in range(2503):
	#print('Second %s' % second)
	simulate_second(second, reindeer)

print([r.score for r in reindeer])
