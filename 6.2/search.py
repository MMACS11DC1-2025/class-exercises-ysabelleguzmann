file = open("6.2/spotify.csv")
junk = file.readline()

drake_data = []

for line in file:
	items = line.strip().split(",")
	artist = str(items[-1])
	songtitle = str(items[-2])
	danceability = float(items[1])
	
	if artist == "Drake":
		drake_data.append([danceability, songtitle, artist])

print("Dance score \tSong")
for item in drake_data:
	print(str(item[0]) + "\t\t" + item[1] + " by " + item[2])

#lowest to highest

for i in range(len(drake_data)):
	lowest = drake_data[i]
	lowest_index = i

	for j in range(i + 1, len(drake_data)):
		if drake_data[j] > lowest:
			lowest = drake_data[j]
			lowest_index = j

	drake_data[lowest_index], drake_data[i] = drake_data[i], drake_data[lowest_index]


print(drake_data)