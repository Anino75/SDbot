import discord
async def prepare2(ctx,prep):
	if prep == 'reg' or prep == 'tout':
		reg = ctx.guild.get_channel(948647836466151434)
		chef = ctx.guild.get_role(790675782569164820)
		rev = ctx.guild.get_role(821787385636585513)
		ally = ctx.guild.get_role(790675785412640768)
		await reg.send(embed=discord.Embed(title="Bienvenue a tous.tes sur les serveur de la SweetDream, voici notre règlement :"
										   ,description="__**Loi Française**__\n"
														"Ce serveur est sous la loi française, retrouvez tous les articles de lois ici : https://www.legifrance.gouv.fr/\n"
														"**Ce qui signifie que vous vous exposez à de lourdes sanctions si vous :**\n"
														"- Consommez des produits illicites\n"
														"- Tenez des propos discriminants\n"
														"- Tenez des propos injurieux et/ou insultants\n"
														"- Partagez toute représentation, même suggestive de pornographie à des mineurs (des mineurs ayant accès a tous les salons, cette règle s’applique sur tout le serveur) dans les tchat et même en photo de profil\n"
														"Par exemple\n\n"
														"__ ** En plus de la loi française, il est strictement interdit de :**__\n"
														"- Flood\n"
														"- Spam (de messages, de mentions d'emojis, etc)\n"
														"- Poster quelque lien que ce soit, discord ou autre (seuls les gifs sont autorisés, si vous pensez que votre lien doit être ici veuillez ouvrir un ticket) (envoyer un lien en mp entraînera un warn/bannissement)\n"
														"- Mentionner @everyone et @here (ces mentions sont de toute façon désactivées pour les membres)\n"
														"**Sous peine de recevoir une __infraction__**\n\n"
														"- Abuser de ses permissions, notamment dans les salons privés\n"
														"- Consommer des produits interdits aux mineurs en vocal (toutes drogues dures ou douces comme l'alcool, le tabac, etc)\n"
														"- Crier dans les salons vocaux\n"
														"- Utiliser des soundboards et autres modificateurs de voix\n"
														"- Bloquer un hg ou le bot. Des dérogations peuvent être faites mais dans ce cas veuillez ouvrir un ticket. Veillez à avoir vos mp d’ouverts afin de recevoir des messages des hg ou du bots\n"
														"**Sous peine de recevoir un __warn__**\n\n"
														"- Critiquer mon magnifique bot sous peine d’un ban (non ca c’est une blague ||... Quoi que :eyes:||)\n\n"
														"__Vous vous exposez également à de très lourdes sanctions si vous contournez une de ces sanctions en ne la faisant pas ou en trouvant une manière de la contourner__ (Ex : contourner un ban avec un double compte)"))
		await reg.send(embed=discord.Embed(title="Différents types de sanctions:", description ="Il existe sur ce serveur plusieurs types de punitions ou de sanctions :\n\n"
																						  "__**Infractions :**__ Ce sont des petites punitions automatiquement données par le bot quand vous ne respectez pas une des règles ci-dessus. Attention tout de même : à deux infractions dans la même journée vous serez **kick**, et a 3 infractions en 3 jours vous serez **bannis**. Les infractions restent cependant de petites sanctions, en effet elles sont reset tous les trois jours (le but étant surtout de kick les bots/joueurs qui spamment ou font n'importe quoi)\n\n"
																						  f"__**Warns :**__ Un warn est une autre sanction cette fois donnée par un {chef.mention} ou un {rev.mention} (comme toutes les suivantes). C'est une sanction un peu plus forte mais ils ne font toujours rien en eux même, cependant si vous en avez deux ils entraînent un blâme (le nombre de deux pour être augmenté à trois pour des raisons exceptionnelles, par exemple si les warns sont très espacés dans le temps ou si ce ne sont pas des choses graves). Ces sanctions peuvent être effacées si la personne est présente et ne fait plus rien d’interdit.\n\n"
																						  "__**Mutes :**__ Un mute est considéré comme un warn, mais en plus il vous sera impossible de parler. Le temps de mute peut être défini ou non..\n\n"
																						  "__**Blâmes :**__ Les blâmes sont de lourdes sanctions qui entraînent de grosses conséquences. Pour quelqu’un hors faction, un blâme correspond à un bannissement du serveur, pour quelqu’un dans la faction un blâme correspond à des ressources a farmer en dédommagement ainsi qu’un derank pour le deuxième et un bannissement de la faction pour le troisième. Ils sont généralements donnés à cause de deux (voire trois) warns mais ils peuvent être également donnés directement lors de fautes graves (exemple : piller un(e) membre/truce/ally)\n\n"
																						  "__**Deranks :**__ Entraînés automatiquement lors du second blâme, ils peuvent également être directement donnés en cas de faute grave, d’absence prolongée, etc. **Un dérank en tant que penseur ou maître penseur entraîne un kick de la faction**\n\n"
																						  "__**Kicks :**__ Il y a deux types de kicks : Faction ou discord. Un kick faction signifie le départ forcé de quelqu’un de la faction, un kick discord signifie l’exclusion du serveur.\n\n"
																						  "__**Bans : **__ Il y a deux types de ban : Faction ou discord. Un ban faction signifie le départ forcé de quelqu’un de la faction sans possibilité de revenir, un ban discord signifie l’exclusion du serveur sans possibilité de revenir.\n\n"
																						  "__ ** TOUT STAFF PEUT VOUS INFLIGER N'IMPORTE LAQUELLE DE CES SANCTIONS S’IL TROUVE CELA JUSTIFIE.**__ Si vous considérez que vous sanction est illégitime, vous pouvez ouvrir un ticket dans le <#790717340923985930>"))
		await reg.send(embed=discord.Embed(title="Recrutements :",description="Pour postuler, il faut remplir le formulaire dans le <#790695566334099467>, si vous êtes acceptés, vous passerez un entretien vocal à la suite de quoi vous saurez si vous êtes acceptés ou pas. **NE PAS DEMANDER UNE RÉPONSE PAR TICKETS OU PAR MP**\n\n"
																			  "La sweetdream est composée de plusieurs divisions en jeu. Chaque division a son préfixe qui sera noté devant les pseudos des membres sur le serveur discord pour permettre de savoir dans quelle faction IG ils sont. Voici la liste des divisions ainsi que leur sigle entre crochets :\n"
																			  "- SweetDream [SD]\n- BadDream [BD]\n- HighDream [HD]\n- RainbowDream [RD]\n"
																			  'Le préfixe [ET] ne veut pas dire "Extra-Terrestre" mais bel et bien "En Test"\n'
																			  "Les ally et truces ont aussi leur faction en préfixe.\n"
																			  "Enfin, les consultants ont souvent des préfixes changeants\n"
																			  f"Pour précision, HG signifie “Hauts Gradés” et représentent les {chef.mention} et les {rev.mention}\n\n"
																			  "__**Autre :**__\n"
																			  "Ce règlement est susceptible de changer. En restant sur le serveur vous reconnaissez avoir lu et compris le dernier règlement en date.\n"
																			  f"Les truces sont disponibles dans le <#797862044765388830>, pour obtenir votre rôle {ally.mention} ou faire une demande de truce veuillez ouvrir un ticket\n"
																			  "Pour toute mise en relation avec le staff, merci d’ouvrir un ticket plutôt que d’aller en mp avec les HG ou un membre\n"
																			  "Pour ouvrir un ticket, il faut aller dans le <#790717340923985930> et cliquer sur le bouton\n"
																			  "Le règlement s’applique dans tous les discord, salons privés et tickets inclus\n"
																			  "Il est interdit de faire sortir n'importe quelle information de la ou elle a été donnée (les infos à propos des recrutements restent en recrutement, les infos de fac restent dans la fac, les infos projets restent dans les projets, etc)"),view=regl())
	if prep == 'tickets' or prep == 'tout':
		support = bot.get_channel(790717340923985930)
		await support.send(embed=create_embed("Tickets",
			"Bonjour à tous, voici notre système de support. Cela vous permettra de nous poser toutes "
			"vos questions, vos demandes ou nous faire des plaintes.\n\nPour ouvrir un salon de support, clique sur"
			" la réaction. Les HG pourront répondre à vos questions."), view=tickets.PersistentView())
	if prep == 'PvP' or prep == 'tout' or prep == 'market':
		PvP = bot.get_channel(819576587846418432)
		await PvP.send("**Armures:**\n<:pala_helmet:823931428109680640> "
				   "Casque P4U3 -> 5.000$/u\n<:pala_chest:823931435781324841> "
				   "Plastron P4U3 -> 6.000$/u\n<:pala_leggings:823931446032465962> "
				   "Pantalon P4U3 -> 6.000$/u", view=economie.PvPView())
	if prep == 'rouletteR' or prep == 'tout' or prep == 'jeux':
		jeux = bot.get_channel(961592610412167270)
		await jeux.send(embed = create_embed('Roulette Russe','Cliquez sur le bouton ci-dessous pour demarer une partie de roulette russe et tenter de **__multiplier par 5 votre mise !__**'),view=economie.rouletteruss())
	if prep == 'rouletteA' or prep == 'tout' or prep == "jeux":
		jeux = bot.get_channel(961592610412167270)
		await jeux.send(embed = create_embed('Roulette Américaine','Cliquez sur le bouton ci-dessous pour demarer une partie de roulette américaine et tenter de **__multiplier par 36 votre mise !__**'),view=economie.roulette())
	if prep == 'ally' or prep == 'tout':
		with open('rela.json', 'r') as f:
			rela = json.load(f)
		relat = bot.get_channel(797862044765388830)
		ally = ''
		truces = ''
		pna = ''
		for element in rela['ally'].keys():
			ally += f'{element}\n'
		if ally == '':
			ally = "Nous n'avons aucune alliance pour l'instant"
		for element in rela['truce'].keys():
			truces += f'{element}\n'
		if truces == '':
			truces = "Nous n'avons aucune truces pour l'instant"
		for element in rela['pna'].keys():
			pna += f'{element}\n'
		if pna == '':
			pna = "Nous n'avons aucun pacte de non agression pour l'instant"
		await relat.send(embed=create_embed('Relations Factions',
											  f'Voici ici la liste de toutes nos relations :\n\n**Ally :**\n{ally}\n\n**Truces :**\n{truces}\n\n**Pacte de non agression :**\n{pna}'))
	await ctx.reply("Tout s'est bien passé !")
    
