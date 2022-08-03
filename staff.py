import discord
async def warn2(ctx, member, raison):
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !",
												 discord.Color.red()))
		return
	_embed = discord.Embed(title="Warn",
						   description="Bonjour,\nTu as été averti.e pour la raison suivante : "+raison+
									   "\nModérateur :"+ctx.author.mention
						   )
	with open('warnblame.json', 'r') as f:
		wb = json.load(f)
	try:
		wb['warns'][str(member.id)].append(raison)
	except:
		wb['warns'][str(member.id)] = [raison]
	with open('warnblame.json', 'w') as f:
		json.dump(wb, f, indent=6)
	await member.send(embed=_embed)
	log = bot.get_channel(944296375007477811)
	await ctx.reply(embed=create_small_embed('Le message a bien été envoyé à' + member.mention))
	await log.send(embed=create_small_embed(member.mention+ ' à été warn par ' +ctx.author.mention+" pour "+raison))

async def unwarn2(ctx, member : discord.Member=None, nbw=None, *, raison="Pas de raison fournie"):
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !",
												 discord.Color.red()))
		return
	try:
		nbw=int(nbw)-1
	except:
		if nbw != None:
			raison = str(nbw)+raison
	_embed = discord.Embed(title="Unwarn",
						   description="Bonjour,\nTon warn a été retiré pour la raison suivante : "+raison+
									   "\nModérateur :"+ctx.author.mention
						   )
	with open('warnblame.json', 'r') as f:
		wb = json.load(f)
	try:
		nombre = len(wb['warns'][str(member.id)])
		if nombre == 1:
			wb['warns'].pop(str(member.id))
		else:
			if nbw==None:
				await ctx.reply(embed=create_small_embed('Ce membre a plusieurs sanction, merci de préciser laquelle vous souhaitez retirer'))
				return
			wb['warns'][str(member.id)].pop(nbw)
	except:
		await ctx.reply(embed=create_small_embed("Ce membre n'a aucun warn a retirer !"))
		return
	with open('warnblame.json', 'w') as f:
		json.dump(wb, f, indent=6)
	await member.send(embed=_embed)
	log = bot.get_channel(944296375007477811)
	await ctx.reply(embed=create_small_embed('Le message a bien été envoyé à' + member.mention))
	await log.send(embed=create_small_embed(member.mention+ ' à été unwarn par ' +ctx.author.mention+" pour "+raison))

async def blame2(ctx, member : discord.Member=None, *, raison="Pas de raison fournie"):
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !",
												 discord.Color.red()))
		return
	_embed = discord.Embed(title="Blame",
						   description="Vous venez de recevoir un blâme sur le serveur SweetDream pour la raison "
									   "suivante : "+raison+"\nLes blames sont de très lourdes sanctions, pour vous "
										"racheter vous devrez donc payer :\n**Au premier :** 10 000 obsidian et 32 "
															"blocs de paladium\n**Pour le second blâme vous vous verrez"
															" derank de la faction ainsi qu'une punition de** 10 000 "
															"obsidian, deux stacks de blocs de pala et 200 000$\n**Au "
															"bout de 3 blâmes vous serez temporairement banni de la "
															"faction pour un mois**\nModérateur : "+ctx.author.mention
						   )
	with open('warnblame.json', 'r') as f:
		wb = json.load(f)
	try:
		wb['blames'][str(member.id)].append(raison)
	except:
		wb['blames'][str(member.id)] = [raison]
	with open('warnblame.json', 'w') as f:
		json.dump(wb, f, indent=6)
	await member.send(embed=_embed)
	log = bot.get_channel(944296375007477811)
	await ctx.reply(embed=create_small_embed('Le message a bien été envoyé à' + member.mention))
	await log.send(embed=create_small_embed(member.mention+ ' à été blamé par ' +ctx.author.mention+" pour "+raison))

async def unblame2(ctx, member , nbw, raison):
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !",
												 discord.Color.red()))
		return
	try:
		nbw=int(nbw)-1
	except:
		if nbw != None:
			raison = str(nbw)+raison
	_embed = discord.Embed(title="Blame",
						   description="Bonjour,\nTon warn a été retiré pour la raison suivante : "+raison+
									   "\nModérateur :"+ctx.author.mention
						   )
	with open('warnblame.json', 'r') as f:
		wb = json.load(f)
	try:
		nombre = len(wb['blames'][str(member.id)])
		if nombre == 1:
			wb['blames'].pop(str(member.id))
		else:
			if nbw==None:
				await ctx.reply(embed=create_small_embed('Ce membre a plusieurs sanction, merci de préciser laquelle vous souhaitez retirer'))
				return
			wb['blames'][str(member.id)].pop(nbw)
	except:
		await ctx.reply(embed=create_small_embed("Ce membre n'a aucun warn a retirer !"))
		return
	with open('warnblame.json', 'w') as f:
		json.dump(wb, f, indent=6)
	await member.send(embed=_embed)
	log = bot.get_channel(944296375007477811)
	await ctx.reply(embed=create_small_embed('Le message a bien été envoyé à' + member.mention))
	await log.send(embed=create_small_embed(member.mention+ ' à été unblame par ' +ctx.author.mention+" pour "+raison))

