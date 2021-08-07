	# if data["status"] == "OK": 
	# 	contests = [] 
	# 	for contest in data["result"]:
	# 		if contest["phase"] != 'BEFORE': 
	# 			break 
	# 		# contests.append(Contest(**contest))
	# 		await ctx.channel.send(contest["phase"]) 
	# 	# for i in contests: 
	# 	# 	await ctx.channel.send(str(i.id) + " " + str(i.name))	
	# else: 
	# 	await ctx.channel.send(APICallFailedException(data["comment"]))