import discord

async def creercompte2(ctx):
	with open('economie.json', 'r') as f:
		Eco = json.load(f)
	try:
		await ctx.reply(embed=create_small_embed(":warning: Vous avez déjà ouvert un compte avec "+str(Eco["Comptes"][str(ctx.author.id)])+"$ dessus !",discord.Color.red()))
	except:
		await compte(ctx.author)
		await ctx.reply("Votre compte à été crée")

async def compte(member):
	with open('economie.json', 'r') as f:
		Eco = json.load(f)
	try:
		int(Eco["Comptes"][str(member.id)])
	except:
		Eco["Comptes"][str(member.id)] = 0
		with open('economie.json', 'w') as f:
			json.dump(Eco, f, indent=6)
		await member.send("Votre compte à été crée")
		log = bot.get_channel(959867855350931486)
		await log.send(embed=create_small_embed(member.mention + ' à ouvert son compte'))

async def money2(ctx,member):
	with open('economie.json', 'r') as f:
		Eco = json.load(f)
	if not member:
		await compte(ctx.author)
		await ctx.reply("Vous avez actuelement "+str(Eco["Comptes"][str(ctx.author.id)])+"$ sur votre compte")
		return
	if 790675782569164820 not in [x.id for x in ctx.author.roles] and 821787385636585513 not in [x.id for x in
																										 ctx.author.roles]:
		await ctx.reply(embed=create_small_embed(":warning: Seuls les HG peuvent voir l'argent des autres !", discord.Color.red()))
		return
	await compte(member)
	await ctx.reply(member.mention + " à actuelement " + str(Eco["Comptes"][str(member.id)]) + "$ sur son compte")

async def adminaddmoney2(ctx,member,money):
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !", discord.Color.red()))
		return
	await compte(member)
	with open('economie.json', 'r') as f:
		Eco = json.load(f)
	Eco["Comptes"][str(member.id)] += int(money)
	with open('economie.json', 'w') as f:
		json.dump(Eco, f, indent=6)
	await member.send(embed=create_small_embed(ctx.author.mention+" Vous a crédité de "+str(money)+"$"))
	await ctx.reply(embed=create_small_embed("L'argent à bien été crédité"))
	log = bot.get_channel(959867855350931486)
	await log.send(embed=create_small_embed(member.mention + ' à été crédité de '+str(money)+"$ par "+ctx.author.mention))

async def adminremovemoney2(ctx,member,money):
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !", discord.Color.red()))
		return
	await compte(member)
	with open('economie.json', 'r') as f:
		Eco = json.load(f)
	Eco["Comptes"][str(member.id)] -= int(money)
	with open('economie.json', 'w') as f:
		json.dump(Eco, f, indent=6)
	await member.send(embed=create_small_embed(ctx.author.mention+" Vous a privé de "+str(money)+"$"))
	await ctx.reply(embed=create_small_embed("L'argent à bien été retiré"))
	log = bot.get_channel(959867855350931486)
	await log.send(embed=create_small_embed(member.mention + ' à été privé de '+str(money)+"$ par "+ctx.author.mention))

