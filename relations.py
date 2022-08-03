import discord
async def addpna2(ctx,faction,member):
	if not faction:
		await ctx.reply(embed=create_small_embed(":warning: Vous n'avez pas spécifié de faction !",discord.Color.red()))
		return
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Vous n'avez pas spécifié d'Ambassadeur !",discord.Color.red()))
		return
	with open('rela.json', 'r') as f:
		rela = json.load(f)
	rela["pna"][faction] = {member.id:[]}
	with open('rela.json', 'w') as f:
		json.dump(rela, f, indent=6)
	await edditally()
	await ctx.reply(embed=create_small_embed('Vous avez ajouté cette faction à la liste avec succès'))

async def addtruce2(ctx,faction,member):
	if not faction:
		await ctx.reply(embed=create_small_embed(":warning: Vous n'avez pas spécifié de faction !",discord.Color.red()))
		return
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Vous n'avez pas spécifié d'Ambassadeur !",discord.Color.red()))
		return
	with open('rela.json', 'r') as f:
		rela = json.load(f)
	rela["truce"][faction] = {member.id:[]}
	with open('rela.json', 'w') as f:
		json.dump(rela, f, indent=6)
	role = ctx.guild.get_role(790675785412640768)
	await member.add_roles(role)
	await edditally()
	await ctx.reply(embed=create_small_embed('Vous avez ajouté cette faction à la liste avec succès'))

async def addally2(ctx,faction,member):
	if not faction:
		await ctx.reply(embed=create_small_embed(":warning: Vous n'avez pas spécifié de faction !",discord.Color.red()))
		return
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Vous n'avez pas spécifié d'Ambassadeur !",discord.Color.red()))
		return
	with open('rela.json', 'r') as f:
		rela = json.load(f)
	rela["ally"][faction] = {member.id:[]}
	with open('rela.json', 'w') as f:
		json.dump(rela, f, indent=6)
	role = ctx.guild.get_role(790675785412640768)
	await member.add_roles(role)
	await edditally()
	await ctx.reply(embed=create_small_embed('Vous avez ajouté cette faction à la liste avec succès'))

async def endally2(ctx,faction):
	if not faction:
		await ctx.reply(embed=create_small_embed(":warning: Vous n'avez pas spécifié de faction !",discord.Color.red()))
		return
	with open('rela.json', 'r') as f:
		rela = json.load(f)
	for type in rela.items():
		for fac in type[1].items():
			if faction == fac[0]:
				typ = type[0]
				for id in fac[1].keys():
					memberid = id
	for personne in rela[typ][faction][memberid]:
		member = ctx.guild.get_member(int(personne))
		ally = ctx.guild.get_role(790675785412640768)
		await member.remove_roles(ally)
		await member.send(f'Notre alliance étant terminée votre grade {ally.mention} vous a été retiré')
	rela[typ].pop(faction)
	with open('rela.json', 'w') as f:
		json.dump(rela, f, indent=6)
	await edditally()
	await ctx.reply(embed=create_small_embed('Vous avez retiré cette faction de la liste avec succès'))

async def addmember2(ctx,member,faction):
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Vous n'avez pas spécifié de membre à ajouter !",discord.Color.red()))
		return
	with open('rela.json', 'r') as f:
		rela = json.load(f)
	for type in rela.items():
		for fac in type[1].items():
			if str(ctx.author.id) in fac[1].keys():
				faction = fac[0]
				typ = type[0]
	if not typ or not faction:
		await ctx.reply(embed=create_small_embed(":warning: Vous n'etes pas un Ambassadeur !",discord.Color.red()))
		return
	if member.id in rela[typ][faction][str(ctx.author.id)]:
		await ctx.reply('Cette personne est déjà dans notre base de donnée.')
	else:
		rela[typ][faction][str(ctx.author.id)].append(member.id)
	with open('rela.json', 'w') as f:
		json.dump(rela, f, indent=6)
	role = ctx.guild.get_role(790675785412640768)
	await member.add_roles(role)
	await ctx.reply(embed=create_small_embed(f'Vous avez ajouté {member.mention} à votre faction avec succès'))

