def sanitize(timestr):
	if '-' in timestr :
		splitter = '-'
	elif ':' in timestr :
		splitter = ':'
	else :
		return(timestr)

	(mins, secs) = timestr.split(splitter)
	return(mins+ '.'+ secs)