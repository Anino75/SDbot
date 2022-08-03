import discord
"""async def candids():
	print('test')
	mydb = mysql.connector.connect(
		host="web49.lws-hosting.com",
		user="cp1873034p22_blbl",
		password="3Do4Ysz6D2",
		database="cp1873034p22_Candid"
	)
	print('ok')
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM Candidatures")
	myresult = mycursor.fetchall()
	print(myresult)
	with open('candid.json', 'r') as f:
		candids = json.load(f)
	if (len(myresult) - candids["nb"]) != 0:
		if myresult[-i-1][0] in candids["ban"]:
			pass
		else:
			guild = bot.get_guild(790367917812088864)
			rep = guild.get_channel(793804078366851092)
			for i in range(len(myresult) - candids["nb"]):
				if myresult[-i-1][0] in candids["id"].keys() and int(str(datetime.now())[5:7]) <= int(str(candids["id"][myresult[-i-1][0]][5:7])) and int(str(datetime.now())[8:10]) <= int(str(candids["id"][myresult[-i-1][0]][8:10])):
					await rep.send(embed=create_small_embed(f"<@{myresult[-i-1][0]}> à tenté de faire une double candidature"))
				else:
					try:
						guild = bot.get_guild(790367917812088864)
						member = guild.get_member(myresult[-i-1][0])
						role = guild.get_role(986686680146772038)
						await member.add_roles(role)
						await member.edit(nick=f'[CE] {myresult[-i-1][1]}')
						message = discord.embed(title=f'Candidature {len(candids[id.keys()])}',description=f'**Pseudo discord :**\n<@{myresult[-i-1][0]}>')
						await rep.send(embed=message,view=candid())
					except:
						try:
							user = bot.get_user(myresult[-i-1][0])
							await user.send("Vous n'avez pas rejoint le serveur discord et votre candidature n'a donc pas pu être traitée ! Veuillez rejoindre : https://discord.gg/D9tTGvt7az et recommencer")
						except:
							pass
		candids["nb"] += i
		with open('candid.json', 'w') as f:
			json.dump(candids, f, indent=6)
	asyncio.sleep(60)"""
			

class candid(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label='Accepter', style=discord.ButtonStyle.green, custom_id='passer')
	async def accept(self,interaction: discord.Interaction, button: discord.ui.Button):
		print(interaction.message.content[24:42])
		guild = interaction.guild
		for embed in interaction.message.embeds:
			member = bot.get_user(int(embed.description[24:42]))
		with open('Interview.json', 'r') as f:
			interviews = json.load(f)
		ead = guild.get_channel(790706486426861578)
		for type in interviews.items():
			for personne in type[1].keys():
				if str(member.id) == personne:
					await interaction.response.send_message(embed=create_small_embed(":warning: Cet utilisateur a deja été accepté !", discord.Color.red()))
					return
		_embed = discord.Embed(title = "Recrutements",
				description ="Salut déjà toutes mes Félicitations, ta candidature SweetDream a été accéptée !\nMaintenant tu vas devoir passer un entretien oral. Pour "
				f"le passer il faudra aller dans le {ead.mention} et ping un recruteur. Tu auras une semaine pour venir dans passer ton entretien, si tu n'es pas "
				"disponible dans ce delai le bot t'enverra un message pour te demander la raison, et nous verrons si elle est acceptable.\nCordialement,\nLe Staff Recrutement SweetDream."
				)
		interviews['Dates'][member.id] = str(datetime.utcnow() + timedelta(days=7))
		await member.send(embed=_embed)
		role = guild.get_role(790675784901197905)
		await member.add_roles(role, reason=f'Fait par {str(interaction.user)[:16]}')
		with open('Interview.json', 'w') as f:
			json.dump(interviews, f, indent=6)
		log = bot.get_channel(831615469134938112)
		await member.edit(nick=f'[CA] {member.nick[5:]}')
		await interaction.response.send_message(embed=create_small_embed('Le message a bien été envoyé à' + member.mention))
		await log.send(embed=create_small_embed(interaction.user.mention + ' à accepté ' + member.mention))
		await interaction.message.edit(view=None)
	@discord.ui.button(label='Refuser', style=discord.ButtonStyle.red, custom_id='refuser')
	async def refuse(self,interaction: discord.Interaction, button: discord.ui.Button):
		member = bot.get_user(int(interaction.message.content[32:50]))
		channel = bot.get_channel(811651953003855882)
		def check(m):
			return m.author == member and m.channel == channel
		await channel.send(f'{interaction.user.mention} pourquoi voulez vous refuser {member.mention} ?')
		msg = await bot.wait_for('message', timeout=None,check=check)
		_embed = discord.Embed(title = "Recrutements",
							description ="Bonjour, malheureusement ta candidature pour rejoindre la SweetDream n'a pas "
										 f"été acceptée pour la raison suivante : {msg.content}.\nTu pourras retenter ta chance dans 2 semaines.\nCordialement,\nLe Staff Recrutement SweetDream"
							)
		await member.send(embed=_embed)
		log = bot.get_channel(831615469134938112)
		ban = bot.get_channel(801163722650419200)
		await member.edit(nick='')
		await interaction.response.send_message(embed=create_small_embed('Le message a bien été envoyé à' + member.mention))
		await log.send(embed=create_small_embed(interaction.user.mention + ' à éxécuté la commande refuse pour ' + member.mention))
		await ban.send(embed=create_small_embed(member.mention + 'est banni.e pendant deux semaines car sa candidature à été refusée',discord.Color.red()))
		await interaction.message.delete()