async def rankup2(ctx, member):
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !",
												 discord.Color.red()))
		return
	guild = ctx.guild
	Roles = {9:790675782338740235,8:790675782364037131,7:790675783352975360,6:790675783549976579,5:790675783693500456,
			 4:790675784120401932,3:790675784225521734,2:791066206437113897, 1:791066207418712094}
	for x in Roles.items():
		rol = guild.get_role(x[1])
		if rol in member.roles:
			role = x[0]
	if not role:
		await ctx.reply(embed=create_small_embed(":warning: Ce membre n'existe pas ou ne peux pas etre rankup !",
												 discord.Color.red()))
		return
	role1 = guild.get_role(Roles[role])
	await member.remove_roles(role1, reason=f'Fait par {str(ctx.author)[:16]}')
	role1 = guild.get_role(Roles[role+1])
	await member.add_roles(role1, reason=f'Fait par {str(ctx.author)[:16]}')
	embed_ = create_small_embed("Félicitation à "+member.mention+" qui passe "+role1.mention+" !",discord.Color.gold())
	rankup = guild.get_channel(791991289007570974)
	await rankup.send(embed=embed_)
	await member.send("Félicitation à toi, tu passes "+role1.name+" !")
	await ctx.reply("Le rankup a bien été effectué")

async def derank2(ctx, member,raison):
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !",
												 discord.Color.red()))
		return
	guild = ctx.guild
	Roles = {9:790675782338740235,8:790675782364037131,7:790675783352975360,6:790675783549976579,5:790675783693500456,
			 4:790675784120401932,3:790675784225521734,2:791066206437113897, 1:791066207418712094}
	for x in Roles.items():
		rol = guild.get_role(x[1])
		if rol in member.roles:
			role = x[0]
	if not role:
		await ctx.reply(embed=create_small_embed(":warning: Ce membre n'existe pas ou ne peux pas etre rankup !",
												 discord.Color.red()))
		return
	role1 = guild.get_role(Roles[role])
	await member.remove_roles(role1, reason=f'Fait par {str(ctx.author)[:16]}')
	role1 = guild.get_role(Roles[role-1])
	await member.add_roles(role1, reason=f'Fait par {str(ctx.author)[:16]}')
	await member.send("Tu viens de te faire dérank pour la raison suivante : "+raison)
	log = bot.get_channel(944296375007477811)
	await log.send(embed=create_small_embed(member.mention + ' à été unblame par ' + ctx.author.mention + " pour " + raison))
	await ctx.reply("Le derank a bien été effectué")

async def ban2(ctx, member,raison):
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !",discord.Color.red()))
		return
	guild = ctx.guild
	embed_ = discord.Embed(
		description="Vous avez été banni de la SweetDream pour la raison suivante : "+raison+"\nModérateur : "+ctx.author.mention,
		color=discord.Color.red()
	)
	try:
		await member.send(embed=embed_)
		message =f'Le message a bien été envoyé à {member.mention}'
	except:
		pass
		message =f"Le message n'a pas pu être envoyé à {member.mention} mais il a bien été banni"
	await guild.ban(member,reason=raison)
	log = bot.get_channel(944296375007477811)
	await log.send(embed=create_small_embed(member.mention + ' à été ban par ' + ctx.author.mention + " pour " + raison))
	await ctx.reply(embed=create_small_embed(message))

async def unban2(ctx, member,raison):
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !",
												 discord.Color.red()))
		return
	guild = ctx.guild
	await guild.unban(member,reason=raison)
	log = bot.get_channel(944296375007477811)
	await log.send(embed=create_small_embed(member.mention + ' à été unban par ' + ctx.author.mention + " pour " + raison))
	await ctx.reply(embed=create_small_embed(member.mention+"à bien été déban"))

async def sanctions2(ctx, member):
		if not member:
			await ctx.reply(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !",discord.Color.red()))
			return
		with open('warnblame.json', 'r') as f:
			wb = json.load(f)
		sanctions = "**Warns :**\n"
		try:
			for i in range(len(wb['warns'][str(member.id)])):
				sanctions += "["+str(i+1)+"] "+wb['warns'][str(member.id)][i] + "\n"
		except:
			sanctions+="Aucun warns"
		sanctions+="\n\n**Blames :**\n"
		try:
			for i in range(len(wb['blames'][str(member.id)])):
				sanctions += "[" + str(i + 1) + "] " + wb['blames'][str(member.id)][i] + "\n"
		except:
			sanctions+= "Aucun Blame"
		await ctx.reply(embed=create_small_embed('Voici les sanction de ' + member.mention + " : \n\n" + sanctions))