async def pay2(ctx,member,money):
	if not member:
		await ctx.reply(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !", discord.Color.red()))
		return
	await compte(ctx.author)
	with open('economie.json', 'r') as f:
		Eco = json.load(f)
	if Eco["Comptes"][str(ctx.author.id)] < money:
		await ctx.reply(embed=create_small_embed(":warning: Vous n'avez pas assez d'argent !", discord.Color.red()))
		return
	await compte(member)
	Eco["Comptes"][str(ctx.author.id)] -= int(money)
	Eco["Comptes"][str(member.id)] += int(money)
	with open('economie.json', 'w') as f:
		json.dump(Eco, f, indent=6)
	await member.send(embed=create_small_embed(ctx.author.mention+" Vous a donné "+str(money)+"$"))
	await ctx.author.send(embed=create_small_embed("Vous avez donné " + str(money) + "$ à "+member.mention))
	await ctx.reply(embed=create_small_embed("Le virement à bien été effectué"))
	log = bot.get_channel(959867855350931486)
	await log.send(embed=create_small_embed(ctx.author.mention+" à donné "+str(money)+"$ à "+member.mention))

class Methode(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label='Payer par solde', style=discord.ButtonStyle.green, custom_id='solde')
	async def solde(self,interaction: discord.Interaction, button: discord.ui.Button):
		await compte(interaction.user)
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		if str(interaction.user.id) != Eco["commande"][interaction.channel.name[-4:]][0]:
			await interaction.response.send_message(":warning: Vous n'êtes pas l'auteur de ce ticket !", ephemeral=True)
			return
		if int(Eco["commande"][interaction.channel.name[-4:]][2]) > Eco["Comptes"][str(interaction.user.id)]:
			await interaction.response.send_message(":warning: Vous n'avez pas assez d'argent ! Veuillez payer en jeu !",ephemeral=True)
			await interaction.channel.send("Merci encore pour votre commande. Veuillez patienter un vendeur va prendre en charge votre commande.")
			Eco["commande"][interaction.channel.name[-4:]].append("\n\n**A payer**")
		else:
			Eco["Comptes"][str(interaction.user.id)] -= Eco["commande"][interaction.channel.name[-4:]][2]
			await interaction.response.send_message("Très bien, merci encore pour votre commande. Veuillez patienter un vendeur va prendre en charge votre commande.")
			Eco["commande"][interaction.channel.name[-4:]].append("\n\n**Déjà payée**")
		with open('economie.json', 'w') as f:
			json.dump(Eco, f, indent=6)
		await interaction.message.delete()
		await commandefinie(interaction.guild,interaction.channel)
	@discord.ui.button(label='Payer en jeu', style=discord.ButtonStyle.red, custom_id='jeu')
	async def jeu(self, interaction: discord.Interaction, button: discord.ui.Button):
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		Eco["commande"][interaction.channel.name[-4:]].append("\n\n**A payer**")
		with open('economie.json', 'w') as f:
			json.dump(Eco, f, indent=6)
		await interaction.response.send_message("Très bien, merci encore pour votre commande. Veuillez patienter un vendeur va prendre en charge votre commande.")
		await interaction.message.delete()
		await commandefinie(interaction.guild,interaction.channel)

class Nombre(discord.ui.Select):
	def __init__(self):
		options = [
			discord.SelectOption(label='1'),
			discord.SelectOption(label='2'),
			discord.SelectOption(label='3'),
			discord.SelectOption(label='4'),
			discord.SelectOption(label='5'),
			discord.SelectOption(label='Plus que 5'),
		]
		super().__init__(placeholder='Combien en voulez-vous ?', min_values=1, max_values=1, options=options, custom_id='Nombre')
	async def callback(self, interaction: discord.Interaction):
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		if str(interaction.user.id) != Eco["commande"][interaction.channel.name[-4:]][0]:
			await interaction.response.send_message(":warning: Vous n'êtes pas l'auteur de ce ticket !",ephemeral=True)
			return
		await interaction.channel.purge()
		if self.values[0] == 'Plus que 5':
			await interaction.channel.send("Veuillez indiquer combien d'Items vous souhaitez prendre")
			nb = await chiffrecommande(interaction.user,interaction.channel)
		else:
			nb = int(self.values[0])
		Eco["commande"][interaction.channel.name[-4:]][2] = str(int(Eco["commande"][interaction.channel.name[-4:]][2])*nb)
		Eco["commande"][interaction.channel.name[-4:]].append(str(nb))
		with open('economie.json', 'w') as f:
			json.dump(Eco, f, indent=6)
		await interaction.channel.send("Souhaitez vous payer en jeu ou avez votre solde ?",view=Methode())

async def chiffrecommande(member,channel):
	def check(m):
		return m.author == member and m.channel == channel
	msg = await bot.wait_for('message', timeout=None,check=check)
	try:
		return int(msg.content)
	except:
		await channel.send(':warning: Veuillez indiquer un chiffre')
		return await chiffrecommande(member,channel)

class NombreView(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
		self.add_item(Nombre())

async def commandefinie(guild,channel):
	with open('economie.json', 'r') as f:
		Eco = json.load(f)
	acheteur = bot.get_user(int(Eco["commande"][channel.name[-4:]][0]))
	embed_=discord.Embed(
		title = "Commande "+channel.name[-4:],
		description = "**Acheteur :**\n"+acheteur.mention+"\n\n**Item :**\n"+Eco["commande"][channel.name[-4:]][1]+"\n\n**Quantité :**\n"+Eco["commande"][channel.name[-4:]][3]+"\n\n**Prix :**\n"+Eco["commande"][channel.name[-4:]][2]+Eco["commande"][channel.name[-4:]][4]+"\n\n**Pour prendre la commande, `*claim` dans le **"+channel.mention
	)
	with open('economie.json', 'w') as f:
		json.dump(Eco, f, indent=6)
	AP = guild.get_channel(960113232398401586)
	vendeur = guild.get_role(960180290683293766)
	await AP.send(vendeur.mention,embed=embed_)
	await channel.send(embed=embed_)

class PvP(discord.ui.Select):
	def __init__(self):
		options = [
			discord.SelectOption(label='Casque P4U3',description='5.000$/u',emoji="<:pala_helmet:823931428109680640>"),
			discord.SelectOption(label='Plastron P4U3',description='6.000$/u',emoji="<:pala_chest:823931435781324841>"),
			discord.SelectOption(label='Pantalon P4U3',description='6.000$/u',emoji="<:pala_leggings:823931446032465962>"),
		]
		super().__init__(placeholder='Quel item voulez vous commander ?', min_values=1, max_values=1, options=options, custom_id='PvP')
	async def callback(self, interaction: discord.Interaction):
		prix = {'Casque P4U3':5000,'Plastron P4U3':6000,'Pantalon P4U3':6000}
		guild = bot.get_guild(790367917812088864)
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		try:
			if Eco["Auteurs"][str(interaction.user.id)] >= 3:
				await interaction.response.send_message(":warning: Vous ne pouvez pas faire plus de 3 commandes en meme temps !",ephemeral=True)
				return
		except:
			pass
		for x in Eco["commande"].items():
			if x[1][0] == str(interaction.user.id) and len(x[1]) < 5:
				await interaction.response.send_message("Veuillez finir votre commande avant d'en rouvrir une autre",ephemeral=True)
				return
		Eco["commande"][Eco["tickets"]] = [str(interaction.user.id),self.values[0],prix[self.values[0]]]
		try:
			Eco["Auteurs"][str(interaction.user.id)] += 1
		except:
			Eco["Auteurs"][str(interaction.user.id)] = 1
		vendeur = guild.get_role(960180290683293766)
		comm = await interaction.guild.create_text_channel(name="Commande " + Eco["tickets"],
													overwrites={guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False, ),
															   interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True, ),
														   vendeur:discord.PermissionOverwrite(read_messages=True, send_messages=True, )},
														   category=guild.get_channel(819574162686738473))
		Eco["tickets"]  = (4-len(str(int(Eco["tickets"])+1)))*"0"+str(int(Eco["tickets"])+1)
		with open('economie.json', 'w') as f:
			json.dump(Eco, f, indent=6)
		await comm.send(interaction.user.mention+", merci d'avoir commandé l'item "+self.values[0]+" chez nous.",
						view=NombreView())
		await interaction.response.send_message("Vous avez crée le channel "+comm.mention,ephemeral=True)