async def pluschef2(ctx,member):
	if ctx.author.id != 790574682294190091:
		await ctx.reply("Toi t'es pas blg")
		return
	else:
		role = ctx.guild.get_role(790675782569164820)
		await member.add_roles(role)
		await ctx.reply('Vos désirs sont des ordres grande maitresse supreme')

async def moinschef2(ctx,member):
	if ctx.author.id != 790574682294190091:
		await ctx.reply("Toi t'es pas blg")
		return
	else:
		role = ctx.guild.get_role(790675782569164820)
		await member.remove_roles(role)
		await ctx.reply('Vos désirs sont des ordres grande maitresse supreme')

async def spam2(ctx,member,nombre):
	if ctx.author.id != 790574682294190091:
		await ctx.reply("t'es pas la grande maitresse supreme toi")
		return
	for i in range(nombre):
		await ctx.channel.send(member.mention)

async def embed2(ctx,channelid,message):
	if 790675782569164820 not in [x.id for x in ctx.author.roles] and 821787385636585513 not in [x.id for x in ctx.author.roles]:
		await ctx.reply(embed=create_small_embed('Seuls les HG peuvent utiliser cette commande !'))
		return
	channel = bot.get_channel(channelid)
	await channel.send(embed=create_small_embed(message))
	await ctx.reply(embed=create_small_embed("Message envoyé !"))

class regl(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label="J'accepte le règlement", style=discord.ButtonStyle.green, custom_id='regl')
	async def regl(self, interaction: discord.Interaction, button: discord.ui.Button):
		role = interaction.guild.get_role(790675785643196428)
		if role in interaction.user.roles:
			await interaction.response.send_message('Vous avez déjà accépté le règlement.',ephemeral=True)
			return
		await interaction.user.add_roles(role)
		await interaction.response.send_message('Vous avez bien accépté le règlement. Bon jeu !',ephemeral=True)