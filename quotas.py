import discord

async def debutquotas2(ctx):
	with open ('quotas.json','r') as f:
		quot = json.load(f)
	def check(m):
		return m.author == ctx.author and m.channel == ctx.channel
	mes = await ctx.reply('Quels sont les quotasde la SD ?')
	SD = await bot.wait_for('message', timeout=600, check=check)
	await mes.delete()
	mes = await ctx.reply('Quels sont les quotasde la SD ?')
	quota = await bot.wait_for('message', timeout=600, check=check)
	await mes.delete()
	Elite = ctx.guild.get_role(993163816693141536)
	Bad = ctx.guild.get_role(993163825773809754)
	id = [[],[]]
	for personne in Elite.members:
		await personne.send(f'Bonjour, vous avez une semaine pour rendre {SD.content} à {ctx.author.mention}')
		id[0].append(personne.id)
	for personne in Bad.members:
		await personne.send(f'Bonjour, vous avez une semaine pour rendre {quota.content} à {ctx.author.mention}')
		id[1].append(personne.id)
	quot["semaine"] += 1
	quot["semaine"+str(quot["semaine"])] = {"SD":{"af":id[0],"fait":[]},"BD":{"af":id[1],"fait":[]}}
	with open ('quotas.json','w') as f:
		json.dump(quot,f,indent=6)
	await ctx.reply('Le message à bien été envoyé')

async def renduquotas2(ctx,divi,member):
	if divi != "SD" and divi != "BD":
		await ctx.reply("Ce n'est pas une division valide !")
		return
	if not member:
		await ctx.reply("Vous n'avez pas indiqué de membre")
		return
	with open ('quotas.json','r') as f:
		quot = json.load(f)
	if member.id not in quot["semaine"+str(quot["semaine"])][divi]["af"]:
		await ctx.reply("Cette personne n'a pas de quotas a rendre")
		return
	quot["semaine"+str(quot["semaine"])][divi]["af"].remove(member.id)
	quot["semaine"+str(quot["semaine"])][divi]["fait"].append(member.id)
	with open ('quotas.json','w') as f:
		json.dump(quot,f,indent=6)
	await member.send(f'Vous avez fait le quota de le {divi} de cette semaine !')
	await ctx.reply('Le message à bien été envoyé')

async def listequotas2(ctx,semaine):
	with open ('quotas.json','r') as f:
		quot = json.load(f)
	if not semaine or semaine > quot["semaine"] or semaine<1:
		semaine = quot["semaine"]
	message = ""
	for divi in quot["semaine"+str(semaine)].keys():
		message += f"\n__**{divi}**__\n**Non Rendu :**\n"
		for personne in quot["semaine"+str(semaine)][divi]["af"]:
			personne = bot.get_user(personne)
			message += "> "+personne.mention+"\n"
		message += "**Rendu :**\n"
		for personne in quot["semaine"+str(semaine)][divi]["fait"]:
			personne = bot.get_user(personne)
			message += "> "+personne.mention+"\n"
	await ctx.reply(embed=create_small_embed(message))