async def removemember2(ctx,member,faction):
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Vous n'avez pas spécifié de membre à ajouter !",discord.Color.red()))
		return
	with open('rela.json', 'r') as f:
		rela = json.load(f)
	for type in rela.items():
		for fac in type[1].items():
			if str(ctx.author.id) in fac[1].keys():
				faction = fac[0]
				typ = type[0]
	if not typ or not faction:
		await ctx.reply(embed=create_small_embed(":warning: Vous n'etes pas un Ambassadeur !",discord.Color.red()))
		return
	if member.id in rela[typ][faction][str(ctx.author.id)]:
		rela[typ][faction][str(ctx.author.id)].remove(member.id)
	else:
		await ctx.reply("Cette personne n'est pas dans notre base de donnée.")
	with open('rela.json', 'w') as f:
		json.dump(rela, f, indent=6)
	role = ctx.guild.get_role(790675785412640768)
	await member.remove_roles(role)
	await ctx.reply(embed=create_small_embed(f'Vous avez enlevé {member.mention} de votre faction avec succès'))

async def askally2(ctx,faction):
	if not faction:
		await ctx.reply(embed=create_small_embed(":warning: Vous n'avez pas spécifié de faction !",discord.Color.red()))
		return
	with open('rela.json', 'r') as f:
		rela = json.load(f)
	member = None
	try:
		for memberid in rela["ally"][faction].keys():
			member = bot.get_user(int(memberid))
	except:
		pass
	try:
		for memberid in rela["truce"][faction].keys():
			member = bot.get_user(int(memberid))
	except:
		pass
	try:
		for memberid in rela["pna"][faction].keys():
			member = bot.get_user(int(memberid))
	except:
		pass
	if member == None:
		await ctx.reply(":warning: Vous n'etes pas en alliance ou avez spécifié la mauvaise faction !")
		return
	await member.send(f'{ctx.author.mention} est il de votre faction ?',view=IsAlly())
	await ctx.reply(embed=create_small_embed(f'Vous avez demandé à {member.mention} de rejoindre la {faction} avec succès'))

class IsAlly(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label='Oui', style=discord.ButtonStyle.green, custom_id='isallyo')
	async def isallyo(self, interaction: discord.Interaction, button: discord.ui.Button):
		guild = bot.get_guild(790367917812088864)
		member = guild.get_member(int(interaction.message.content[2:20]))
		if member == None:
			await interaction.response.send_message('Cette personne à quitté le discord')
			await interaction.message.delete()
			return
		with open('rela.json', 'r') as f:
			rela = json.load(f)
		for type in rela.items():
			for fac in type[1].items():
				if str(interaction.user.id) in fac[1].keys():
					faction = fac[0]
					typ = type[0]
		if member.id in rela[typ][faction][str(interaction.user.id)]:
			await interaction.user.send('Cette personne est déjà dans notre base de donnée.')
		else:
			rela[typ][faction][str(interaction.user.id)].append(member.id)
		role = guild.get_role(790675785412640768)
		await member.add_roles(role)
		await member.send(f'Vous avez été ajouté à la {faction}')
		with open('rela.json', 'w') as f:
			json.dump(rela, f, indent=6)
		await interaction.response.send_message(f'Vous avez ajouté {member.mention} avec succès')
		await interaction.message.delete()
	@discord.ui.button(label='Non', style=discord.ButtonStyle.red, custom_id='isallyn')
	async def isallyn(self, interaction: discord.Interaction, button: discord.ui.Button):
		guild = bot.get_guild(790367917812088864)
		member = guild.get_member(int(interaction.message.content[2:20]))
		await member.send("Votre demande de grade \"ally\" n'a pas pu aboutir car votre chef n'a pas confirmé que vous etiez de la faction")
		await interaction.response.send_message(f"{member.mention} n'a pas été ajouté")
		await interaction.message.delete()

async def edditally():
	channel = bot.get_channel(797862044765388830)
	message = await channel.fetch_message(967858924722196500)
	with open('rela.json', 'r') as f:
		rela = json.load(f)
	ally = ''
	truces = ''
	pna = ''
	for element in rela['ally'].items():
		ally += f"\n{element[0]} - <@{''.join(list(element[1].keys()))}>"
	if ally == '':
		ally = "\nNous n'avons aucune alliance pour l'instant"
	for element in rela['truce'].items():
		truces += f"\n{element[0]} - <@{''.join(list(element[1].keys()))}>"
	if truces == '':
		truces = "\nNous n'avons aucune truces pour l'instant"
	for element in rela['pna'].items():
		pna += f"\n{element[0]} - <@{''.join(list(element[1].keys()))}>"
	if pna == '':
		pna = "\nNous n'avons aucun pacte de non agression pour l'instant"
	await message.edit(embed=create_embed('Relations Factions',
										f'Voici ici la liste de toutes nos relations :\n\n**Ally :**{ally}\n\n**Truces :**{truces}\n\n**Pacte de non agression :**{pna}'))
