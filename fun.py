import discord

async def aleacrush2(ctx,member):
	if not member:
		member = ctx.author
	guild = ctx.guild
	member2 = guild.members[random.randint(0,len(guild.members))]
	await ctx.reply(embed=create_small_embed(f'{member.mention}, Vous êtes tombé sous le charme de {member2.mention}'))

async def pendu2(ctx):
	with open('liste_francais.txt','r',encoding="latin-1") as f:
		liste = f.readlines()
	f = 0
	pend = ["","```\n_______```","```\n|\n|\n|\n|\n|\n_______```","```\n__________\n|\n|\n|\n|\n|\n_______```","```\n__________\n|         |\n|\n|\n|\n|\n_______```","```\n__________\n|         |\n|         °\n|\n|\n|\n_______```","```\n__________\n|         |\n|         °\n|         |\n|\n|\n_______```","```\n__________\n|         |\n|         °\n|         |\n|         /\n|\n_______```","```\n__________\n|         |\n|         °\n|         |\n|         /\ \n|\n_______```","```\n__________\n|         |\n|         °\n|         |\ \n|         /\ \n|\n_______```","```\n__________\n|         |\n|         °\n|        /|\ \n|         /\ \n|\n_______```"]
	mot = list(liste[random.randint(0,len(liste))].lower())
	trouv = ['- ']*(len(mot)-1)
	util = []
	mot.pop(-1)
	message = await ctx.reply(" ".join(trouv))
	while f<10:
		let = await ctx.reply('\nVeuillez donner une lettre')
		lettre = (await waiting(ctx)).content
		if lettre in util:
			await ctx.reply('Vous avez déjà utilisé cette lettre !')
		else:
			if lettre in mot:
				for i in range(len(mot)):
					if mot[i] == lettre:
						trouv[i] = lettre
			else:
				await ctx.reply("Votre lettre n'est pas dans le mot")
				f += 1
			util.append(lettre)
		await message.delete()
		message = await ctx.reply(content=pend[f]+"\n"+' '.join(trouv))
		if trouv == mot:
			await ctx.reply('Vous avez gagné ! Félicitations !')
			return
		await let.delete()
	await ctx.reply(f"Vous avez perdu ! Le mot était {''.join(mot)}")

async def waiting(ctx):
	def check(m):
		return m.author == ctx.author and m.channel == ctx.channel
	lettre = await bot.wait_for('message', timeout=600, check=check)
	if len(lettre.content)>1 or ord(lettre.content)<97 or ord(lettre.content)>122:
		await ctx.reply("Veuillez n'indiquer qu'une seule lettre minuscule")
		lettre = await waiting(ctx)
	return lettre

async def motus2(ctx):
	with open('liste_francais.txt','r',encoding="latin-1") as f:
		liste = f.readlines()
	mot = list(liste[random.randint(0,len(liste))].upper())
	mot.pop(-1)
	print(mot)
	message = await ctx.reply(f"Veuillez indiquer des mots en {len(mot)} lettres\n")
	for j in range(5):
		let = await ctx.reply('\nVeuillez donner un mot')
		motu = list(((await ww(ctx,len(mot))).content).upper())
		if motu == mot:
			await ctx.reply('Vous avez gagné ! Félicitations !')
			await message.edit(content=message.content+'\n***__'+'__*** ***__'.join(motu)+'__***')
			return
		for i in range(len(motu)):
			if motu[i] in mot:
				if motu[i] == mot[i]:
					motu[i] = f'***{motu[i]}***'
				motu[i] = f'__{motu[i]}__'
		desc = message.content+"\n"+' '.join(motu)
		await message.delete()
		message = await ctx.reply(desc)
		await let.delete()
	await ctx.reply(f"Vous avez perdu ! Le mot était {''.join(mot)}")

async def ww(ctx,ll):
	with open('liste_francais.txt','r',encoding="latin-1") as f:
		liste = f.readlines()
	def check(m):
		return m.author == ctx.author and m.channel == ctx.channel
	lettre = await bot.wait_for('message', timeout=600, check=check)
	if len(lettre.content)!=ll:
		await ctx.reply(f"Veuillez n'indiquer que des mots francais de {ll} lettres")
		lettre = await ww(ctx,ll)
	if (lettre.content+'\n') not in liste:
		print("pb")
	return lettre