async def refuse2(ctx, member, raison):
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !",discord.Color.red()))
		return
	_embed = discord.Embed(title = "Recrutements",
							description ="Bonjour, malheureusement ta candidature pour rejoindre la SweetDream n'a pas "
										 "été acceptée pour la raison suivante "+(raison)+".\nTu pourras retenter ta "
										"chance dans 2 semaines. \nCordialement,\nLe Staff Recrutement SweetDream"
							)
	await member.send(embed=_embed)
	log = bot.get_channel(831615469134938112)
	ban = bot.get_channel(801163722650419200)
	await member.edit(nick='')
	await ctx.reply(embed=create_small_embed('Le message a bien été envoyé à' + member.mention))
	await log.send(embed=create_small_embed(ctx.author.mention + ' à éxécuté la commande refuse pour ' + member.mention+" Pour la raison suivante : "+raison))
	await ban.send(embed=create_small_embed(member.mention + 'est banni.e pendant deux semaines car sa candidature à été refusée Pour la raison suivante : '+raison,discord.Color.red()))

async def accept2(ctx, member):
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !", discord.Color.red()))
		return
	with open('Interview.json', 'r') as f:
		interviews = json.load(f)
	ead = ctx.guild.get_channel(790706486426861578)
	for type in interviews.items():
		for personne in type[1].keys():
			if str(member.id) == personne:
				await ctx.reply(embed=create_small_embed(":warning: Cet utilisateur a deja été accepté !", discord.Color.red()))
				return
	guild = ctx.guild
	_embed = discord.Embed(title = "Recrutements",
							description ="Salut déjà toutes mes Félicitations, ta candidature SweetDream a été accéptée !\nMaintenant tu vas devoir passer un entretien oral. Pour "
							f"le passer il faudra aller dans le {ead.mention} et ping un recruteur. Tu auras deux semaine pour venir dans passer ton entretien, si tu n'es pas "
							"disponible dans ce delai le bot t'enverra un message pour te demander la raison, et nous verrons si elle est acceptable.\nCordialement,\nLe Staff Recrutement SweetDream."
							)
	interviews['Dates'][member.id] = str(datetime.utcnow() + timedelta(days=14))
	try:
		await member.edit(nick=f'[CA] {member.nick[5:]}')
	except:
		await member.edit(nick=f'[CA] {member.name}')
	try:
		await member.send(embed=_embed)
	except:
		await ctx.reply(f"Votre message n'a pas pu etre envoyé car {member.mention} à fermé ses mp")
	role = guild.get_role(790675784901197905)
	await member.add_roles(role, reason=f'Fait par {str(ctx.author)[:16]}')
	with open('Interview.json', 'w') as f:
		json.dump(interviews, f, indent=6)
	log = bot.get_channel(831615469134938112)
	await ctx.reply(embed=create_small_embed('Le message a bien été envoyé à' + member.mention))
	await log.send(embed=create_small_embed(ctx.author.mention + ' à éxécuté la commande accept pour ' + member.mention))

