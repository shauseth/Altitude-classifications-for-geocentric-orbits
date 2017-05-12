altitude = int(raw_input("Altitude (in kms): \n"))

def orbit(dist):
	if dist < 160:
		if dist == 42:
			return "I see what you did there."
		else:
			return "That's not high enough to reach orbit!"
	elif dist in range(160, 2000):
		return "Low Earth orbit (LEO)"
	elif dist in range(2000, 35786):
		return "Medium Earth orbit (MEO)"
	elif dist == 42164:
		return "Geosynchronous orbit (GSO) or Geostationary orbit(GEO)"
	elif dist > 35786:
		return "High Earth orbit"

print orbit(altitude)