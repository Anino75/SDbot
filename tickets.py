import discord

class PersistentView(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label='Ouvrir un ticket', style=discord.ButtonStyle.green, custom_id='ticket')
	async def ticket(self,interaction: discord.Interaction, button: discord.ui.Button):
		with open('tickets.json', 'r') as f:
			ticket = json.load(f)
		for x in list(ticket['auteurs'].items()):
			if interaction.user.id == x[1] and 790675782569164820 not in [x.id for x in interaction.user.roles] and 821787385636585513 not in [x.id for x in interaction.user.roles]:
				await interaction.response.send_message(":warning: Vous avez déjà un ticket ouvert !", ephemeral=True)
				return
		guild = bot.get_guild(790367917812088864)
		tick = await interaction.guild.create_text_channel(name="Ticket "+str(ticket['tickets']),overwrites={guild.default_role: discord.
			PermissionOverwrite(read_messages=False, send_messages=False,),interaction.user:discord.
			PermissionOverwrite(read_messages=True, send_messages=True,)},category=guild.get_channel(790707455033999373))
		await tick.send(interaction.user.mention,embed=create_small_embed("Posez votre question et attendez la réponse d'une "
																	"personne compétente.\nCliquez sur la réaction pour"
																	" fermer le salon de support."),view=fermerticket())
		ticket['auteurs'][ticket['tickets'][-4:]] = interaction.user.id
		if int(ticket['tickets'])+1>999:
			ticket['tickets'] = str(int(ticket['tickets']) + 1)
		else:
			ticket['tickets'] = "0"+str(int(ticket['tickets'])+1)
		with open('tickets.json', 'w') as f:
			json.dump(ticket, f, indent=6)
		await interaction.response.send_message(interaction.user.mention+" Vous avez crée le channel "+tick.mention, ephemeral=True)

class fermerticket(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label='Fermer le ticket', style=discord.ButtonStyle.green, custom_id='fermticket')
	async def fermer(self,interaction: discord.Interaction, button: discord.ui.Button):
		if 790675782569164820 not in [x.id for x in interaction.user.roles] and 821787385636585513 not in [x.id for x in interaction.user.roles]:
			await interaction.response.send_message(embed=create_small_embed(':warning: Seuls les HG peuvent fermer un ticket !',discord.Color.red()))
			return
		with open('tickets.json', 'r') as f:
			ticket = json.load(f)
		transcript = await chat_exporter.export(interaction.channel)
		transcript_file = discord.File(
			io.BytesIO(transcript.encode()),
			filename=f"transcript-{interaction.channel.name}.html",
		)
		ticket['auteurs'].pop(interaction.channel.name[-4:])
		log = bot.get_channel(790721209305792553)
		with open('tickets.json', 'w') as f:
			json.dump(ticket, f, indent=6)
		await log.send(file=transcript_file)
		await interaction.channel.delete()

async def close(ctx):
	if 790675782569164820 not in [x.id for x in ctx.author.roles] and 821787385636585513 not in [x.id for x in
																										 ctx.author.roles]:
		await ctx.reply(embed=create_small_embed(':warning: Seuls les HG peuvent fermer un ticket !', discord.Color.red()))
		return
	with open('tickets.json', 'r') as f:
		ticket = json.load(f)
	transcript = await chat_exporter.export(ctx.channel)
	transcript_file = discord.File(
		io.BytesIO(transcript.encode()),
		filename=f"transcript-{ctx.channel.name}.html",
	)
	ticket['auteurs'].pop(ctx.channel.name[-4:])
	log = bot.get_channel(790721209305792553)
	with open('tickets.json', 'w') as f:
		json.dump(ticket, f, indent=6)
	await log.send(file=transcript_file)
	await ctx.channel.delete()