async def addtime2(ctx, member, time_string):
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !", discord.Color.red()))
		return
	with open('Interview.json', 'r') as f:
		interviews = json.load(f)
	try:
		time = int(time_string)
	except:
		time = 7
	for type in interviews.items():
		for personne in type[1].keys():
			if str(member.id) == personne:
				a = str(member.id)
				b = type[0]
	try:
		interviews[b].pop(a)
	except:
		await ctx.reply(embed=create_small_embed(":warning: Cet utilisateur n'est pas en attente d'entretien !"))
		return
	interviews['Dates'][member.id] = str((datetime.utcnow() + timedelta(minutes=0, days=time)))
	log = bot.get_channel(831615469134938112)
	with open('Interview.json', 'w') as f:
		json.dump(interviews, f, indent=6)
	_embed = discord.Embed(title="Recrutements",
						   description=f"Bonjour,\nTa réponse à ta demande d'ajout de temps a été acceptée et tu as {time} jours en plus pour passer ton entretien oral.\n"
						   "Cordialement,\nLe Staff Recrutement SweetDream."
						   )
	await member.send(embed=_embed)
	await ctx.reply(embed=create_small_embed('Le message a bien été envoyé à' + member.mention))
	await log.send(embed=create_small_embed(ctx.author.mention + ' à éxécuté la commande addtime pour ' + member.mention))

class testview(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label='Accepter', style=discord.ButtonStyle.green, custom_id='pass')
	async def accept(self,interaction: discord.Interaction, button: discord.ui.Button):
		member = bot.get_user(int(interaction.message.content[2:20]))
		with open('Interview.json', 'r') as f:
			interviews = json.load(f)
		_embed = discord.Embed(title = "Recrutements",
							description ="Bravo, tu es désormais un.e membre officiel de la faction ! Tu as accès aux "
										 "salons de faction. N'hésites pas a être actif.ve en vocal et en écrit pour "
										 "monter en grade et avoir accès a plus de bases ;-)"
							)
		with open('Interview.json', 'w') as f:
			json.dump(interviews, f, indent=6)
		await member.send(embed=_embed)
		member = interaction.guild.get_member(member.id)
		role = interaction.guild.get_role(791066206109958204)
		await member.remove_roles(role, reason=f'Fait par {str(interaction.user)[:16]}')
		role1 = interaction.guild.get_role(791066207418712094)
		await member.add_roles(role1, reason=f'Fait par {str(interaction.user)[:16]}')
		log = bot.get_channel(831615469134938112)
		await interaction.response.send_message(embed=create_small_embed('Le message a bien été envoyé à' + member.mention),ephemeral=True)
		await log.send(embed=create_small_embed(interaction.user.mention + ' à éxécuté la accépté ' + member.mention))
		await interaction.message.delete()
	@discord.ui.button(label='Refuser', style=discord.ButtonStyle.red, custom_id='refuse')
	async def refuse(self,interaction: discord.Interaction, button: discord.ui.Button):
		member = bot.get_user(int(interaction.message.content[2:20]))
		with open('Interview.json', 'r') as f:
			interviews = json.load(f)
		_embed = discord.Embed(title="Recrutements",
						   description="Bonjour,\nSuite à ta periode de test tu n'as malheureusement pas été retenu... Tu pourras"
										" retenter ta chance en faisant une nouvelle candidature écrite dans 2 semaines.\n"
										"Cordialement,\nle Staff Recrutement SweetDream.")
		with open('Interview.json', 'w') as f:
			json.dump(interviews, f, indent=6)
		log = bot.get_channel(831615469134938112)
		ban = bot.get_channel(801163722650419200)
		try:
			await member.send(embed=_embed)
			await interaction.response.send_message(embed=create_small_embed('Le message a bien été envoyé à ' + member.mention),ephemeral=True)
			member = interaction.guild.get_member(member.id)
			role = interaction.guild.get_role(790675784901197905)
			await member.remove_roles(role, reason=f'Fait par {str(interaction.user)[:16]}')
			role1 = interaction.guild.get_role(791066206109958204)
			await member.remove_roles(role1, reason=f'Fait par {str(interaction.user)[:16]}')
		except:
			await interaction.response.send_message(embed=create_small_embed("La commande a été prise en compte mais le message n'a pas pu être envoyé car la personne a quitté le serveur"),ephemeral=True)
		await log.send(embed=create_small_embed(interaction.user.mention + ' à éxécuté la commande kickphases pour ' + member.mention))
		await ban.send(embed=create_small_embed(member.mention + ' est banni.e pendant deux semaines car iel à été kick des phases ',discord.Color.red()))
		await interaction.message.delete()