class PvPView(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
		self.add_item(PvP())

async def claim2(ctx):
	try:
		int(ctx.channel.name[-4:])
	except:
		await ctx.reply(embed=create_small_embed(":warning: Cette commande ne peut etre utilisée que dans une commande !", discord.Color.red()))
		return
	await compte(ctx.author)
	vendeur = ctx.guild.get_role(960180290683293766)
	await ctx.channel.set_permissions(ctx.author,read_messages=True, send_messages=True)
	await ctx.channel.set_permissions(vendeur,overwrite= None)
	await ctx.reply("Vous avez bien pris en charge cette commande")

async def livre2(ctx):
	if ctx.channel.name[:7] != 'commande':
		await ctx.reply(embed=create_small_embed(":warning: Cette commande ne peut etre utilisée que dans une commande !", discord.Color.red()))
		return
	with open('economie.json', 'r') as f:
		Eco = json.load(f)
	transcript = await chat_exporter.export(ctx.channel)
	transcript_file = discord.File(
		io.BytesIO(transcript.encode()),
		filename=f"transcript-{ctx.channel.name}.html",
	)
	if Eco["commande"][ctx.channel.name[-4:]][4] == "\n\n**Déjà payée**":
		Eco["Comptes"][str(ctx.author.id)] += Eco["commande"][ctx.channel.name[-4:]][2]
		await ctx.author.send("Vous avez été payé")
	Eco["commande"].pop([ctx.channel.name[-4:]][4])
	Eco['Auteurs'][Eco["commande"][ctx.channel.name[-4:]][0]] -= 1
	log = bot.get_channel(819580672310116356)
	with open('economie.json', 'w') as f:
		json.dump(Eco, f, indent=6)
	await log.send(file=transcript_file)
	await ctx.channel.delete()

class rouletteruss(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label='Jouer à la Roulette Russe', style=discord.ButtonStyle.green, custom_id='debutroulette')
	async def Roullette(self, interaction: discord.Interaction, button: discord.ui.Button):
		await compte(interaction.user)
		with open('economie.json','r') as f:
			Eco = json.load(f)
		try:
			Eco["Mises"][str(interaction.user.id)]
			await interaction.response.send_message(':warning: Vous avez déjà un jeu ouvert !',ephemeral=True)
			return
		except:
			pass
		jeu = bot.get_channel(961597988613025812)
		await interaction.response.send_message("Vous avez une partie en cours dans le channel "+jeu.mention,ephemeral=True)
		await jeu.send(interaction.user.mention+' Combien voulez-vous miser ?')
		def check(m):
			return m.author == interaction.user and m.channel == jeu
		mise = await bot.wait_for('message', timeout=None, check=check)
		try:
			mise = int(mise.content)
		except:
			jeu.send(":warning: Ceci n'est pas un chiffre, veuillez recommencer avec un chiffre")
			return
		if Eco["Comptes"][str(interaction.user.id)] < mise:
			await jeu.send(":warning: Vous n'avez pas assez d'argent pour miser ca !")
			return
		Eco["Comptes"][str(interaction.user.id)] -= mise
		Eco["Mises"][str(interaction.user.id)] = [0,mise]
		await jeu.send('Confirmez vous votre partie avec une mise de '+str(mise)+' ?',view=gains())
		with open('economie.json', 'w') as f:
			json.dump(Eco, f, indent=6)

async def rouletterusse2(ctx,mise):
	await compte(ctx.author)
	with open('economie.json','r') as f:
		Eco = json.load(f)
	try:
		Eco["Mises"][str(ctx.author.id)]
		await ctx.reply(':warning: Vous avez déjà un jeu ouvert, si vous en avez encore besoin le voici',view=gains())
		return
	except:
		pass
	jeu = bot.get_channel(961597988613025812)
	if not mise:
		await jeu.send(ctx.author.mention+' Combien voulez-vous miser ?')
		def check(m):
			return m.author == ctx.author and m.channel == jeu
		mise = await bot.wait_for('message', timeout=None, check=check)
	try:
		mise = int(mise.content)
	except:
		jeu.send(":warning: Ceci n'est pas un chiffre, veuillez recommencer avec un chiffre")
		return
	if Eco["Comptes"][str(ctx.author.id)] < mise:
		await jeu.send(":warning: Vous n'avez pas assez d'argent pour miser ca !")
		return
	Eco["Comptes"][str(ctx.author.id)] -= mise
	Eco["Mises"][str(ctx.author.id)] = [0,mise]
	await jeu.send('Confirmez vous votre partie avec une mise de '+str(mise)+' ?',view=gains())
	with open('economie.json', 'w') as f:
		json.dump(Eco, f, indent=6)

class gains(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label='Jouer à la Roulette Russe', style=discord.ButtonStyle.green, custom_id='roulette')
	async def Roulette(self, interaction: discord.Interaction, button: discord.ui.Button):
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		if str(interaction.user.id) not in Eco["Mises"].keys():
			await interaction.response.send_message(":warning: Vous n'avez pas commencé de parties de Roulette Russe !",ephemeral=True)
			return
		chance = random.randint(1, 6-Eco["Mises"][str(interaction.user.id)][0])
		multip = [115/100,27/23,35/27,10/7,2]
		if 1 == chance:
			Eco["Mises"].pop(str(interaction.user.id))
			embed = discord.Embed(
				title='Vous avez perdu...',
				description='Vous pouvez toujours retenter votre chance !',
			)
			embed.timestamp = datetime.utcnow()
			embed.set_footer(text='', icon_url='')  # \u200b to remove text
			embed.set_thumbnail(url='https://c.tenor.com/ZpBMkWyufhMAAAAC/dead.gif')
			await interaction.response.send_message(embed=embed)
		elif Eco["Mises"][str(interaction.user.id)][0] == 4:
			Eco["Mises"][str(interaction.user.id)][1] = Eco["Mises"][str(interaction.user.id)][0]*2
			embed = discord.Embed(
				title='JACKPOT !',
				description='Vous avez gagné ' + str(Eco["Mises"][str(interaction.user.id)][1])+
			"$ ! Vous avez touché le maximum d'argent possible !"
			)
			embed.timestamp = datetime.utcnow()
			embed.set_footer(text='', icon_url='')  # \u200b to remove text
			embed.set_thumbnail(url='https://c.tenor.com/YjPBups7H48AAAAC/6m-rain.gif')
			Eco["Comptes"][str(interaction.user.id)] += Eco["Mises"][str(interaction.user.id)][1]
			await interaction.response.send_message(embed=embed)
		else:
			Eco["Mises"][str(interaction.user.id)] = [Eco["Mises"][str(interaction.user.id)][0]+1, round(multip[Eco["Mises"][str(interaction.user.id)][0]] * Eco["Mises"][str(interaction.user.id)][1])]
			embed = discord.Embed(
				title='Vous avez gagné !',
				description='Vous avez gagné ' + str(Eco["Mises"][str(interaction.user.id)][1])+
			"$ !\nTenterez vous de rejouer afin d'augmenter votre gain à " + str(round(Eco["Mises"][str(interaction.user.id)][1] * multip[Eco["Mises"][str(interaction.user.id)][0]-1])) + "$ ?"
				)
			embed.timestamp = datetime.utcnow()
			embed.set_footer(text='', icon_url='')  # \u200b to remove text
			embed.set_thumbnail(url='https://c.tenor.com/YjPBups7H48AAAAC/6m-rain.gif')
			await interaction.response.send_message(embed=embed, view=gains())
		with open('economie.json', 'w') as f:
			json.dump(Eco, f, indent=6)
		await interaction.message.delete()
	@discord.ui.button(label='Ne pas jouer', style=discord.ButtonStyle.red, custom_id='arret')
	async def Arretroulette(self, interaction: discord.Interaction, button: discord.ui.Button):
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		if str(interaction.user.id) not in Eco["Mises"].keys():
			await interaction.response.send_message(":warning: Vous n'avez pas commencé de parties de Roulette Russe !")
			return
		await interaction.response.send_message('Vous avez gagné '+str(Eco["Mises"][str(interaction.user.id)][1])+"$ !")
		Eco["Comptes"][str(interaction.user.id)] += Eco["Mises"][str(interaction.user.id)][1]
		Eco["Mises"].pop(str(interaction.user.id))

class Machineasous(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label='Jouer à la Machine à sous', style=discord.ButtonStyle.green, custom_id='machine')
	async def Machine(self, interaction: discord.Interaction, button: discord.ui.Button):
		com = bot.get_channel(961597988613025812)
		com.send(f'{interaction.user.mention} Combien voulez vous miser ? ')
		def check(m):
			return m.author == interaction.user and m.channel == com
		msg = await bot.wait_for('message', timeout=None, check=check)
		try:
			mise = int(msg.content)
		except:
			await com.send(':warning: Veuillez indiquer un chiffre !')
			return
		rec = [{'iron':['https://gamepedia.cursecdn.com/minecraft_gamepedia/0/06/Iron_Ingot_JE2_BE2.png',25]},
			   {"gold":['gold',50]},
			   {"dia":['diamant',75]},
			   {'ame':['amethyste',100]},
			   {'tit':['titane',250]},
			   {'pala':['https://lh3.googleusercontent.com/nYLin0cucsC32StqXD4USvthj-9ypNzVptz9oZWZ0t4-oMLdXWYZKmjYPqlzPNFypRHwKKv0qFlCbUOaXWvb=s400',500]},
			   {'end':['endium',1000]}]
		desc = []
		for i in range(3):
			desc.append(rec[random.randint(0,7)])
		if desc[0] == desc[1] == desc[2]:
			mise = mise
		embed = discord.Embed(
			title='Machine à sous',
			description=f'',
		)
		embed.timestamp = datetime.utcnow()
		embed.set_footer(text='', icon_url='')  # \u200b to remove text
		embed.set_thumbnail(
			url='https://cdn.discordapp.com/attachments/772451269272928257/937037959516000286/unknown.png')
		return embed

class roulette(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label='Jouer à la Roulette Américaine', style=discord.ButtonStyle.green, custom_id='debutrouletteA')
	async def RoulletteA(self, interaction: discord.Interaction, button: discord.ui.Button):
		jeu = bot.get_channel(961597988613025812)
		embed = create_small_embed('Roulette Américaine')
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/772451269272928257/965658339428171876/unknown.png")
		await jeu.send(embed=embed,view=rouleView())
		await interaction.response.send_message("Vous avez une partie en cours dans le channel "+jeu.mention,ephemeral=True)

class roule(discord.ui.Select):
	def __init__(self):
		options = [
			discord.SelectOption(label='Miser sur un chiffre', description='Mise x36'),
			discord.SelectOption(label='Miser sur Rouge', description='Mise x2'),
			discord.SelectOption(label='Miser sur Noir', description='Mise x2'),
			discord.SelectOption(label='Miser sur Pair', description='Mise x2'),
			discord.SelectOption(label='Miser sur Impair', description='Mise x2'),
			discord.SelectOption(label='Miser sur Manque', description='Mise x2'),
			discord.SelectOption(label='Miser sur Passe', description='Mise x2'),
			discord.SelectOption(label='Miser sur la première douzaine (1-12)', description='Mise x3'),
			discord.SelectOption(label='Miser sur la deuxième douzaine (13-24)', description='Mise x3'),
			discord.SelectOption(label='Miser sur la troisième douzaine (25-36)', description='Mise x3'),
		]
		super().__init__(placeholder='Sur quoi voulez vous miser ?', min_values=1, max_values=1, options=options,
						 custom_id='inter')
	async def callback(self, interaction: discord.Interaction):
		chiffres = {'Roug': [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
					'Noir': [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35],
					'Pair': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36],
					'Impa': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35],
					'Manq': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
					'Pass': [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36],
					'la p': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
					'la d': [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
					'la t': [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]}
		if self.values[0] == 'Miser sur un chiffre':
			def check(m):
				return m.author == interaction.user and m.channel == interaction.channel
			chiffre = await bot.wait_for('message', timeout=None, check=check)
			try:
				if int(chiffre.content) > 36:
					await interaction.response.send_message(":warning: Vous ne pouvez miser que sur des chiffres entre 0 et 36, ainsi que le 00")
					return
				if chiffre.content == "00":
					chiffre = [37]
				else:
					chiffre = [int(chiffre.content)]
			except:
				await interaction.channel.send(":warning: Ceci n'est pas un chiffre, veuillez recommencer avec un chiffre")
				return
		else:
			chiffre = chiffres[self.values[0][10:14]]
		await interaction.channel.send(f'{interaction.user.mention} Combien voulez vous miser ?')
		def check(m):
			return m.author == interaction.user and m.channel == interaction.channel
		mise = await bot.wait_for('message', timeout=None, check=check)
		try:
			mise = int(mise.content)
		except:
			await interaction.channel.send(":warning: Ceci n'est pas un chiffre, veuillez recommencer avec un chiffre")
			return
		await compte(interaction.user)
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		if Eco["Comptes"][str(interaction.user.id)] < mise:
			await interaction.channel.send(":warning: Vous n'avez pas assez d'argent pour miser ca !")
			return
		chance = random.randint(0,37)
		if chance == 0 or chance == 37:
			couleur = 'Vert'
		elif chance in chiffres['Roug']:
			couleur = 'Rouge'
		else:
			couleur = 'Noir'
		if chance in chiffre:
			if self.values[0][10:12] == 'un':
				mise = mise * 35
			elif self.values[0][10:12] == "la":
				mise = mise * 2
			await interaction.response.send_message(embed=discord.Embed(title=f'{chance}. {couleur}.',description=f'{interaction.user.mention} Vous avez misé {self.values[0][6:]} et vous avez gagné {mise}$ !'))
			Eco["Comptes"][str(interaction.user.id)] += mise
		else:
			await interaction.channel.send(embed=discord.Embed(title=f'{chance}. {couleur}.',description=f'{interaction.user.mention} Vous avez perdu.'))
			Eco["Comptes"][str(interaction.user.id)] -= mise
		with open('economie.json', 'w') as f:
			json.dump(Eco, f, indent=6)

class rouleView(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
		self.add_item(roule())

async def reset(ctx,res):
	if res == 'eco' or res == 'tout':
		Eco = {
			"Comptes": {},
			"Mises": {},
			"tickets": "0000",
			"commande": {},
			"Auteurs": {}
		}
	with open('economie.json', 'w') as f:
		json.dump(Eco, f, indent=6)
	ctx.reply("Tout s'est bien passé")