async def oralyes2(ctx, member):
	with open('Interview.json', 'r') as f:
		interviews = json.load(f)
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !", discord.Color.red()))
		return
	_embed = discord.Embed(title = "Recrutements",
							description ="Félicitation, tu viens de passer ton entretien oral et tu as réussi !\nTu es désormais en test dans la faction. Pendant cette periode de "
							"test nous allons t'évaluer sur ton activité (en jeu, en vocal, écrit) et sur ta capacité à farmer.\nAfin de verifier ton activité tu devra farmer un maximum de points parmis le catalogue suivant :\n**Farmer :**\n- Graines de paladium -> 25 points\n- Graine d'endium -> 500 points\n- Bouteilles de farmer (1000xp) -> 100 points\n\n**Hunter :**\n- Spawner T4 witch -> 1.000.000 points\n- Autre spawner T4 -> 250.000 points\n- Empty spawner -> 6.500 points\n- Broken spawners -> 4.000 points\n\n**Miner :**\n- Findium -> 60 points\n- Minerais d'améthyste -> 35 points\n- Minerais de titane -> 35 points\n- Minerais de paladium -> 80 points\n- Cobblebreaker -> 100 points\n- Cobblestone -> 0.125 points\n\n**Alchimiste :**\n- Lightning potion -> 2.000 points (30 max par personne)\n- Extractor -> 200 points\n- Fleurs -> 50 points/stack\n- Harpagophytum -> 1.000 points\n\n**BC :**\n- Obsidienne Normale -> 12.5 points\n- Poisonned Obsidian -> 15 points\n- Boom Obsidian -> 25 points\n- Mega Boom Obsidian -> 300 points\n- Big obsidian -> 200 points\n\n**Ressources :**\n- Lingot de titane : 17 points\n- Lingot d'amethyste : 17 points\n- 1$ -> 0,2 point\n- lingot de pala : 40 points\n- Nugget en endium : 75.000 points\n\nSi nous considérons que tu es suffisament actif pour entrer tu pourras nous montrer tout ce que tu as farmé. Si c'est suffisant tu pourras nous le donner et entrer dirrectement dans la faction sinon tu n'auras plus qu'une semaine pour farmer un nombre d'une ressource choisie par toi et les recruteurs' Nous t'invitons donc rester présent et actif.\nEn cas de problèmes tu peux"
							" envoyer un message a un recruteur afin de signaler une absence.\nCordialement,\nLe Staff Recrutement SweetDream")
	for type in interviews.items():
		for personne in type[1].keys():
			if str(member.id) == personne:
				a = str(member.id)
				b = type[0]
	try:
		interviews[b].pop(a)
	except:
		await ctx.reply(embed=create_small_embed(":warning: Cet utilisateur n'est pas en attente d'entretien !"))
		return
	interviews["ET"][member.id] = str((datetime.utcnow() + timedelta(days=30)))
	with open('Interview.json', 'w') as f:
		json.dump(interviews, f, indent=6)
	with open('phases.json', 'r') as f:
		phases = json.load(f)
	phases["A faire"][member.id] = str(datetime.now())
	with open('phases.json', 'w') as f:
		json.dump(phases, f, indent=6)
	try:
		await member.edit(nick=f'[ET] {member.nick[5:]}')
	except:
		await member.edit(nick=f'[ET] {member.name}')
	role = ctx.guild.get_role(790675784901197905)
	role1 = ctx.guild.get_role(791066206109958204)
	await member.remove_roles(role, reason=f'Fait par {str(ctx.author)[:16]}')
	await member.add_roles(role1, reason=f'Fait par {str(ctx.author)[:16]}')
	log = bot.get_channel(831615469134938112)
	await member.send(embed=_embed)
	await ctx.reply(embed=create_small_embed('Le message a bien été envoyé à' + member.mention))
	await log.send(embed=create_small_embed(ctx.author.mention + ' à éxécuté la commande oralyes pour ' + member.mention))

async def oralno2(ctx, member):
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !", discord.Color.red()))
		return
	with open('Interview.json', 'r') as f:
		interviews = json.load(f)
	guild = ctx.guild
	_embed = discord.Embed(title = "Recrutements",
							description ="Bonjour,\nMalheureusement ton entretien oral n'a pas été accepté mais tu "
										 "pourras refaire une candidature écrite dans 2 semaines. \nCordialement,\n"
										 "Le staff Recrutement SweetDream."
							)
	role = guild.get_role(790675784901197905)
	await member.remove_roles(role, reason=f'Fait par {str(ctx.author)[:16]}')
	for type in interviews.items():
		for personne in type[1].keys():
			if str(member.id) == personne:
				a = str(member.id)
				b = type[0]
	try:
		interviews[b].pop(a)
	except:
		await ctx.reply(embed=create_small_embed(":warning: Cet utilisateur n'est pas en attente d'entretien !"))
		return
	with open('Interview.json', 'w') as f:
		json.dump(interviews, f, indent=6)
	await member.edit(nick=f'')
	await member.send(embed=_embed)
	log = bot.get_channel(831615469134938112)
	ban = bot.get_channel(801163722650419200)
	await ctx.reply(embed=create_small_embed('Le message a bien été envoyé à' + member.mention))
	await log.send(embed=create_small_embed(ctx.author.mention + ' à éxécuté la commande oralno pour ' + member.mention))
	await ban.send(embed=create_small_embed(member.mention + 'est banni pendant deux semaines car iel à été refusé.e en entretien',discord.Color.red()))

async def finphases2(ctx, member,rendu):
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !", discord.Color.red()))
		return
	with open('Interview.json', 'r') as f:
		interviews = json.load(f)
	guild = ctx.guild
	_embed = discord.Embed(title = "Recrutements",
							description ="Bravo, tu es désormais un.e membre officiel de la faction ! Tu as accès aux "
										 "salons de faction. N'hésites pas a être actif.ve en vocal et en écrit pour "
										 "monter en grade et avoir accès a plus de bases ;-)"
							)
	for type in interviews.items():
		for personne in type[1].keys():
			if str(member.id) == personne:
				a = str(member.id)
				b = type[0]
	try:
		interviews[b].pop(a)
	except:
		await ctx.reply(embed=create_small_embed(":warning: Cet utilisateur n'est pas en attente d'entretien ou a fini sa limite de temps"))
	with open('Interview.json', 'w') as f:
			json.dump(interviews, f, indent=6)
	with open('phases.json', 'r') as f:
		phases = json.load(f)
	phases["A faire"].pop[str(member.id)]
	phases["Fait"][member.id] = [str(datetime.now()),rendu]
	with open('phases.json', 'w') as f:
		json.dump(phases, f, indent=6)
	await member.send(embed=_embed)
	try:
		await member.edit(nick=f'[??] {member.nick[5:]}')
	except:
		await member.edit(nick=f'[??] {member.name}')
	role = guild.get_role(791066206109958204)
	await member.remove_roles(role, reason=f'Fait par {str(ctx.author)[:16]}')
	role1 = guild.get_role(791066207418712094)
	await member.add_roles(role1, reason=f'Fait par {str(ctx.author)[:16]}')
	log = bot.get_channel(831615469134938112)
	await ctx.reply(embed=create_small_embed('Le message a bien été envoyé à' + member.mention))
	await log.send(embed=create_small_embed(ctx.author.mention + ' à éxécuté la commande finphases pour ' + member.mention))

async def kickphases2(ctx, member, raison):
	with open('Interview.json', 'r') as f:
		interviews = json.load(f)
	guild = ctx.guild
	_embed = discord.Embed(title="Recrutements",
						   description="Bonjour,\nTu as été kick des phases pour la raison suivante : "+raison+" Tu pourras"
										" retenter ta chance en faisant une nouvelle candidature écrite dans 2 semaines.\n"
										"Cordialement,\nle Staff Recrutement SweetDream.")
	for type in interviews.items():
		for personne in type[1].keys():
			if str(member.id) == personne:
				a = str(member.id)
				b = type[0]
	try:
		interviews[b].pop(a)
	except:
		await ctx.reply(embed=create_small_embed(":warning: Cet utilisateur n'est pas en attente d'entretien ou a fini sa limite de temps"))
	with open('Interview.json', 'w') as f:
		json.dump(interviews, f, indent=6)
	log = bot.get_channel(831615469134938112)
	ban = bot.get_channel(801163722650419200)
	try:
		await member.send(embed=_embed)
		await ctx.reply(embed=create_small_embed('Le message a bien été envoyé à ' + member.mention))
		member = guild.get_member(member.id)
		role = guild.get_role(790675784901197905)
		await member.remove_roles(role, reason=f'Fait par {str(ctx.author)[:16]}')
		role1 = guild.get_role(791066206109958204)
		await member.remove_roles(role1, reason=f'Fait par {str(ctx.author)[:16]}')
	except:
		await ctx.reply(embed=create_small_embed("La commande a été prise en compte mais le message n'a pas pu être envoyé car la personne a quitté le serveur"))
	await log.send(embed=create_small_embed(ctx.author.mention + ' à éxécuté la commande kickphases pour ' + member.mention))
	await ban.send(embed=create_small_embed(member.mention + ' est banni.e pendant deux semaines car iel à été kick des phases ',discord.Color.red()))
