import asyncio
from code import interact
from inspect import stack
import io
import json
import random
import sys
import time
import traceback
from datetime import datetime, timedelta
import math
from urllib import response
#from sqlalchemy import true
import chat_exporter
import discord
from discord.ext import commands, tasks
import mysql.connector
import typing
from typing import Optional
import requests

debug = True
SERVER = True
intents = discord.Intents().all()

class PersistentViewBot(commands.Bot):
	def __init__(self):
		super().__init__(command_prefix=commands.when_mentioned_or('SD'), help_command=None, case_insensitive=True, intents=intents)
	async def setup_hook(self) -> None:
		self.add_view(PersistentView())
		self.add_view(fermerticket())
		self.add_view(PvPView())
		self.add_view(farmView())
		self.add_view(mineraisView())
		self.add_view(alchimisteView())
		self.add_view(livresView())
		self.add_view(machinesView())
		self.add_view(outilsView())
		self.add_view(servicesView())
		self.add_view(pillagesView())
		self.add_view(basesclaimView())
		self.add_view(RouleR())
		self.add_view(contijouer(0,0))
		self.add_view(roulette())
		self.add_view(rouleView({},0))
		self.add_view(regl())
		self.add_view(IsAlly())
		self.add_view(candid(0))
		self.add_view(page())
		self.add_view(NombreView())
		self.add_view(ench())
		self.add_view(vend())
		self.add_view(pagecl())
		self.add_view(actu())
		self.add_view(boutonform())
		self.add_view(boutonform2([]))
		self.add_view(autoview([],[]))
		self.add_view(blackjackview())
#		self.add_view(divi())

bot = PersistentViewBot()

"""
This logs discord api actions too:
global LOGGER
LOGGER.basicConfig(filename='command.log', format=f"{datetime.now().strftime('%Y:%m:%d %H:%M:%S')} [%(levelname)s] %(message)s",
						  encoding='utf-8', level=0)
"""
with open('token.txt', 'r') as f:
	TOKEN = f.read()

# =========== Tools ===========

@bot.command()
async def sync(ctx):
    synced = await ctx.bot.tree.sync()
    await ctx.send(f"Synced {len(synced)} commands")

async def infac(member:discord.Member):
	fac = [1068460789612163072,790675782569164820, 821787385636585513, 790675781789155329, 791426367362433066,1011394095383580843,790675782338740235, 790675782364037131, 790675783352975360,790675783549976579, 790675783693500456, 790675784120401932,790675784225521734, 791066206437113897, 791066207418712094,1011953852427272302,791066206109958204,790675784901197905]
	t = [x.id for x in member.roles]
	for x in fac:
			if x in t:
				return True 
	return False

""" tree = bot.tree
@tree.error()
async def on_app_command_error(interaction: Interaction,error: AppCommandError):
	if isinstance(error, commands.MissingPermissions):
		await interaction.response.send_message(f'''Tu n'as pas la permission pour effectuer cette action !''')
	elif isinstance(error, commands.MissingPermissions):
		await interaction.response.send_message(f'''Tu n'as pas le rôle nécéssaire pour effectuer cette action !''')
	elif isinstance(error, commands.MissingRequiredArgument):
		await interaction.response.send_message(f'''> <:Forget:1002454977043771443> __{interaction.user.mention}__, Tu as oublié une partie de la commande, réessaies comme sa : *`r!ban <mention> <raison>`*''')
 """

@bot.tree.command()
@discord.app_commands.checks.has_any_role(791066206109958204,1011953852427272302,791066207418712094,791066206437113897,790675784225521734,790675784120401932,790675783693500456,790675783549976579,790675783352975360,790675782364037131,790675782338740235,821787385636585513,790675782569164820)
async def absence(interaction: discord.Interaction,raison:str,date:str) -> None:
	"""Merci de mettre la date sous la forme JJ/MM/AAAA"""
	if 813928386946138153 in [x.id for x in interaction.user.roles]:
		await interaction.response.send_message('Vous êtes déjà absent.e !')
		return
	try:
		if int(date[0:2]) + int(date[3:5]) + int(date[6:10]) < 2100 and len(date) == 10 and ((int(date[0:2])>int(str(datetime.now())[8:10]) and int(date[3:5])==int(str(datetime.now())[5:7]) and int(date[6:10])>=int(str(datetime.now())[0:4])) or (int(date[3:5])>int(str(datetime.now())[5:7]) and int(date[6:10])>=int(str(datetime.now())[0:4]))):
			pass
		else:
			await interaction.response.send_message("La date n'est pas valide, merci de recommencer avec une date valide")
			return
	except:
		await interaction.response.send_message("La date n'est pas valide, merci de recommencer avec une date valide")
		return
	with open('absence.json', 'r') as f:
		ab = json.load(f)
	if date[0:10] in ab.keys():
		ab[date[0:10]][interaction.user.id] = raison
	else:
		ab[date[0:10]] = {interaction.user.id:raison}
	with open('absence.json', 'w') as f:
		json.dump(ab, f, indent=6)
	chanel = bot.get_channel(790719427800858634)
	await chanel.send(f"{interaction.user.mention} est absent jusqu'au {date} pour {raison}")
	role = interaction.guild.get_role(813928386946138153)
	await interaction.user.add_roles(role)
	await interaction.response.send_message('Votre absence a bien été prise en compte')


""" @bot.tree.command()
@discord.app_commands.checks.cooldown(1, 604800, commands.BucketType.user)
async def choixdivi(interaction: discord.Interaction,divi:str) -> None:
	if 798301141094891620 not in  and 790675782569164820 not in [x.id for x in interaction.user.roles] and 791066207418712094 not in [x.id for x in interaction.user.roles] and 791066206437113897 not in [x.id for x in interaction.user.roles] and 790675784225521734 not in [x.id for x in interaction.user.roles] and 790675784120401932 not in [x.id for x in interaction.user.roles] and 790675783693500456 not in [x.id for x in interaction.user.roles] and 790675783549976579 not in [x.id for x in interaction.user.roles] and 790675783352975360 not in [x.id for x in interaction.user.roles] and 790675782364037131 not in [x.id for x in interaction.user.roles] and 790675782338740235 not in [x.id for x in interaction.user.roles]:
		await interaction.response.send_message(embed=create_small_embed(':warning: Seuls les membres peuvent utiliser cette commande !',discord.Color.red()))
		return
	if divi != "SD" and divi != "BD" and divi != "HD":
		await interaction.response.send_message('La division que vous avez indiqué n\'est pas bonne, merci  d\'ecrire `*choixdivi SD` ou BD ou HD')
		return
	guild = interaction.guild
	SD = guild.get_role(986333837065850952)
	BD = guild.get_role(991601555209990174)
	test = bot.get_channel(791452088370069525)
	if SD.id in [x.id for x in interaction.user.roles]:
		await interaction.user.remove_roles(SD)
	if BD.id in [x.id for x in interaction.user.roles]:
		await interaction.user.remove_roles(BD)
	if divi == "SD":
		await interaction.user.add_roles(SD)
		await interaction.user.edit(nick=f'[SD] {interaction.user.nick[5:]}')
	if divi == "BD":
		await interaction.user.add_roles(BD)
		await interaction.user.edit(nick=f'[BD] {interaction.user.nick[5:]}')
	if divi == "HD":
		await interaction.user.edit(nick=f'[HD] {interaction.user.nick[5:]}')
	await test.send(f'{interaction.user.mention} est passé dans la division {divi}')
	await interaction.response.send_message(f'Vous etes passé dans la {divi}') """

@tasks.loop(seconds = 36000)
async def abs():
	with open('absence.json', 'r') as f:
		ab = json.load(f)
	a = []
	date = f"{str(datetime.now())[8:10]}/{str(datetime.now())[5:7]}/{str(datetime.now())[0:4]}"
	guild=bot.get_guild(790367917812088864)
	for dates in ab.keys():
		if dates[6:] < date[6:] or (dates[3:5]<date[3:5] and dates[6:] == date[6:]) or (dates[0:2]<= date[0:2] and dates[3:5] == date[3:5] and dates[6:] == date[6:]):
			for personne in ab[dates].keys():
				personne = guild.get_member(int(personne))
				role = guild.get_role(813928386946138153)
				try:
					await personne.remove_roles(role)
				except:
					pass
		a.append(dates)
	for dates in a:
		ab.pop(dates)
	with open('absence.json', 'w') as f:
		json.dump(ab, f, indent=6)

@tasks.loop(seconds = 60)
async def voc():
	with open('voc.json','r') as f:
		voc = json.load(f)
	with open ('points.json','r') as f:
		pt = json.load(f)
	with open ('equipes.json','r') as f:
		eq = json.load(f)
	guild = bot.get_guild(790367917812088864)
	dtn = str(datetime.now())[5:7]+"/"+str(datetime.now())[0:4]
	if dtn not in voc.keys():
		voc[dtn] = {}
	for channel in guild.voice_channels:
		if len(channel.members)-1 > [mem.bot for mem in channel.members].count(True) and len(channel.members)-1 > [mem.voice.mute for mem in channel.members].count(True) and len(channel.members)-1 > [mem.voice.self_mute for mem in channel.members].count(True) and len(channel.members)-1 > [mem.voice.self_deaf for mem in channel.members].count(True) and len(channel.members)-1 > [mem.voice.deaf for mem in channel.members].count(True):
			for member in channel.members:
				if len(channel.members)>1 and member.voice.mute == False and member.voice.self_mute == False and member.voice.deaf == False and member.voice.self_deaf == False and member.bot == False:
					if str(member.id) in voc["total"].keys():
						voc["total"][str(member.id)] += 1
					else:
						voc["total"][str(member.id)] = 1
					if str(member.id) in voc[dtn].keys():
						voc[dtn][str(member.id)] += 1
					else:
						voc[dtn][str(member.id)] = 1
					if str(member.id) in pt.keys():
						pt[str(member.id)] += 3
					else:
						pt[str(member.id)] = 3
					for role in eq.keys():
						if int(role) in [t.id for t in member.roles]:
							eq[role]['total'] += 3
							if str(member.id) in eq[role]['membres'].keys():
								eq[role]['membres'][str(member.id)] += 3
							else:
								eq[role]['membres'][str(member.id)] = 3
	with open("voc.json",'w') as f:
		json.dump(voc, f, indent=6)
	with open ('points.json','w') as f:
		json.dump(pt,f,indent=6)
	with open ('equipes.json','w') as f:
		json.dump(eq,f,indent=6)

@bot.tree.command()
async def tempsdevoc(interaction: discord.Interaction,total_ou_mois:str) -> None:
	'''Consultez votre temps de voc total ou de ce mois ci (a partir du 1er)'''
	if total_ou_mois == "mois":
		total_ou_mois = str(datetime.now())[5:7]+"/"+str(datetime.now())[0:4]
	elif total_ou_mois != "total":
		await interaction.response.send_message('Vous ne pouvez voir que votre activité `totale` ou votre activité du `mois`')
		return
	with open('voc.json','r') as f:
		voc = json.load(f)
	if str(interaction.user.id) not in voc[total_ou_mois]:
		await interaction.response.send_message('''Vous n'êtes jamais venu en voc !''')
		return
	nb = sorted(voc[total_ou_mois].values(),reverse=True).index(voc[total_ou_mois][str(interaction.user.id)])+1
	await interaction.response.send_message(f'Vous avez `{voc[total_ou_mois][str(interaction.user.id)]}` minutes de voc et êtes {nb}{"eme" if nb != 1 else "er"}')

@bot.tree.command()
@discord.app_commands.checks.has_any_role(791426367362433066,821787385636585513,790675782569164820)
async def recruteurtempsdevoc(interaction: discord.Interaction,membre:discord.Member,total_ou_mois:str) -> None:
	'''Consultez l'activité vocale d'un membre en test. Commande réservée aux recruteurs.'''
	if 791066206109958204 not in [x.id for x in membre.roles]:
		await interaction.response.send_message('''Vous ne pouvez voir que l'activité des membres en test !''')
		return
	if total_ou_mois == "mois":
		total_ou_mois = str(datetime.now())[5:7]+"/"+str(datetime.now())[0:4]
	elif total_ou_mois != "total":
		await interaction.response.send_message('Vous ne pouvez voir que votre activité `totale` ou votre activité du `mois`')
		return
	with open('voc.json','r') as f:
		voc = json.load(f)
	if str(membre.id) not in voc[total_ou_mois]:
		await interaction.response.send_message(f'''{membre.mention} n'est jamais venu en voc !''')
		return
	await interaction.response.send_message(f'{membre.mention} a `{voc[total_ou_mois][str(membre.id)]}` minutes de voc')

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def joueurtempsdevoc(interaction: discord.Interaction,membre:discord.Member,total_ou_mois:str) -> None:
	'''Consultez l'activité vocale d'un membre. Commande réservée aux HG.'''
	if total_ou_mois == "mois":
		total_ou_mois = str(datetime.now())[5:7]+"/"+str(datetime.now())[0:4]
	elif total_ou_mois != "total":
		await interaction.response.send_message('Vous ne pouvez voir que votre activité `totale` ou votre activité du `mois`')
		return
	with open('voc.json','r') as f:
		voc = json.load(f)
	if str(membre.id) not in voc[total_ou_mois]:
		await interaction.response.send_message(f'''{membre.mention} n'est jamais venu en voc !''')
		return
	await interaction.response.send_message(f'{membre.mention} a `{voc[total_ou_mois][str(membre.id)]}` minutes de voc')

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def admintempsdevoc(interaction: discord.Interaction,total_ou_mois:str) -> None:
	'''Consultez l'activité vocale de tous les membres. Commande réservée aux HG.'''
	if total_ou_mois == "mois":
		total_ou_mois = str(datetime.now())[5:7]+"/"+str(datetime.now())[0:4]
	elif total_ou_mois != "total":
		await interaction.response.send_message('Vous ne pouvez voir que votre activité `totale` ou votre activité du `mois`')
		return
	with open('voc.json','r') as f:
		voc = json.load(f)
	msg = ''
	s = sorted(voc[total_ou_mois], key=lambda memb: voc[total_ou_mois][memb],reverse=True)
	if len(voc[total_ou_mois].keys()) < 20:
		for i in range(len(voc[total_ou_mois].keys())):
			msg += f'{i+1} : <@{s[i]}> - ({voc[total_ou_mois][s[i]]})\n'
	else:
		for i in range(20):
			msg += f'{i+1} : <@{s[i]}> - ({voc[total_ou_mois][s[i]]})\n'
	await interaction.response.send_message(embed=discord.Embed(title=f'Page 1',description=("Total :\n" if total_ou_mois == "total" else "Mois :\n")+msg),view=page())

class page(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label="Page précédente", style=discord.ButtonStyle.red, custom_id='prec')
	async def prec(self, interaction: discord.Interaction, button: discord.ui.Button):
		for element in interaction.message.embeds:
			tir = int(element.title[-1])
			if element.description[0:5] == "Total":
				total_ou_mois = "total"
			else:
				total_ou_mois = str(datetime.now())[5:7]+"/"+str(datetime.now())[0:4]
		if tir == 1:
			await interaction.response.send_message('Vous êtes déjà à la première page',ephemeral=True)
			return
		with open('voc.json','r') as f:
			voc = json.load(f)
		msg = ''
		s = sorted(voc[total_ou_mois], key=lambda memb: voc[total_ou_mois][memb],reverse=True)
		for i in range((tir-2)*20,(tir-1)*20):
			msg += f'{i+1} : <@{s[i]}> - ({voc[total_ou_mois][s[i]]})\n'
		await interaction.message.edit(embed=discord.Embed(title=f'Page {tir-1}',description=(("Total :\n" if total_ou_mois == "total" else "Mois :\n")+msg)))
		await interaction.response.send_message('Message modifié',ephemeral=True)
	@discord.ui.button(label="Page suivante", style=discord.ButtonStyle.green, custom_id='suiv')
	async def suiv(self, interaction: discord.Interaction, button: discord.ui.Button):
		for element in interaction.message.embeds:
			tir = int(element.title[-1])
			if element.description[0:5] == "Total":
				total_ou_mois = "total"
			else:
				total_ou_mois = str(datetime.now())[5:7]+"/"+str(datetime.now())[0:4]
		with open('voc.json','r') as f:
			voc = json.load(f)
		if tir*20 >= len(voc[total_ou_mois].keys()):
			await interaction.response.send_message('Vous êtes déjà à la dernière page',ephemeral=True)
			return
		msg = ''
		s = sorted(voc[total_ou_mois], key=lambda memb: voc[total_ou_mois][memb],reverse=True)
		if len(voc[total_ou_mois].keys()) < (tir+1)*20:
			for i in range(tir*20,len(voc[total_ou_mois].keys())):
				msg += f'{i+1} : <@{s[i]}> - ({voc[total_ou_mois][s[i]]})\n'
		else:
			for i in range(tir*20,(tir+1)*20):
				msg += f'{i+1} : <@{s[i]}> - ({voc[total_ou_mois][s[i]]})\n'
		await interaction.message.edit(embed=discord.Embed(title=f'Page {tir+1}',description=(("Total :\n" if total_ou_mois == "total" else "Mois :\n")+msg)))
		await interaction.response.send_message('Message modifié',ephemeral=True)

@bot.event
async def on_member_remove(member):
	if not member.bot:
		with open('phases.json', 'r') as f:
			phases = json.load(f)
		with open('Interview.json', 'r') as f:
			interviews = json.load(f)
		chanel = bot.get_channel(937312061833240586)
		if str(member.id) in phases["A faire"].keys():
			phases["A faire"].pop(str(member.id))
			await chanel.send(f'{member.mention} ({member.name}) est parti et à été retiré des phases')
		if str(member.id) in interviews["Dates"].keys():
			interviews["Dates"].pop(str(member.id))
			await chanel.send(f'{member.mention} ({member.name}) est parti et à été retiré des en attente')
		if str(member.id) in interviews["Wait"].keys():
			interviews["Wait"].pop(str(member.id))
			await chanel.send(f'{member.mention} ({member.name}) est parti et à été retiré des en attente')
		if str(member.id) in interviews["Responded"].keys():
			interviews["Responded"].pop(str(member.id))
			await chanel.send(f'{member.mention} ({member.name}) est parti et à été retiré des en attente')
		with open('phases.json', 'w') as f:
			json.dump(phases, f, indent=6)
		with open('Interview.json', 'w') as f:
			json.dump(interviews, f, indent=6)

@bot.tree.command()
async def spam(interaction: discord.Interaction,member: discord.Member,nombre: typing.Optional[int]):
	'''Spam allegrement quelqu'un. Commande réservée à la grande maîtresse suprême.'''
	if interaction.user.id != 790574682294190091:
		await interaction.response.send_message("t'es pas la grande maitresse supreme toi")
		return
	for i in range(nombre):
		await interaction.channel.send(member.mention)

'''
@bot.tree.command()
async def weshwesh(interaction: discord.Interaction):
	if interaction.user.id != 790574682294190091:
		await interaction.response.send_message('T'es pas la grande maitresse supreme toi !')
		return
	with open('voc.json','r') as f:
		voc = json.load(f)
	Roles = {"790675782338740235":48600,"790675782364037131":39600,"790675783352975360":31500,"790675783549976579":24300,"790675783693500456":18000,
			 "790675784120401932":12600,"790675784225521734":8100,"791066206437113897":4500,"791066207418712094":1800,"791066206109958204":0}
	for personne in interaction.guild.members:
		for tt in personne.roles:
			if str(tt.id) in Roles.keys():
				if str(personne.id) in voc['total'].keys():
					voc['total'][str(personne.id)] += Roles[str(tt.id)]
				else:
					voc['total'][str(personne.id)] = Roles[str(tt.id)]
	with open("voc.json",'w') as f:
		json.dump(voc, f, indent=6)
	await interaction.response.send_message('fait')


@bot.tree.command()
async def ilemosh(interaction: discord.Interaction,member: discord.Member):
	if interaction.user.id != 790574682294190091:
		await interaction.response.send_message("t'es pas la grande maitresse supreme toi")
		return
	with open('phases.json', 'r') as f:
		phases = json.load(f)
	phases["A faire"].pop(str(member.id))
	with open('phases.json', 'w') as f:
		json.dump(phases, f, indent=6)
	await interaction.response.send_message('nickel')

@bot.tree.command()
async def renduphases(interaction: discord.Interaction,member: discord.Member,*,rendu:str):
	if interaction.user.id != 790574682294190091:
		await interaction.response.send_message("t'es pas la grande maitresse supreme toi")
		return
	if not rendu:
		await interaction.response.send_message("t'as pas mis le rendu blg")
	with open('phases.json', 'r') as f:
		phases = json.load(f)
	phases["A faire"].pop(str(member.id))
	phases["Fait"][member.id]=[str(datetime.now()),rendu]
	with open('phases.json', 'w') as f:
		json.dump(phases, f, indent=6)
	await member.send("Merci d'avoir rendu votre phase, elle est suffisante et vous n'aurez pas besoin de farmer plus. Attention : ne parlez pas de cette phase ni combien de points vous avez donné sous peine de sanctions !")
	await interaction.response.send_message('nickel')

@bot.tree.command()
async def jj(interaction: discord.Interaction):
	with open('inac.json', 'r') as f:
		ina = json.load(f)
	e = discord.Embed(title = f'Inac', description = f'Voici toutes les personnes qui ont répondu au sondage')
	for typ in ina.items():
		st = ""
		for pers in typ[1]:
			tt = bot.get_user(pers)
			st += f'{tt.mention}\n'
		e.add_field(name = f'{typ[0]} - {str(len(typ[1]))}', value = st ,inline = False)
	await interaction.response.send_message(embed=e)

@bot.tree.command()
@discord.app_commands.checks.has_any_role(791426367362433066,821787385636585513,790675782569164820)
async def addtime(interaction: discord.Interaction, member: discord.Member, time_string:typing.Optional[str]):
	if not member:
		await interaction.response.send_message(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !", discord.Color.red()))
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
		await interaction.response.send_message(embed=create_small_embed(":warning: Cet utilisateur n'est pas en attente d'entretien !"))
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
	await interaction.response.send_message(embed=create_small_embed('Le message a bien été envoyé à' + member.mention))
	await log.send(embed=create_small_embed(interaction.user.mention + ' à éxécuté la commande addtime pour ' + member.mention))

class testview(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label='Accepter', style=discord.ButtonStyle.green, custom_id='pass')
	async def accept(self,interaction: discord.Interaction, button: discord.ui.Button):
		member = bot.get_user(int(interaction.message.content[2:20]))
		with open('phases.json', 'r') as f:
			phases = json.load(f)
		phases["A faire"][member.id] = str(datetime.now())
		with open('phases.json', 'w') as f:
			json.dump(phases, f, indent=6)
		with open('Interview.json', 'r') as f:
			interviews = json.load(f)
		if str(member.id) in interviews['ET'].keys():
			interviews['ET'].pop(str(member.id))
			with open('Interview.json', 'w') as f:
				json.dump(interviews, f, indent=6)
		try:
			role = interaction.guild.get_role(791066206109958204)
			await member.remove_roles(role, reason=f'Fait par {str(interaction.user)[:16]}')
		except:
			pass
		role1 = interaction.guild.get_role(1011953852427272302)
		await member.add_roles(role1, reason=f'Fait par {str(interaction.user)[:16]}')
		await interaction.response.send_message('Message envoyé')
		try:
			await member.send(embed=discord.Embed(title='Recrutements',description="Bravo à toi pour avoir rankup et réussi ta période de test ! Il ne te manque plus qu'a rendre tes phases a un recruteur dans le <#1011954323271458846>\n**__RAPPEL :__ Il est strictement interdit de parler des phases et de donner le nombre de points que vous avez fait pour rentrer sous peine de sanctions** "))
		except:
			await interaction.response.send_message(f'{member.mention} à désactivé ses mp mais il a quand meme été ajouté aux phases')
			return
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
'''
@bot.tree.command()
async def pati(interaction: discord.Interaction,id:str):
	'''Kick manuellement quelqu'un des phases. Commande réservée à la grande maîtresse suprême.'''
	if interaction.user.id != 790574682294190091:
		await interaction.response.send_message("t'es pas la grande maitresse supreme toi")
		return
	with open('phases.json', 'r') as f:
		phases = json.load(f)
	phases["A faire"].pop(str(id))
	with open('phases.json', 'w') as f:
		json.dump(phases, f, indent=6)
	await interaction.response.send_message('nickel')

@bot.tree.command()
async def listephases(interaction: discord.Interaction):
	'''Voir la liste des gens qui sont encore en phase. Commande réservée à la grande maîtresse suprême.'''
	if interaction.user.id != 790574682294190091:
		await interaction.response.send_message("t'es pas la grande maitresse supreme toi")
		return
	with open('phases.json', 'r') as f:
		phases = json.load(f)
	af = ''
	ff = ''
	for personne in phases["A faire"].keys():
		af+=f'<@{personne}>'
	for personne in phases["Fait"].keys():
		ff+=f'<@{personne}>'
	await interaction.channel.send(f'Fait :\n{ff}')
	if len(af) >= 2000:
		await interaction.channel.send(f'A faire :\n{af[0:1900]}')
		await interaction.channel.send(f'{af[1900:]}')
	else:
		await interaction.channel.send(f'A faire :\n{af}')

@bot.tree.command()
async def pluschef(interaction: discord.Interaction,member:discord.Member):
	'''Ajouter un chef. Commande réservée à la grande maîtresse suprême.'''
	if interaction.user.id != 790574682294190091:
		await interaction.response.send_message("Toi t'es pas blg")
		return
	else:
		role = interaction.guild.get_role(790675782569164820)
		await member.add_roles(role)
		await interaction.response.send_message('Vos désirs sont des ordres grande maitresse supreme')

@bot.tree.command()
async def moinschef(interaction: discord.Interaction,member:discord.Member):
	'''Enlever un chef. Commande réservée à la grande maîtresse suprême.'''
	if interaction.user.id != 790574682294190091:
		await interaction.response.send_message("Toi t'es pas blg")
		return
	else:
		role = interaction.guild.get_role(790675782569164820)
		await member.remove_roles(role)
		await interaction.response.send_message('Vos désirs sont des ordres grande maitresse supreme')

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

class vend(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label="Je veux être notifié pendant les commandes", style=discord.ButtonStyle.green, custom_id='prrol')
	async def prrol(self, interaction: discord.Interaction, button: discord.ui.Button):
		role = interaction.guild.get_role(1016022889780228136)
		if role in interaction.user.roles:
			await interaction.response.send_message('Vous avez déjà le role <@&1016022889780228136>.',ephemeral=True)
			return
		await interaction.user.add_roles(role)
		await interaction.response.send_message('Vous avez bien pris le rôle <@&1016022889780228136>. Bon jeu !',ephemeral=True)
	@discord.ui.button(label="Je ne veux plus être notifié pendant les commandes", style=discord.ButtonStyle.red, custom_id='enrol')
	async def enrol(self, interaction: discord.Interaction, button: discord.ui.Button):
		role = interaction.guild.get_role(1016022889780228136)
		if role not in interaction.user.roles:
			await interaction.response.send_message("Vous n'avez déjà plus le role <@&1016022889780228136>.",ephemeral=True)
			return
		await interaction.user.remove_roles(role)
		await interaction.response.send_message('Vous avez bien retiré le rôle <@&1016022889780228136>. Bon jeu !',ephemeral=True)

class ench(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label="Prendre le rôle enchères", style=discord.ButtonStyle.blurple, custom_id='enchères')
	async def ench(self, interaction: discord.Interaction, button: discord.ui.Button):
		role = interaction.guild.get_role(1015575937787633675)
		if role in interaction.user.roles:
			await interaction.response.send_message('Vous avez déjà le role enchères.',ephemeral=True)
			return
		await interaction.user.add_roles(role)
		await interaction.response.send_message('Vous avez bien pris le role enchères',ephemeral=True)

def get_left_space(str1_, str2_):
	rv = len(str1_) - len(str2_)
	return "".join([' ' for x in range(rv)])

@bot.event
async def on_ready():
	print(f'[{datetime.now().strftime("%Y:%m:%d %H:%M:%S")}]', 'Bot is online!')
	# functions
	effectif.start()
	inactivity.start()
	abs.start()
	candids.start()
	voc.start()
	# prints
	field_placeholder = '+----------------------------------+'
	fields = [f"| Username: {bot.user}", f"| ID: {bot.user.id}", f"| Version: {str(discord.__version__)}"]
	print(field_placeholder)
	for field in fields:
		print(f"{field}{get_left_space(field_placeholder, field)[:-1]}|")
	print(field_placeholder)
	BOT_INVITE_LINK = f'https://discord.com/api/oauth2/authorize?client_id={str(bot.user.id)}&permissions=8&scope=applications.commands%20bot'
	act = discord.Game(name="/help pour voir les commandes auxquelles vous avez accès")
	await bot.change_presence(activity=act)
	await drops()

async def drops():
	await asyncio.sleep(random.randint(7200,86400))
	channel = await bot.fetch_channel(791452088370069525)
	nb = random.randint(10,100)
	await channel.send(embed=create_embed(title='Drop !',description=f'Cliquez en premier sur le bouton pour gagner **{nb}** DP !'),view=drop(nb,1,[]))
	await drops()

class drop(discord.ui.View):
	def __init__(self,money,win,dej):
		super().__init__(timeout=None)
		self.money = money
		self.win = win
		self.dej = dej
	@discord.ui.button(label="Recuperer la money !", style=discord.ButtonStyle.green, custom_id='recupmmoney')
	async def regl(self, interaction: discord.Interaction, button: discord.ui.Button):
		dej = list(self.dej)
		if str(interaction.user.id) in dej:
			interaction.response.send_message(embed=create_small_embed("Vous ne pouvez participer qu'une fois à un drop !"),ephemeral=True)
			return
		if int(str(self.win)) == len(dej)+1:
			await interaction.response.edit_message(embed=create_small_embed(f"Félicitation à {'<@' if len(dej)!=0 else ''}{'>, <@'.join(dej)}{'> et' if len(dej)!=0 else ''} {interaction.user.mention} qui {'ont' if len(dej)!=0 else 'à'} gagné {self.money} DP dans un drop !"),view=None)
		else:
			await interaction.response.edit_message(embed=create_embed(title='Drop !',description=f'''Cliquez en premier sur le bouton pour gagner **{self.money}** DP !\n{self.win} gagnants\nGagnants déjà présents : {', '.join(dej)}{' et' if len(dej)!=0 else ''} {interaction.user.mention}'''),view=drop(self.money,self.win,dej+[str(interaction.user.id)]))
		with open('points.json', 'r') as f:
			pt = json.load(f)
		pt[str(interaction.user.id)] += int(str(self.money))
		with open('points.json', 'w') as f:
			json.dump(pt, f, indent=6)

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def createdrop(interaction: discord.Interaction,channel:discord.TextChannel,prix:int,nb_gagnants:int):
	'''Envoyer manuellement un drop. Commande réservée aux HG.'''
	await channel.send(embed=create_embed(title='Drop !',description=f'Cliquez en premier sur le bouton pour gagner **{prix}** DP !\n{nb_gagnants} gagnants'),view=drop(prix,nb_gagnants,[]))
	await interaction.response.send_message(embed=create_small_embed("Message envoyé !"),ephemeral=True)

async def del_message(message):
	try:
		await message.delete()
	except:
		pass

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def embed(interaction: discord.Interaction,channel:discord.TextChannel,*,message:str):
	'''Envoyer manuellement un embed. Commande réservée aux HG.'''
	await channel.send(embed=create_small_embed(message))
	await interaction.response.send_message(embed=create_small_embed("Message envoyé !"))

def create_embed(title=None, description=None, color=discord.Color.blue()):
	embed = discord.Embed(
		title=title,
		description=description,
		color=color
	)
	embed.timestamp = datetime.utcnow()
	embed.set_footer(text='', icon_url='') #\u200b to remove text
	embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/772451269272928257/937037959516000286/unknown.png')
	return embed

def create_small_embed(description=None, color=discord.Color.blue()):
	embed = discord.Embed(
		description=description,
		color=color
	)
	return embed

@bot.tree.command()
async def editally(interaction: discord.Interaction):
	'''Mettre a jour le #alliances-faction.'''
	await edditally()
	await interaction.response.send_message('Fait')

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

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def prepare(interaction: discord.Interaction,prep:str):
	'''Preparer des trucs. Commande réservée aux HG.'''
	if prep == 'BJ':
		await interaction.channel.send('Pour jouer au blackjack, cliquez sur le bouton', view=blackjackview())
	if prep =='encheres':
		await interaction.channel.send('Pour être notifiés des dèrnières enchères, prennez le role en cliquant sur le bouton',view=ench())
	if prep =='mentionvendeur':
		chan = bot.get_channel(1014650824108019792)
		await chan.send('Pour être notifiés des dèrnières commandes, prennez le role en cliquant sur le bouton',view=vend())
	if prep == 'reg' or prep == 'tout':
		reg = interaction.guild.get_channel(948647836466151434)
		chef = interaction.guild.get_role(790675782569164820)
		rev = interaction.guild.get_role(821787385636585513)
		ally = interaction.guild.get_role(790675785412640768)
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
			" la réaction. Les HG pourront répondre à vos questions."), view=PersistentView())
	if prep == 'RouleR' or prep == 'tout' or prep == 'jeux':
		jeux = bot.get_channel(961592610412167270)
		await jeux.send(embed = create_embed('Roulette Russe','Cliquez sur le bouton ci-dessous pour demarrer une partie de roulette russe et tenter de **__multiplier par 5 votre mise !__**'),view=RouleR())
	if prep == 'rouletteA' or prep == 'tout' or prep == "jeux":
		jeux = bot.get_channel(961592610412167270)
		await jeux.send(embed = create_embed('Roulette Américaine','Cliquez sur le bouton ci-dessous pour demarrer une partie de roulette américaine et tenter de **__multiplier par 36 votre mise !__**'),view=roulette())
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
	if prep == 'tout' or prep == 'market':
		views={"PvP":[PvPView(),819576587846418432],"farming":[farmView(),820047258597720094],"minerais":[mineraisView(),819575989003747400],"alchimiste":[alchimisteView(),819576467284295701],"livres":[livresView(),823930348047695952],"machines":[machinesView(),819577657711657011],"outils":[outilsView(),819576748651839498],"services":[servicesView(),819578071875059712],"pillages":[pillagesView(),819577906761695242],"BC":[basesclaimView(),1012658806406262795]}
		for tu in views.items():
			chan = bot.get_channel(tu[1][1])
			await chan.send(await edimarket(tu[0]), view=tu[1][0])
	await interaction.response.send_message("Tout s'est bien passé !")

async def edimarket(item):
	with open('economie.json', 'r') as f:
		Eco = json.load(f)
	msg = ""
	views={"PvP":[0,100],"farming":[99,200],"minerais":[199,300],"alchimiste":[299,400],"livres":[399,500],"machines":[499,600],"outils":[599,700],"services":[699,800],"pillages":[799,900],"BC":[899,1000]}
	a = views[item][0]
	b = views[item][1]
	for tt in Eco["items"].items():
		if a<int(tt[0])<b: 
			msg += f'{tt[1][2]} {tt[1][0]} -> {tt[1][1]}$/{tt[1][3]}\n'
	return msg

# =========== Effectif ===========

@tasks.loop(seconds = 3600)
async def effectif():
	guild = bot.get_guild(790367917812088864)
	channel = await bot.fetch_channel(937006102653071452)
	role_ids = {'Staff': [1068460789612163072,790675782569164820, 821787385636585513, 790675781789155329, 791426367362433066,1011394095383580843],
				'Membres VIP': [790675782338740235, 790675782364037131, 790675783352975360],
				'Membres +': [790675783549976579, 790675783693500456, 790675784120401932],
				'Membres': [790675784225521734, 791066206437113897, 791066207418712094]}
	message = await channel.fetch_message(937008348597997628)
	_embed = discord.Embed(
		title='Voici notre effectif:',
		description='',
		color=discord.Color.magenta()
	)
	roles = {x: [] for x in role_ids}
	for r_ids_obj in list(role_ids.items()):
		for r_id in r_ids_obj[1]:
			if debug: print(r_id)
			r = guild.get_role(r_id)
			roles[r_ids_obj[0]].append(r)
	if debug: print(roles)
	for roles_obj in list(roles.items()):
		_embed.description += f"\n**{roles_obj[0]} :**\n\n"
		for role in roles_obj[1]:
			v_field = ", ".join([x.mention for x in role.members])
				# _embed.add_field(name=role.name, value=v_field if v_field != '' else ' - ')
			_embed.description += f"{role.mention} : {v_field}\n\n"
	await message.edit(embed=_embed)

# =========== Recrutements ===========

@tasks.loop(seconds=300)
async def candids():
	mydb=mysql.connector.connect(
		host="web49.lws-hosting.com",
		database="cp1873034p22_Candid",
		user = "cp1873034p22_test",
		password="ptmhjXzQx6@YyCe",)
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM Candids")
	myresult = mycursor.fetchall()
	with open('candid.json','r') as f:
		candids = json.load(f)
	if len(myresult) > candids['nb']:
		for i in range(len(myresult) - candids["nb"]):
			guild = bot.get_guild(790367917812088864)
			try:
				member = guild.get_member(int(myresult[-i-1][0]))
				await envoicandid(guild,member,myresult[-i-1][1],myresult[-i-1][2],myresult[-i-1][3],myresult[-i-1][2],myresult[-i-1][4],myresult[-i-1][5],myresult[-i-1][6]+myresult[-i-1][7],myresult[-i-1][8],myresult[-i-1][9],myresult[-i-1][10],myresult[-i-1][11])
			except:
				try:
					user = bot.get_user(myresult[-i-1][0])
					await user.send("Vous n'avez pas rejoint le serveur discord et votre candidature n'a donc pas pu être traitée ! Veuillez rejoindre : https://discord.gg/D9tTGvt7az et recommencer")
				except:
					pass
		candids["nb"] += i+1
		with open('candid.json', 'w') as f:
			json.dump(candids, f, indent=6)

async def envoicandid(guild,auteur:discord.Member,psmc,anps,pbort,prirl,cnmc,cmpl,pqsd,fcrc,objpl,disp):
	msg = f'''**Pseudo discord :**\n{auteur.mention}\n
	**Pseudo Minecraft :**\n{psmc}\n
	**Anciens Pseudos :**\n{anps}\n
	**Problèmes orthographiques :**\n{pbort}\n
	**Présentation IRL :**\n{prirl}\n
	**Comment et depuis quand connaissez vous minecraft ?**\n{cnmc}\n
	**Commant connaissez vous paladium, avancement, prédilections et sanctions**\n{cmpl}\n
	**Pourquoi la SweetDream ?**\n{pqsd}\n
	**Anciennes factions :**\n{fcrc}\n
	**Objectif sur paladium :**\n{objpl}\n
	**Disponibilités :**\n{disp}'''
	rep = guild.get_channel(793804078366851092)
	with open('Candids.json','r') as f:
		candids = json.load(f)
	d = len(candids[2]['data'])
	candids[2]['data'].append({'psmc':str(psmc),'anps':str(anps),'pborb':str(pbort),'prirl':str(prirl),'cnmc':str(cnmc),'pqsd':str(pqsd),'fcrc':str(fcrc),'objpl':str(objpl),'disp':str(disp)})
	with open('Candids.json', 'w') as f:
		json.dump(candids, f, indent=6)
	guild = bot.get_guild(790367917812088864)
	for j in range(math.ceil(len(msg)/2000)):
		if len(msg)<(j+1)*2000:
			await rep.send(embed=discord.Embed(title=f'Candidature {d}',description=msg[j*2000:]),view=candid(auteur))
		else:
			await rep.send(embed=discord.Embed(title=f'Candidature {d}',description=msg[j*2000:(j+1)*2000]))
		role = guild.get_role(986686680146772038)
		await auteur.add_roles(role)
		await auteur.edit(nick=f'[CE] {psmc}')
		try:
			await auteur.send('Nous avons bien reçu votre candidature.')
		except:
			pass

async def acccandid(member:discord.Member,author):
	with open('Interview.json', 'r') as f:
		interviews = json.load(f)
	for type in interviews.items():
		for personne in type[1].keys():
			if str(member.id) == personne:
				return ":warning: Cet utilisateur a deja été accepté !"
	guild = bot.get_guild(790367917812088864)
	_embed = discord.Embed(title = "Recrutements",
							description ="Salut déjà toutes mes Félicitations, ta candidature SweetDream a été accéptée !\nMaintenant tu vas devoir passer un entretien oral. Pour "
							f"le passer il faudra aller dans le <#811651536622977074> et ping un recruteur. Tu auras deux semaine pour venir dans passer ton entretien, si tu n'es pas "
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
		return f"Votre message n'a pas pu etre envoyé car {member.mention} à fermé ses mp"
	role = guild.get_role(790675784901197905)
	role2 = guild.get_role(986686680146772038)
	await member.remove_roles(role2, reason=f'Fait par {str(author)[:16]}')
	await member.add_roles(role, reason=f'Fait par {str(author)[:16]}')
	if str(author.id) in interviews["Recruteur"].keys():
		interviews["Recruteur"][str(author.id)] += 1
	else:
		interviews["Recruteur"][str(author.id)] = 1
	if str(author.id) in interviews["Candids"].keys():
		interviews["Candids"][str(author.id)] += 1
	else:
		interviews["Candids"][str(author.id)] = 1
	with open('Interview.json', 'w') as f:
			json.dump(interviews, f, indent=6)
	log = bot.get_channel(831615469134938112)
	await log.send(embed=create_small_embed(author.mention + ' à éxécuté la commande accept pour ' + member.mention))
	return f'Le message a bien été envoyé à {member.mention}'

async def refcandid(member,author,raison):
	_embed = discord.Embed(title = "Recrutements",
							description =f"""Bonjour, malheureusement ta candidature pour rejoindre la SweetDream n'a pas 
										été acceptée pour la raison suivante {raison}.\nTu pourras retenter ta 
										chance dans 2 semaines. \nCordialement,\nLe Staff Recrutement SweetDream"""
							)
	await member.send(embed=_embed)
	log = bot.get_channel(831615469134938112)
	await member.edit(nick='')
	with open('Interview.json', 'r') as f:
		interviews = json.load(f)
	if str(author.id) in interviews["Candids"].keys():
		interviews["Candids"][str(author.id)] += 1
	else:
		interviews["Candids"][str(author.id)] = 1
	if str(author.id) in interviews["Recruteur"].keys():
		interviews["Recruteur"][str(author.id)] += 1
	else:
		interviews["Recruteur"][str(author.id)] = 1
	with open('Interview.json', 'w') as f:
			json.dump(interviews, f, indent=6)
	guild = bot.get_guild(790367917812088864)
	role = guild.get_role(986686680146772038)
	try:
		await member.remove_roles(role)
	except:
		pass
	await log.send(embed=create_small_embed(f'{author.mention} à éxécuté la commande refuse pour {member.mention} Pour la raison suivante : {raison}'))
	return f'Le message a bien été envoyé à {member.mention}'


class candid(discord.ui.View):
	def __init__(self,auteur):
		super().__init__(timeout=None)
		self.member = auteur
	@discord.ui.button(label='Accepter', style=discord.ButtonStyle.green, custom_id='passer')
	async def accept(self,interaction: discord.Interaction, button: discord.ui.Button):
		await interaction.message.edit(view=None)
		await interaction.response.send_message(embed=create_small_embed(await acccandid(self.member,interaction.user)))
	@discord.ui.button(label='Refuser', style=discord.ButtonStyle.red, custom_id='refuser')
	async def refuse(self,interaction: discord.Interaction, button: discord.ui.Button):
		await interaction.response.send_modal(refusee(self.member,interaction.message))

class refusee(discord.ui.Modal,title="Refus de candidature SD"):
	def __init__(self,mem,msg):
		super().__init__()
		self.qq = discord.ui.TextInput(
			label=f"Pourquoi souhaitez-vous refuser {mem.name}",
			style=discord.TextStyle.paragraph
		)
		self.add_item(self.qq)
		self.msg = msg
		self.mem = mem
	async def on_submit(self, interaction: discord.Interaction) -> None:
		await interaction.response.send_message(embed=create_small_embed(await refcandid(self.mem,interaction.user,self.qq)))
		await self.msg.edit(view=None)


class boutonform(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label='Candidater', style=discord.ButtonStyle.green, custom_id='candidat')
	async def candid(self,interaction: discord.Interaction, button: discord.ui.Button):
		modal = Formulaire()
		await interaction.response.send_modal(modal)

class Formulaire(discord.ui.Modal,title="Formulaire de candidature SD"):
	def __init__(self):
		super().__init__()
		self.pseudo = discord.ui.TextInput(
			label="Pseudo Minecraft",
			placeholder='''Pseudo Minecraft''',
			max_length=16,
		)
		self.add_item(self.pseudo)
		self.anpseudo = discord.ui.TextInput(
			label="Anciens Pseudo",
			placeholder='''Anciens Pseudo'''
		)
		self.add_item(self.anpseudo)

		self.pbo = discord.ui.TextInput(
			label="Avez-vous des problèmes orthographiques ?",
			style=discord.TextStyle.paragraph,
			placeholder='''Dyslexie, Dysorthographie, TDAH, etc.... Cela n'aura aucun impact dans la faction !'''
		)
		self.add_item(self.pbo)
		self.description = discord.ui.TextInput(
			label="Présentez vous IRL",
			style=discord.TextStyle.paragraph,
			placeholder="N'hésite pas à parler de toi, nous voulons en savoir davantage sur toi. Au moins 450 caractères",
			min_length=450,
		)
		self.add_item(self.description)
		self.quest = discord.ui.TextInput(
			label="Questions Minecraft",
			style=discord.TextStyle.paragraph,
			placeholder="Comment et depuis quand connaissez vous Minecraft. Quels sont vos domaines de prédilection",
		)
		self.add_item(self.quest)
	async def on_submit(self, interaction: discord.Interaction) -> None:
		data = [self.pseudo,self.anpseudo,self.pbo,self.description,self.quest]
		await interaction.response.send_message('''___***Attention ! Votre candidature n'est pas encore envoyée ! Pour finir la procédure veuillez finir le deuxieme questionnaire***___''',ephemeral=True,view=boutonform2(data))

class boutonform2(discord.ui.View):
	def __init__(self,data:str):
		super().__init__(timeout=None)
		self.data = data
	@discord.ui.button(label='Finir ma candidature', style=discord.ButtonStyle.green, custom_id='candidat2')
	async def candida(self,interaction: discord.Interaction, button: discord.ui.Button):
		modal = Formulaire2(self.data)
		await interaction.response.send_modal(modal)

class Formulaire2(discord.ui.Modal,title="Formulaire de candidature SD"):
	def __init__(self,data:str):
		super().__init__()
		self.av = discord.ui.TextInput(
			label="Questions paladium",
			style=discord.TextStyle.paragraph,
			placeholder="Comment connaissez vous paladium. Quel est votre avancement en jeu ? Avez vous eu des sanctions ?",
		)
		self.add_item(self.av)
		self.sd = discord.ui.TextInput(
			label="Questions SD",
			style=discord.TextStyle.paragraph,
			placeholder="Pourquoi voulez vous rejoindre une faction et en particulier la SD. Que veut dire Tryhard pour vous?",
		)
		self.add_item(self.sd)
		self.tryh = discord.ui.TextInput(
			label="Avez vous eu des factions précédemment ?",
			style=discord.TextStyle.paragraph,
			placeholder="""Si oui lesquelles ? Pourquoi avez vous rejoint ses factions ? Et pourquoi les avez vous quittée(s) ?""",
		)
		self.add_item(self.tryh)
		self.obj = discord.ui.TextInput(
			label="Objectifs et Occupations",
			style=discord.TextStyle.paragraph,
			placeholder="Avez vous des objectifs sur Paladium ? Qu'est ce que vous voulez faire sur Paladium ?",
		)
		self.add_item(self.obj)
		self.dis = discord.ui.TextInput(
			label="Quelles sont vos disponibilités ?",
			placeholder="Quelles sont vos disponibilités ?",
		)
		self.add_item(self.dis)
		self.data = data
	async def on_submit(self, interaction: discord.Interaction) -> None:
		await interaction.response.defer()
		await envoicandid(interaction.guild,interaction.user,self.data[0],self.data[1],self.data[2],self.data[3],self.data[4],self.av,self.sd,self.tryh,self.obj,self.dis)

@bot.tree.command()
async def sendrecru(interaction: discord.Interaction):
	'''Envoyer le formulaire de candidature SD.'''
	await interaction.response.send_message('Pour candidater appuyez sur le bouton ci-dessous',view=boutonform())

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def listerecru(interaction: discord.Interaction):
	'''Voir qui fait quoi chez les recruteurs. Commande réservée aux HG.'''
	with open('Interview.json', 'r') as f:
		interviews = json.load(f)
		msg = '**Total :**\n'
	for rec in sorted(interviews["Recruteur"], key=lambda recru: interviews["Recruteur"][recru],reverse=True):
		msg += f'<@{rec}> - {interviews["Recruteur"][rec]}\n'

	msg += '\n**Candidatures :**\n'
	for rec in sorted(interviews["Candids"], key=lambda recru: interviews["Candids"][recru],reverse=True):
		msg += f'<@{rec}> - {interviews["Candids"][rec]}\n'

	msg += '\n**Entretiens :**\n'
	for rec in sorted(interviews["Oral"], key=lambda recru: interviews["Oral"][recru],reverse=True):
		msg += f'<@{rec}> - {interviews["Oral"][rec]}\n'

	msg += '\n**Phases :**\n'
	for rec in sorted(interviews["Phases"], key=lambda recru: interviews["Phases"][recru],reverse=True):
		msg += f'<@{rec}> - {interviews["Phases"][rec]}'

	await interaction.response.send_message(embed=create_small_embed(msg))

@bot.tree.command()
@discord.app_commands.checks.has_any_role(791426367362433066,821787385636585513,790675782569164820)
async def refuse(interaction: discord.Interaction, member: discord.Member, *, raison:str):
	'''Refuser manuellement une candidature. Commande réservée à la grande maîtresse suprême.'''
	if interaction.user.id != 790574682294190091:
		await interaction.response.send_message(embed=create_small_embed('Cette commande est obsolete, merci de mp <@790574682294190091> pour plus de renseignements'))
		return
	if not member:
		await interaction.response.send_message(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !",discord.Color.red()))
		return
	log = bot.get_channel(831615469134938112)
	await interaction.response.send_message(embed=create_small_embed('Le message a bien été envoyé à' + member.mention))
	await log.send(await refcandid(member,interaction.user,raison))

@bot.tree.command()
@discord.app_commands.checks.has_any_role(791426367362433066,821787385636585513,790675782569164820,1068460789612163072)
async def accept(interaction: discord.Interaction, member: discord.Member):
	'''Accepter manuellement une candidature. Commande réservée à la grande maîtresse suprême.'''
	if interaction.user.id != 790574682294190091:
		await interaction.response.send_message(embed=create_small_embed('Cette commande est obsolete, merci de mp <@790574682294190091> pour plus de renseignements'))
		return
	if not member:
		await interaction.response.send_message(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !", discord.Color.red()))
		return
	await interaction.response.send_message(embed=create_small_embed(await acccandid(member,interaction.user)))

@tasks.loop(seconds = 3600)
async def inactivity():
	with open('Interview.json', 'r') as f:
		interviews = json.load(f)
	guild = bot.get_guild(790367917812088864)
	dtn = datetime.now()
	mem = []
	for user_id in interviews["Dates"].items():
		if int(str(dtn)[5:7]) > int(str(user_id[1])[5:7]) or int(str(dtn)[8:10]) >= int(str(user_id[1])[8:10]) and int(str(dtn)[5:7]) >= int(str(user_id[1])[5:7]):
			user = await bot.fetch_user(user_id[0])
			try:
				_embed = discord.Embed(title="Recrutements",
									   description="Bonjour, Tu avais 2 semaine pour faire ton entretien oral pour rejoindre la SweetDream mais tu ne l'as pas passé. Merci de repondre ici meme (au bot "
													"SweetDream). de dire pourquoi tu ne peux pas passer ton oral.\nCordialement,\nLe Staff Recrutement SweetDream.")
				await user.send(embed=_embed)
				interviews['Wait'][user_id[0]] = str(datetime.utcnow() + timedelta(days=2))
			except:
				pass
			mem.append(user_id[0])
	for element in mem:
		interviews['Dates'].pop(element)
	memb = []
	for user_id in list(interviews["Wait"].items()):
		if int(str(dtn)[5:7]) > int(str(user_id[1])[5:7]) or int(str(dtn)[8:10]) >= int(str(user_id[1])[8:10]) and int(str(dtn)[5:7]) >= int(str(user_id[1])[5:7]):
			try:
				user = await guild.fetch_member(user_id[0])
				_embed2 = discord.Embed(title="Recrutements",
										description="Bonjour, \ntu n'as pas répondu assez rapidement au bot et ta candidature a été annulée. Tu peux toujours tenter d'en refaire "
										"une.\n A bientot,\nLe staff Recrutement SweetDream"
											)
				await user.send(embed=_embed2)
				role = guild.get_role(790675784901197905)
				await user.remove_roles(role)
			except:
				pass
			memb.append(user_id[0])
	for element in memb:
		interviews['Wait'].pop(element)
	guild = bot.get_guild(790367917812088864)
	fin = guild.get_channel(937312061833240586)
	memi = []
	for user_id in list(interviews["ET"].items()):
		if int(str(dtn)[5:7]) > int(str(user_id[1])[5:7]) or int(str(dtn)[8:10]) >= int(str(user_id[1])[8:10]) and int(str(dtn)[5:7]) >= int(str(user_id[1])[5:7]):
			user = await bot.fetch_user(user_id[0])
			if user==None:
				memi.append(user_id[0])
			else:
				await fin.send(f'{user.mention} a fini sa periode de test.?')# Voulez vous le faire passer   ,view=testview()
				memi.append(user_id[0])
	for element in memi:
		interviews['ET'].pop(element)
	if len(mem)+len(memb)+len(memi)>0:
		with open('Interview.json', 'w') as f:
			json.dump(interviews, f, indent=6)

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def debutphases(interaction: discord.Interaction, member: discord.Member):
	'''Commencer manuellement les phases. Commande réservée aux HG.'''
	with open('phases.json', 'r') as f:
		phases = json.load(f)
	phases["A faire"][member.id] = str(datetime.now())
	with open('phases.json', 'w') as f:
		json.dump(phases, f, indent=6)
	with open('Interview.json', 'r') as f:
		interviews = json.load(f)
	if str(member.id) in interviews['ET'].keys():
		interviews['ET'].pop(str(member.id))
		with open('Interview.json', 'w') as f:
			json.dump(interviews, f, indent=6)
	try:
		role = interaction.guild.get_role(791066206109958204)
		await member.remove_roles(role, reason=f'Fait par {str(interaction.user)[:16]}')
	except:
		pass
	role1 = interaction.guild.get_role(1011953852427272302)
	await member.add_roles(role1, reason=f'Fait par {str(interaction.user)[:16]}')
	try:
		await member.send(embed=discord.Embed(title='Recrutements',description="Bravo à toi pour avoir rankup et réussi ta période de test ! Il ne te manque plus qu'a rendre tes phases a un recruteur dans le <#1011954323271458846>\n**__RAPPEL :__ Il est strictement interdit de parler des phases et de donner le nombre de points que vous avez fait pour rentrer sous peine de sanctions** "))
	except:
		await interaction.response.send_message(f'{member.mention} à désactivé ses mp mais il a quand meme été ajouté aux phases')
		return
	await interaction.response.send_message('Message envoyé')

@bot.tree.command()
@discord.app_commands.checks.has_any_role(791426367362433066,821787385636585513,790675782569164820)
async def oralyes(interaction: discord.Interaction, member: discord.Member):
	'''Accepter un oral. Commande réservée aux recruteurs.'''
	with open('Interview.json', 'r') as f:
		interviews = json.load(f)
	if not member:
		await interaction.response.send_message(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !", discord.Color.red()))
		return
	_embed = discord.Embed(title = "Recrutements",
							description ="Félicitation, tu viens de passer ton entretien oral et tu as réussi !\nTu es désormais en test dans la faction. Pendant cette periode de "
							"test nous allons t'évaluer sur ton activité (en jeu, en vocal, écrit) et sur ta capacité à farmer.\nAfin de verifier ton activité tu devra farmer un maximum de points parmis le catalogue suivant :\n**Farmer :**\n- Graines de paladium -> 25 points\n- Graine d'endium -> 500 points\n- Bouteilles de farmer (1000xp) -> 100 points\n\n**Hunter :**\n- Spawner T4 witch -> 1.000.000 points\n- Autre spawner T4 -> 250.000 points\n- Empty spawner -> 6.500 points\n- Broken spawners -> 4.000 points\n\n**Miner :**\n- Findium -> 60 points\n- Minerais d'améthyste -> 35 points\n- Minerais de titane -> 35 points\n- Minerais de paladium -> 80 points\n- Cobblebreaker -> 100 points\n- Cobblestone -> 0.125 points\n\n**Alchimiste :**\n- Lightning potion -> 2.000 points (30 max par personne)\n- Extractor -> 200 points\n- Fleurs -> 50 points/stack\n- Harpagophytum -> 1.000 points\n\n**BC :**\n- Obsidienne Normale -> 5 points\n- Poisonned Obsidian -> 15 points\n- Boom Obsidian -> 25 points\n- Mega Boom Obsidian -> 300 points\n- Big obsidian -> 200 points\n\n**Ressources :**\n- Lingot d'amethyste : 17 points\n- Lingot de titane : 17 points\n- 1$ -> 0,2 point\n- lingot de pala : 40 points\n- Nugget en endium : 75.000 points\n\nSi nous considérons que tu es suffisament actif pour entrer tu pourras nous montrer tout ce que tu as farmé. Si c'est suffisant tu pourras nous le donner et entrer dirrectement dans la faction sinon tu n'auras plus qu'une semaine pour farmer un nombre d'une ressource choisie par toi et les recruteurs' Nous t'invitons donc rester présent et actif.\nEn cas de problèmes tu peux"
							" envoyer un message a un recruteur afin de signaler une absence.\nCordialement,\nLe Staff Recrutement SweetDream")
	for type in interviews.items():
		for personne in type[1].keys():
			if str(member.id) == personne:
				a = str(member.id)
				b = type[0]
	try:
		interviews[b].pop(a)
	except:
		await interaction.response.send_message(embed=create_small_embed(":warning: Cet utilisateur n'est pas en attente d'entretien !"))
		return
	interviews["ET"][member.id] = str((datetime.utcnow() + timedelta(days=30)))
	with open('Interview.json', 'w') as f:
		json.dump(interviews, f, indent=6)
	try:
		await member.edit(nick=f'[ET] {member.nick[5:]}')
	except:
		await member.edit(nick=f'[ET] {member.name}')
	if str(interaction.user.id) in interviews["Recruteur"].keys():
		interviews["Recruteur"][str(interaction.user.id)] += 1
	else:
		interviews["Recruteur"][str(interaction.user.id)] = 1
	if str(interaction.user.id) in interviews["Oral"].keys():
		interviews["Oral"][str(interaction.user.id)] += 1
	else:
		interviews["Oral"][str(interaction.user.id)] = 1
	role = interaction.guild.get_role(790675784901197905)
	role1 = interaction.guild.get_role(791066206109958204)
	await member.remove_roles(role, reason=f'Fait par {str(interaction.user)[:16]}')
	await member.add_roles(role1, reason=f'Fait par {str(interaction.user)[:16]}')
	log = bot.get_channel(831615469134938112)
	await member.send(embed=_embed)
	await interaction.response.send_message(embed=create_small_embed('Le message a bien été envoyé à' + member.mention))
	await log.send(embed=create_small_embed(interaction.user.mention + ' à éxécuté la commande oralyes pour ' + member.mention))

@bot.tree.command()
@discord.app_commands.checks.has_any_role(791426367362433066,821787385636585513,790675782569164820)
async def oralno(interaction: discord.Interaction, member: discord.Member):
	'''Refuser un oral. Commande réservée aux recruteurs.'''
	if not member:
		await interaction.response.send_message(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !", discord.Color.red()))
		return
	with open('Interview.json', 'r') as f:
		interviews = json.load(f)
	guild = interaction.guild
	_embed = discord.Embed(title = "Recrutements",
							description ="Bonjour,\nMalheureusement ton entretien oral n'a pas été accepté mais tu "
										 "pourras refaire une candidature écrite dans 2 semaines. \nCordialement,\n"
										 "Le staff Recrutement SweetDream."
							)
	role = guild.get_role(790675784901197905)
	await member.remove_roles(role, reason=f'Fait par {str(interaction.user)[:16]}')
	for type in interviews.items():
		for personne in type[1].keys():
			if str(member.id) == personne:
				a = str(member.id)
				b = type[0]
	try:
		interviews[b].pop(a)
	except:
		await interaction.response.send_message(embed=create_small_embed(":warning: Cet utilisateur n'est pas en attente d'entretien !"))
		return
	with open('Interview.json', 'w') as f:
		json.dump(interviews, f, indent=6)
	await member.edit(nick=f'')
	await member.send(embed=_embed)
	if str(interaction.user.id) in interviews["Recruteur"].keys():
		interviews["Recruteur"][str(interaction.user.id)] += 1
	else:
		interviews["Recruteur"][str(interaction.user.id)] = 1
	if str(interaction.user.id) in interviews["Oral"].keys():
		interviews["Oral"][str(interaction.user.id)] += 1
	else:
		interviews["Oral"][str(interaction.user.id)] = 1
	log = bot.get_channel(831615469134938112)
	ban = bot.get_channel(801163722650419200)
	await interaction.response.send_message(embed=create_small_embed('Le message a bien été envoyé à' + member.mention))
	await log.send(embed=create_small_embed(interaction.user.mention + ' à éxécuté la commande oralno pour ' + member.mention))
	await ban.send(embed=create_small_embed(member.mention + 'est banni pendant deux semaines car iel à été refusé.e en entretien',discord.Color.red()))

@bot.tree.command()
@discord.app_commands.checks.has_any_role(791426367362433066,821787385636585513,790675782569164820)
async def finphases(interaction: discord.Interaction, member: discord.Member,*,rendu:str):
	'''Terminer des phases. Indiquer dans "rendu" ce que la personne à donné. Commande réservée aux recruteurs.'''
	with open('Interview.json', 'r') as f:
		interviews = json.load(f)
	guild = interaction.guild
	_embed = discord.Embed(title = "Recrutements",
							description ="Bravo, tu es désormais un.e membre officiel de la faction ! Tu as maintenant accès aux "
										 "salons de faction. N'hésites pas a être actif.ve en vocal et en écrit pour "
										 "monter en grade et avoir accès a plus de bases ;-)"
							)
	if str(interaction.user.id) in interviews["Recruteur"].keys():
		interviews["Recruteur"][str(interaction.user.id)] += 1
	else:
		interviews["Recruteur"][str(interaction.user.id)] = 1
	if str(interaction.user.id) in interviews["Phases"].keys():
		interviews["Phases"][str(interaction.user.id)] += 1
	else:
		interviews["Phases"][str(interaction.user.id)] = 1
	with open('Interview.json', 'w') as f:
			json.dump(interviews, f, indent=6)
	with open('phases.json', 'r') as f:
		phases = json.load(f)
	phases["A faire"].pop(str(member.id))
	phases["Fait"][member.id] = [str(datetime.now()),rendu]
	with open('phases.json', 'w') as f:
		json.dump(phases, f, indent=6)
	await member.send(embed=_embed)
	try:
		await member.edit(nick=f'[SD] {member.nick[5:]}')
	except:
		await member.edit(nick=f'[SD] {member.name}')
	role = guild.get_role(1011953852427272302)
	await member.remove_roles(role, reason=f'Fait par {str(interaction.user)[:16]}')
	role1 = guild.get_role(791066207418712094)
	await member.add_roles(role1, reason=f'Fait par {str(interaction.user)[:16]}')
	embed_ = create_small_embed("Bienvenue à "+member.mention+" dans la faction !",discord.Color.gold())
	rankup = guild.get_channel(791991289007570974)
	await rankup.send(embed=embed_)
	log = bot.get_channel(831615469134938112)
	await interaction.response.send_message(embed=create_small_embed('Le message a bien été envoyé à ' + member.mention))
	await log.send(embed=create_small_embed(interaction.user.mention + ' à éxécuté la commande finphases pour ' + member.mention))

@bot.tree.command()
@discord.app_commands.checks.has_any_role(791426367362433066,821787385636585513,790675782569164820)
async def kickphases(interaction: discord.Interaction, member: discord.User, *, raison:str):
	'''Kick quelqu'un des phases. Commande réservée aux recruteurs.'''
	with open('Interview.json', 'r') as f:
		interviews = json.load(f)
	guild = interaction.guild
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
		await interaction.channel.send(embed=create_small_embed(":warning: Cet utilisateur n'est pas en attente d'entretien ou a fini sa limite de temps"))
	if str(interaction.user.id) in interviews["Recruteur"].keys():
		interviews["Recruteur"][str(interaction.user.id)] += 1
	else:
		interviews["Recruteur"][str(interaction.user.id)] = 1
	if str(interaction.user.id) in interviews["Candids"].keys():
		interviews["Phases"][str(interaction.user.id)] += 1
	else:
		interviews["Phases"][str(interaction.user.id)] = 1
	with open('Interview.json', 'w') as f:
		json.dump(interviews, f, indent=6)
	log = bot.get_channel(831615469134938112)
	ban = bot.get_channel(801163722650419200)
	try:
		with open('phases.json', 'r') as f:
			phases = json.load(f)
		phases["A faire"].pop(str(member.id))
		with open('phases.json', 'w') as f:
			json.dump(phases, f, indent=6)
	except:
		await interaction.channel.send(embed=create_small_embed(":warning: Cet utilisateur n'est pas en train de faire les phases"))
	try:
		await member.send(embed=_embed)
		await interaction.response.send_message(embed=create_small_embed('Le message a bien été envoyé à ' + member.mention))
		member = guild.get_member(member.id)
		role = guild.get_role(790675784901197905)
		await member.remove_roles(role, reason=f'Fait par {str(interaction.user)[:16]}')
		role1 = guild.get_role(791066206109958204)
		await member.remove_roles(role1, reason=f'Fait par {str(interaction.user)[:16]}')
		role1 = guild.get_role(1011953852427272302)
		await member.remove_roles(role1, reason=f'Fait par {str(interaction.user)[:16]}')
		await member.edit(nick="")
	except:
		await interaction.response.send_message(embed=create_small_embed("La commande a été prise en compte mais le message n'a pas pu être envoyé car la personne a quitté le serveur"))
	await log.send(embed=create_small_embed(interaction.user.mention + ' à éxécuté la commande kickphases pour ' + member.mention))
	await ban.send(embed=create_small_embed(member.mention + ' est banni.e pendant deux semaines car iel à été kick des phases ',discord.Color.red()))

# =========== Staff ===========

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def lock(interaction: discord.Interaction):
	'''Fermer un salon. Commande réservée aux HG.'''
	await interaction.channel.edit(overwrites={interaction.guild.default_role: discord.PermissionOverwrite(send_messages=False,)})
	await interaction.response.send_message(create_small_embed('''Ce channel à été **lock** par un membre du staff. Vous ne pouvez donc plus y parler jusqu'a ce qu'il soit unlock.\nIl peut avoir été lock pour plusieurs raisons mais généralement il s'agit d'une prévention (afin d'éviter que la discussion actuelle ne dégénère).\nMerci de votre comprehension,\nLe staff Sweetdream'''))

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def unlock(interaction: discord.Interaction):
	'''Rouvrir un salon. Commande réservée aux HG.'''
	await interaction.channel.edit(overwrites={interaction.guild.default_role: discord.PermissionOverwrite(send_messages=None,)})
	await interaction.response.send_message(create_small_embed('''Le channel à été unlock'''))


@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def warn(interaction: discord.Interaction, member : discord.Member, *, raison:str):
	'''Warn un membre. Commande réservée aux HG.'''
	if not member:
		await interaction.response.send_message(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !",
												 discord.Color.red()))
		return
	_embed = discord.Embed(title="Warn",
						   description="Bonjour,\nTu as été averti.e pour la raison suivante : "+raison)
	with open('warnblame.json', 'r') as f:
		wb = json.load(f)
	try:
		wb['warns'][str(member.id)].append([raison,str(datetime.now())])
	except:
		wb['warns'][str(member.id)] = [[raison,str(datetime.now())]]
	with open('warnblame.json', 'w') as f:
		json.dump(wb, f, indent=6)
	await member.send(embed=_embed)
	log = bot.get_channel(944296375007477811)
	await interaction.response.send_message(embed=create_small_embed('Le message a bien été envoyé à' + member.mention))
	await log.send(embed=create_small_embed(member.mention+ ' à été warn par ' +interaction.user.mention+" pour "+raison))

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def unwarn(interaction: discord.Interaction, member : discord.Member, nbw:typing.Optional[int], *, raison:typing.Optional[str]):
	'''Enlver un warn. Mettre dans nbw le numéro du warn à retirer (vous pouvez voir avec /sanctions). Commande réservée aux HG.'''
	if member.id == interaction.user.id:
		await interaction.response.send_message(embed=create_small_embed("Tu peux pas t'unwarn sale vilain",discord.Color.red()))
		return
	try:
		nbw=int(nbw)-1
	except:
		if nbw != None:
			raison = str(nbw)+raison
	_embed = discord.Embed(title="Unwarn",
						   description="Bonjour,\nTon warn a été retiré pour la raison suivante : "+raison)
	with open('warnblame.json', 'r') as f:
		wb = json.load(f)
	try:
		nombre = len(wb['warns'][str(member.id)])
		if nombre == 1:
			wb['warns'].pop(str(member.id))
		else:
			if nbw==None:
				await interaction.response.send_message(embed=create_small_embed('Ce membre a plusieurs sanction, merci de préciser laquelle vous souhaitez retirer'))
				return
			wb['warns'][str(member.id)].pop(nbw)
	except:
		await interaction.response.send_message(embed=create_small_embed("Ce membre n'a aucun warn a retirer !"))
		return
	with open('warnblame.json', 'w') as f:
		json.dump(wb, f, indent=6)
	await member.send(embed=_embed)
	log = bot.get_channel(944296375007477811)
	await interaction.response.send_message(embed=create_small_embed('Le message a bien été envoyé à' + member.mention))
	await log.send(embed=create_small_embed(member.mention+ ' à été unwarn par ' +interaction.user.mention+" pour "+raison))

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def blame(interaction: discord.Interaction, member : discord.Member, *, raison:str):
	'''Mettre un blame à un membre. Commande réservée aux HG.'''
	if not member:
		await interaction.response.send_message(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !",
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
															"faction pour un mois**")
	with open('warnblame.json', 'r') as f:
		wb = json.load(f)
	try:
		wb['blames'][str(member.id)].append([raison,str(datetime.now())])
	except:
		wb['blames'][str(member.id)] = [[raison,str(datetime.now())]]
	with open('warnblame.json', 'w') as f:
		json.dump(wb, f, indent=6)
	await member.send(embed=_embed)
	log = bot.get_channel(944296375007477811)
	await interaction.response.send_message(embed=create_small_embed('Le message a bien été envoyé à' + member.mention))
	await log.send(embed=create_small_embed(member.mention+ ' à été blamé par ' +interaction.user.mention+" pour "+raison))

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def unblame(interaction: discord.Interaction, member : discord.Member, nbw:typing.Optional[int], *, raison:typing.Optional[str]):
	'''Enlver un blame. Mettre dans nbw le numéro du warn à retirer (vous pouvez voir avec /sanctions). Commande réservée aux HG.'''
	if member.id == interaction.user.id:
		await interaction.response.send_message(embed=create_small_embed("Tu peux pas t'unblame sale vilain",discord.Color.red()))
		return
	try:
		nbw=int(nbw)-1
	except:
		if nbw != None:
			raison = str(nbw)+raison
	_embed = discord.Embed(title="Blame",description="Bonjour,\nTon warn a été retiré pour la raison suivante : "+raison)
	with open('warnblame.json', 'r') as f:
		wb = json.load(f)
	try:
		nombre = len(wb['blames'][str(member.id)])
		if nombre == 1:
			wb['blames'].pop(str(member.id))
		else:
			if nbw==None:
				await interaction.response.send_message(embed=create_small_embed('Ce membre a plusieurs sanction, merci de préciser laquelle vous souhaitez retirer'))
				return
			wb['blames'][str(member.id)].pop(nbw)
	except:
		await interaction.response.send_message(embed=create_small_embed("Ce membre n'a aucun warn a retirer !"))
		return
	with open('warnblame.json', 'w') as f:
		json.dump(wb, f, indent=6)
	await member.send(embed=_embed)
	log = bot.get_channel(944296375007477811)
	await interaction.response.send_message(embed=create_small_embed('Le message a bien été envoyé à' + member.mention))
	await log.send(embed=create_small_embed(member.mention+ ' à été unblame par ' +interaction.user.mention+" pour "+raison))

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def rankup(interaction: discord.Interaction, member:discord.Member):
	'''Rankup un membre. Commande réservée aux HG.'''
	guild = interaction.guild
	Roles = {9:790675782338740235,8:790675782364037131,7:790675783352975360,6:790675783549976579,5:790675783693500456,
			 4:790675784120401932,3:790675784225521734,2:791066206437113897, 1:791066207418712094}
	for x in Roles.items():
		rol = guild.get_role(x[1])
		if rol in member.roles:
			role = x[0]
	if not role:
		await interaction.response.send_message(embed=create_small_embed(":warning: Ce membre n'existe pas ou ne peux pas etre rankup !",
												 discord.Color.red()))
		return
	role1 = guild.get_role(Roles[role])
	await member.remove_roles(role1, reason=f'Fait par {str(interaction.user)[:16]}')
	role1 = guild.get_role(Roles[role+1])
	await member.add_roles(role1, reason=f'Fait par {str(interaction.user)[:16]}')
	embed_ = create_small_embed("Félicitation à "+member.mention+" qui passe "+role1.mention+" !",discord.Color.gold())
	rankup = guild.get_channel(791991289007570974)
	await rankup.send(embed=embed_)
	await member.send("Félicitation à toi, tu passes "+role1.name+" !")
	await interaction.response.send_message("Le rankup a bien été effectué")

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def derank(interaction: discord.Interaction, member:discord.Member,*,raison:typing.Optional[str]):
	'''Dérank un membre. Commande réservée aux HG.'''
	if not member:
		await interaction.response.send_message(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !",
												 discord.Color.red()))
		return
	guild = interaction.guild
	Roles = {9:790675782338740235,8:790675782364037131,7:790675783352975360,6:790675783549976579,5:790675783693500456,
			 4:790675784120401932,3:790675784225521734,2:791066206437113897, 1:791066207418712094}
	for x in Roles.items():
		rol = guild.get_role(x[1])
		if rol in member.roles:
			role = x[0]
	if not role:
		await interaction.response.send_message(embed=create_small_embed(":warning: Ce membre n'existe pas ou ne peux pas etre rankup !",
												 discord.Color.red()))
		return
	role1 = guild.get_role(Roles[role])
	await member.remove_roles(role1, reason=f'Fait par {str(interaction.user)[:16]}')
	role1 = guild.get_role(Roles[role-1])
	await member.add_roles(role1, reason=f'Fait par {str(interaction.user)[:16]}')
	await member.send("Tu viens de te faire dérank pour la raison suivante : "+raison)
	log = bot.get_channel(944296375007477811)
	await log.send(embed=create_small_embed(member.mention + ' à été unblame par ' + interaction.user.mention + " pour " + raison))
	await interaction.response.send_message("Le derank a bien été effectué")

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def ban(interaction: discord.Interaction, member:discord.Member,*,raison:str):
	'''Bannir quelqu'un (oui Dawen on peut meme ban les autres HG). Commande réservée aux HG.'''
	if member.id == 790574682294190091:
		await interaction.response.send_message('Vous ne pouvez pas ban la grande maitresse suprème !')
		try:
			interaction.user.send('Vous avez été banni pour avoir tenté de bannir la grande maitresse suprème')
		except:
			pass
		await interaction.guild.ban(interaction.user,reason='Tente de ban la grande maitresse supreme')
	if not member:
		await interaction.response.send_message(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !",discord.Color.red()))
		return
	guild = interaction.guild
	embed_ = discord.Embed(
		description=f"Vous avez été banni de la SweetDream pour la raison suivante : {raison}",
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
	await log.send(embed=create_small_embed(member.mention + ' à été ban par ' + interaction.user.mention + " pour " + raison))
	await interaction.response.send_message(embed=create_small_embed(message))

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def unban(interaction: discord.Interaction, member:discord.User,*,raison:str):
	'''Débannir quelqu'un. Commande réservée aux HG.'''
	if member.id == interaction.user.id:
		await interaction.response.send_message(embed=create_small_embed("Tu peux pas t'unwarn sale vilain",discord.Color.red()))
		return
	guild = interaction.guild
	await guild.unban(member,reason=raison)
	log = bot.get_channel(944296375007477811)
	await log.send(embed=create_small_embed(member.mention + ' à été unban par ' + interaction.user.mention + " pour " + raison))
	await interaction.response.send_message(embed=create_small_embed(member.mention+"à bien été déban"))

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def sanctions(interaction: discord.Interaction, member: discord.Member):
	'''Consulter les sanctions d'un membre. Commande réservée aux HG.'''
	if not member:
		await interaction.response.send_message(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !",discord.Color.red()))
		return
	with open('warnblame.json', 'r') as f:
		wb = json.load(f)
	with open('phases.json', 'r') as f:
		ph = json.load(f)
	msg = f"Mention : {member.mention} ({member.nick})\nA rejoint le serveur le {str(member.joined_at)[8:10]}/{str(member.joined_at)[5:7]}/{str(member.joined_at)[0:4]}"
	if str(member.id) in ph["Fait"]:
		msg += f"\nMembre de la fac depuis le {ph['Fait'][str(member.id)][0][8:10]}/{ph['Fait'][str(member.id)][0][5:7]}/{ph['Fait'][str(member.id)][0][0:4]}"
	for element in wb.keys():
		msg += f"\n\n**{element} :**"
		try:
			for i in range(len(wb[element][str(member.id)])):
				msg += f"\n[{str(i+1)}] {wb[element][str(member.id)][i][0]} - *{wb[element][str(member.id)][i][1][8:10]}/{wb[element][str(member.id)][i][1][5:7]}/{wb[element][str(member.id)][i][1][0:4]}*"
		except:
			msg+=f"\nAucun {element}"
	embed = discord.Embed(title=member.name,description=msg)
	embed.set_thumbnail(url=member.avatar.url)
	await interaction.response.send_message(embed=embed)

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def addinfo(interaction: discord.Interaction, member: discord.Member,positive_negative_neutre:str,*,info:str):
	'''Ajouter une info invisible sur un membre. Commande réservée aux HG.'''
	if not member:
		await interaction.response.send_message(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !",discord.Color.red()))
		return
	with open('warnblame.json', 'r') as f:
		wb = json.load(f)
	if positive_negative_neutre != "negative" and positive_negative_neutre != "positive" and positive_negative_neutre != "neutre":
		await interaction.response.send_message("Il faut écrire `positive`, `negative` ou `neutre` patate")
		return
	if str(member.id) in wb[positive_negative_neutre].keys():
		wb[positive_negative_neutre][str(member.id)].append([info,str(datetime.now())])
	else:
		wb[positive_negative_neutre][str(member.id)] = [[info,str(datetime.now())]]
	with open('warnblame.json', 'w') as f:
		json.dump(wb, f, indent=6)
	await interaction.response.send_message(embed=create_small_embed("l'info à été enregistrée"))

# =========== Tickets ===========

class PersistentView(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label='Ouvrir un ticket', style=discord.ButtonStyle.green, custom_id='ticket')
	async def ticket(self,interaction: discord.Interaction, button: discord.ui.Button):
		with open('tickets.json', 'r') as f:
			ticket = json.load(f)
		for x in list(ticket['auteurs'].items()):
			if not interaction.permissions.administrator:
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
		if not interaction.permissions.administrator:
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

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def close(interaction: discord.Interaction):
	'''Fermer un ticket. Commande réservée aux HG.'''
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

# =========== Economie ===========

@bot.tree.command()
async def creercompte(interaction: discord.Interaction):
	'''Se créer un compte'''
	with open('economie.json', 'r') as f:
		Eco = json.load(f)
	try:
		await interaction.response.send_message(embed=create_small_embed(":warning: Vous avez déjà ouvert un compte avec "+str(Eco["Comptes"][str(interaction.user.id)])+"$ dessus !",discord.Color.red()))
	except:
		await compte(interaction.user)
		await interaction.response.send_message("Votre compte à été crée")

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

@bot.tree.command()
async def money(interaction: discord.Interaction):
	'''Consultez votre money'''
	await compte(interaction.user)
	with open('economie.json', 'r') as f:
		Eco = json.load(f)
	await interaction.response.send_message("Vous avez actuelement "+str(Eco["Comptes"][str(interaction.user.id)])+"$ sur votre compte")

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def give(interaction: discord.Interaction,member:discord.Member,money:int):
	'''Donner (créer) de l'argent à quelqu'un. Commande réservée aux HG.'''
	if not member:
		await interaction.response.send_message(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !", discord.Color.red()))
		return
	await compte(member)
	with open('economie.json', 'r') as f:
		Eco = json.load(f)
	Eco["Comptes"][str(member.id)] += int(money)
	with open('economie.json', 'w') as f:
		json.dump(Eco, f, indent=6)
	await member.send(embed=create_small_embed(interaction.user.mention+" Vous a crédité de "+str(money)+"$"))
	await interaction.response.send_message(embed=create_small_embed("L'argent à bien été crédité"))
	log = bot.get_channel(959867855350931486)
	await log.send(embed=create_small_embed(member.mention + ' à été crédité de '+str(money)+"$ par "+interaction.user.mention))

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def remove(interaction: discord.Interaction,member:discord.Member,money:int):
	'''Retirer (supprimer) de l'argent à quelqu'un. Commande réservée aux HG.'''
	if not member:
		await interaction.response.send_message(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !", discord.Color.red()))
		return
	await compte(member)
	with open('economie.json', 'r') as f:
		Eco = json.load(f)
	Eco["Comptes"][str(member.id)] -= int(money)
	with open('economie.json', 'w') as f:
		json.dump(Eco, f, indent=6)
	await member.send(embed=create_small_embed(interaction.user.mention+" Vous a privé de "+str(money)+"$"))
	await interaction.response.send_message(embed=create_small_embed("L'argent à bien été retiré"))
	log = bot.get_channel(959867855350931486)
	await log.send(embed=create_small_embed(member.mention + ' à été privé de '+str(money)+"$ par "+interaction.user.mention))

@bot.tree.command()
async def pay(interaction: discord.Interaction,member:discord.Member,money:int):
	'''Donner de l'argent à quelqu'un d'autre.'''
	if not member:
		await interaction.response.send_message(embed=create_small_embed(":warning: Ce membre n'est pas sur le discord !", discord.Color.red()))
		return
	await compte(interaction.user)
	with open('economie.json', 'r') as f:
		Eco = json.load(f)
	if Eco["Comptes"][str(interaction.user.id)] < money:
		await interaction.response.send_message(embed=create_small_embed(":warning: Vous n'avez pas assez d'argent !", discord.Color.red()))
		return
	await compte(member)
	Eco["Comptes"][str(interaction.user.id)] -= int(money)
	Eco["Comptes"][str(member.id)] += int(money)
	with open('economie.json', 'w') as f:
		json.dump(Eco, f, indent=6)
	await member.send(embed=create_small_embed(interaction.user.mention+" Vous a donné "+str(money)+"$"))
	await interaction.user.send(embed=create_small_embed("Vous avez donné " + str(money) + "$ à "+member.mention))
	await interaction.response.send_message(embed=create_small_embed("Le virement à bien été effectué"))
	log = bot.get_channel(959867855350931486)
	await log.send(embed=create_small_embed(interaction.user.mention+" à donné "+str(money)+"$ à "+member.mention))

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
		id = interaction.message.content[-4:-1]
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		await interaction.channel.purge()
		if self.values[0] == 'Plus que 5':
			await interaction.channel.send(f"Veuillez indiquer combien de {Eco['items'][id][3]} de {Eco['items'][id][0]} vous souhaitez prendre")
			nb = await chiffrecommande(interaction.user,interaction.channel)
		else:
			nb = int(str(self.values[0]))
		await interaction.channel.send("Très bien, merci encore pour votre commande. Veuillez patienter un vendeur va prendre en charge votre commande.")
		msg=f"**Acheteur :**\n{interaction.user.mention} ({interaction.user.name})\n\n**Item :**\n{Eco['items'][id][0]}\n\n**Quantité :**\n{nb} {Eco['items'][id][3]}\n\n**Prix :**\n{Eco['items'][id][1]*nb}\n\n**Pour prendre la commande, `/claim` dans le **{interaction.channel.mention}"
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		Eco["Commandes"][str(interaction.channel.id)]=msg
		with open('economie.json', 'w') as f:
			json.dump(Eco, f, indent=6)
		embed_=discord.Embed(title = "Commande "+interaction.user.name,description = msg)
		APp = interaction.guild.get_channel(960113232398401586)
		await APp.send("<@&1016022889780228136>",embed=embed_)
		await interaction.channel.send(embed=embed_)

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
	@discord.ui.button(label="J'annule ma commande !", style=discord.ButtonStyle.red, custom_id='annulernombr')
	async def annulernombr(self, interaction: discord.Interaction, button: discord.ui.Button):
		await interaction.channel.delete()

class PvP(discord.ui.Select):
	def __init__(self):
		options = []
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		for tt in Eco["items"].items():
			if 000<int(tt[0])<100:
				options.append(discord.SelectOption(label=f'{tt[1][0]} (ID : {tt[0]})',description=f'{tt[1][1]}$/{tt[1][3]}',emoji=tt[1][2]))
		super().__init__(placeholder='Quel item voulez vous commander ?', min_values=1, max_values=1, options=options, custom_id='PvP')
	async def callback(self, interaction: discord.Interaction):
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		guild = bot.get_guild(790367917812088864)
		vendeur = guild.get_role(960180290683293766)
		comm = await interaction.guild.create_text_channel(name=f"Commande {interaction.user.name}",
													overwrites={guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False, ),
															   interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True, ),
														   vendeur:discord.PermissionOverwrite(read_messages=True, send_messages=True, )},
														   category=guild.get_channel(1015558169545674782))
		await comm.send(f"{interaction.user.mention}, merci d'avoir commandé l'item {self.values[0][:-4]} chez nous. (ID : {self.values[0][-4:-1]})",view=NombreView())
		await interaction.response.send_message("Vous avez crée le channel "+comm.mention,ephemeral=True)

class PvPView(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
		self.add_item(PvP())

class farm(discord.ui.Select):
	def __init__(self):
		options = []
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		for tt in Eco["items"].items():
			if 99<int(tt[0])<200:
				options.append(discord.SelectOption(label=f'{tt[1][0]} (ID : {tt[0]})',description=f'{tt[1][1]}$/{tt[1][3]}',emoji=tt[1][2]))
		super().__init__(placeholder='Quel item voulez vous commander ?', min_values=1, max_values=1, options=options, custom_id='farm')
	async def callback(self, interaction: discord.Interaction):
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		guild = bot.get_guild(790367917812088864)
		vendeur = guild.get_role(960180290683293766)
		comm = await interaction.guild.create_text_channel(name=f"Commande {interaction.user.name}",
													overwrites={guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False, ),
															   interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True, ),
														   vendeur:discord.PermissionOverwrite(read_messages=True, send_messages=True, )},
														   category=guild.get_channel(1015558169545674782))
		await comm.send(f"{interaction.user.mention}, merci d'avoir commandé l'item {self.values[0]} chez nous. (ID : {self.values[0][-4:-1]})",view=NombreView())
		await interaction.response.send_message("Vous avez crée le channel "+comm.mention,ephemeral=True)

class farmView(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
		self.add_item(farm())

class minerais(discord.ui.Select):
	def __init__(self):
		options = []
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		for tt in Eco["items"].items():
			if 199<int(tt[0])<300:
				options.append(discord.SelectOption(label=f'{tt[1][0]} (ID : {tt[0]})',description=f'{tt[1][1]}$/{tt[1][3]}',emoji=tt[1][2]))
		super().__init__(placeholder='Quel item voulez vous commander ?', min_values=1, max_values=1, options=options, custom_id='minerais')
	async def callback(self, interaction: discord.Interaction):
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		guild = bot.get_guild(790367917812088864)
		vendeur = guild.get_role(960180290683293766)
		comm = await interaction.guild.create_text_channel(name=f"Commande {interaction.user.name}",
													overwrites={guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False, ),
															   interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True, ),
														   vendeur:discord.PermissionOverwrite(read_messages=True, send_messages=True, )},
														   category=guild.get_channel(1015558169545674782))
		await comm.send(f"{interaction.user.mention}, merci d'avoir commandé l'item {self.values[0]} chez nous. (ID : {self.values[0][-4:-1]})",view=NombreView())
		await interaction.response.send_message("Vous avez crée le channel "+comm.mention,ephemeral=True)

class mineraisView(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
		self.add_item(minerais())

class alchimiste(discord.ui.Select):
	def __init__(self):
		options = []
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		for tt in Eco["items"].items():
			if 299<int(tt[0])<400:
				options.append(discord.SelectOption(label=f'{tt[1][0]} (ID : {tt[0]})',description=f'{tt[1][1]}$/{tt[1][3]}',emoji=tt[1][2]))
		super().__init__(placeholder='Quel item voulez vous commander ?', min_values=1, max_values=1, options=options, custom_id='alchimiste')
	async def callback(self, interaction: discord.Interaction):
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		guild = bot.get_guild(790367917812088864)
		vendeur = guild.get_role(960180290683293766)
		comm = await interaction.guild.create_text_channel(name=f"Commande {interaction.user.name}",
													overwrites={guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False, ),
															   interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True, ),
														   vendeur:discord.PermissionOverwrite(read_messages=True, send_messages=True, )},
														   category=guild.get_channel(1015558169545674782))
		await comm.send(f"{interaction.user.mention}, merci d'avoir commandé l'item {self.values[0]} chez nous. (ID : {self.values[0][-4:-1]})",view=NombreView())
		await interaction.response.send_message("Vous avez crée le channel "+comm.mention,ephemeral=True)

class alchimisteView(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
		self.add_item(alchimiste())

class livres(discord.ui.Select):
	def __init__(self):
		options = []
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		for tt in Eco["items"].items():
			if 399<int(tt[0])<500:
				options.append(discord.SelectOption(label=f'{tt[1][0]} (ID : {tt[0]})',description=f'{tt[1][1]}$/{tt[1][3]}',emoji=tt[1][2]))
		super().__init__(placeholder='Quel item voulez vous commander ?', min_values=1, max_values=1, options=options, custom_id='livres')
	async def callback(self, interaction: discord.Interaction):
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		guild = bot.get_guild(790367917812088864)
		vendeur = guild.get_role(960180290683293766)
		comm = await interaction.guild.create_text_channel(name=f"Commande {interaction.user.name}",
													overwrites={guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False, ),
															   interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True, ),
														   vendeur:discord.PermissionOverwrite(read_messages=True, send_messages=True, )},
														   category=guild.get_channel(1015558169545674782))
		await comm.send(f"{interaction.user.mention}, merci d'avoir commandé l'item {self.values[0]} chez nous. (ID : {self.values[0][-4:-1]})",view=NombreView())
		await interaction.response.send_message("Vous avez crée le channel "+comm.mention,ephemeral=True)

class livresView(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
		self.add_item(livres())

class machines(discord.ui.Select):
	def __init__(self):
		options = []
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		for tt in Eco["items"].items():
			if 499<int(tt[0])<600:
				options.append(discord.SelectOption(label=f'{tt[1][0]} (ID : {tt[0]})',description=f'{tt[1][1]}$/{tt[1][3]}',emoji=tt[1][2]))
		super().__init__(placeholder='Quel item voulez vous commander ?', min_values=1, max_values=1, options=options, custom_id='machines')
	async def callback(self, interaction: discord.Interaction):
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		guild = bot.get_guild(790367917812088864)
		vendeur = guild.get_role(960180290683293766)
		comm = await interaction.guild.create_text_channel(name=f"Commande {interaction.user.name}",
													overwrites={guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False, ),
															   interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True, ),
														   vendeur:discord.PermissionOverwrite(read_messages=True, send_messages=True, )},
														   category=guild.get_channel(1015558169545674782))
		await comm.send(f"{interaction.user.mention}, merci d'avoir commandé l'item {self.values[0]} chez nous. (ID : {self.values[0][-4:-1]})",view=NombreView())
		await interaction.response.send_message("Vous avez crée le channel "+comm.mention,ephemeral=True)

class machinesView(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
		self.add_item(machines())

class outils(discord.ui.Select):
	def __init__(self):
		options = []
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		for tt in Eco["items"].items():
			if 599<int(tt[0])<700:
				options.append(discord.SelectOption(label=f'{tt[1][0]} (ID : {tt[0]})',description=f'{tt[1][1]}$/{tt[1][3]}',emoji=tt[1][2]))
		super().__init__(placeholder='Quel item voulez vous commander ?', min_values=1, max_values=1, options=options, custom_id='outils')
	async def callback(self, interaction: discord.Interaction):
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		guild = bot.get_guild(790367917812088864)
		vendeur = guild.get_role(960180290683293766)
		comm = await interaction.guild.create_text_channel(name=f"Commande {interaction.user.name}",
													overwrites={guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False, ),
															   interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True, ),
														   vendeur:discord.PermissionOverwrite(read_messages=True, send_messages=True, )},
														   category=guild.get_channel(1015558169545674782))
		await comm.send(f"{interaction.user.mention}, merci d'avoir commandé l'item {self.values[0]} chez nous. (ID : {self.values[0][-4:-1]})",view=NombreView())
		await interaction.response.send_message("Vous avez crée le channel "+comm.mention,ephemeral=True)

class outilsView(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
		self.add_item(outils())

class services(discord.ui.Select):
	def __init__(self):
		options = []
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		for tt in Eco["items"].items():
			if 699<int(tt[0])<800:
				options.append(discord.SelectOption(label=f'{tt[1][0]} (ID : {tt[0]})',description=f'{tt[1][1]}$/{tt[1][3]}',emoji=tt[1][2]))
		super().__init__(placeholder='Quel item voulez vous commander ?', min_values=1, max_values=1, options=options, custom_id='services')
	async def callback(self, interaction: discord.Interaction):
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		guild = bot.get_guild(790367917812088864)
		vendeur = guild.get_role(960180290683293766)
		comm = await interaction.guild.create_text_channel(name=f"Commande {interaction.user.name}",
													overwrites={guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False, ),
															   interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True, ),
														   vendeur:discord.PermissionOverwrite(read_messages=True, send_messages=True, )},
														   category=guild.get_channel(1015558169545674782))
		await comm.send(f"{interaction.user.mention}, merci d'avoir commandé l'item {self.values[0]} chez nous. (ID : {self.values[0][-4:-1]})",view=NombreView())
		await interaction.response.send_message("Vous avez crée le channel "+comm.mention,ephemeral=True)

class servicesView(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
		self.add_item(services())

class pillages(discord.ui.Select):
	def __init__(self):
		options = []
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		for tt in Eco["items"].items():
			if 799<int(tt[0])<900:
				options.append(discord.SelectOption(label=f'{tt[1][0]} (ID : {tt[0]})',description=f'{tt[1][1]}$/{tt[1][3]}',emoji=tt[1][2]))
		super().__init__(placeholder='Quel item voulez vous commander ?', min_values=1, max_values=1, options=options, custom_id='pillages')
	async def callback(self, interaction: discord.Interaction):
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		guild = bot.get_guild(790367917812088864)
		vendeur = guild.get_role(960180290683293766)
		comm = await interaction.guild.create_text_channel(name=f"Commande {interaction.user.name}",
													overwrites={guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False, ),
															   interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True, ),
														   vendeur:discord.PermissionOverwrite(read_messages=True, send_messages=True, )},
														   category=guild.get_channel(1015558169545674782))
		await comm.send(f"{interaction.user.mention}, merci d'avoir commandé l'item {self.values[0]} chez nous. (ID : {self.values[0][-4:-1]})",view=NombreView())
		await interaction.response.send_message("Vous avez crée le channel "+comm.mention,ephemeral=True)

class pillagesView(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
		self.add_item(pillages())

class basesclaim(discord.ui.Select):
	def __init__(self):
		options = []
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		for tt in Eco["items"].items():
			if 899<int(tt[0])<1000:
				options.append(discord.SelectOption(label=f'{tt[1][0]} (ID : {tt[0]})',description=f'{tt[1][1]}$/{tt[1][3]}',emoji=tt[1][2]))
		super().__init__(placeholder='Quel item voulez vous commander ?', min_values=1, max_values=1, options=options, custom_id='basesclaim')
	async def callback(self, interaction: discord.Interaction):
		with open('economie.json', 'r') as f:
			Eco = json.load(f)
		guild = bot.get_guild(790367917812088864)
		vendeur = guild.get_role(960180290683293766)
		comm = await interaction.guild.create_text_channel(name=f"Commande {interaction.user.name}",
													overwrites={guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False, ),
															   interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True, ),
														   vendeur:discord.PermissionOverwrite(read_messages=True, send_messages=True, )},
														   category=guild.get_channel(1015558169545674782))
		await comm.send(f"{interaction.user.mention}, merci d'avoir commandé l'item {self.values[0]} chez nous. (ID : {self.values[0][-4:-1]})",view=NombreView())
		await interaction.response.send_message("Vous avez crée le channel "+comm.mention,ephemeral=True)

class basesclaimView(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
		self.add_item(basesclaim())

@bot.tree.command()
@discord.app_commands.checks.has_permissions(manage_channels=True)
async def editmarket(interaction: discord.Interaction,categorie:str,message:str):
	'''Donner (créer) de l'argent . Commande réservée aux HG.'''
	views={"PvP":PvPView(),"farming":farmView(),"minerais":mineraisView(),"alchimiste":alchimisteView(),"livres":livresView(),"machines":machinesView(),"outils":outilsView(),"services":servicesView(),"pillages":pillagesView(),"BC":basesclaimView()}
	if categorie not in views.keys():
		await interaction.response.send_message('Mauvaise catégorie')
		return
	message = await interaction.channel.fetch_message(message)
	msg = await edimarket(categorie)
	await message.edit(content=msg, view=views[categorie])
	await interaction.response.send_message('ok',ephemeral=True)

@bot.tree.command()
@discord.app_commands.checks.has_permissions(manage_channels=True)
async def additem(interaction: discord.Interaction,id:str,titre:str,prix:int,emoji:str,stack_u:str):
	'''Ajouter un item dans le market. Commande réservée aux membres du staff (hors Recruteurs).'''
	with open('economie.json', 'r') as f:
		Eco = json.load(f)
	Eco["items"][id] = [titre,prix,emoji,stack_u]
	with open('economie.json', 'w') as f:
		json.dump(Eco, f, indent=6)
	await interaction.response.send_message(f'{titre} à été ajouté au catalogue pour {prix}$/{stack_u}',ephemeral=True)

@bot.tree.command()
@discord.app_commands.checks.has_permissions(manage_channels=True)
async def decaleid(interaction: discord.Interaction,plus_moins_arrange:str,debut:int,fin:int):
	'''Decaler tous les objets du market ou les arranger. Commande réservée aux membres du staff (hors Recruteurs).'''
	with open('economie.json', 'r') as f:
		Eco = json.load(f)
	if plus_moins_arrange=='plus':
		dict1 = dict(Eco["items"])
		for tt in Eco["items"].items():
			if debut<=int(tt[0])<=fin:
				dict1[str(int(tt[0])+1)] = tt[1]
		Eco["items"] = dict1
		with open('economie.json', 'w') as f:
			json.dump(Eco, f, indent=6)
		await interaction.response.send_message(f'tout a bien été décalé de un en plus',ephemeral=True)
	elif plus_moins_arrange=='moins':
		dict1 = dict(Eco["items"])
		for tt in Eco["items"].items():
			if debut<=int(tt[0])<=fin: 
				dict1[str(int(tt[0])-1)] = tt[1]
		Eco["items"] = dict1
		with open('economie.json', 'w') as f:
			json.dump(Eco, f, indent=6)
		await interaction.response.send_message(f'tout a bien été décalé de un en moins',ephemeral=True)
	elif plus_moins_arrange == "arrange":
		Eco["items"] = dict(sorted(Eco["items"].items(),key=lambda t: int(t[0])))
		with open('economie.json', 'w') as f:
			json.dump(Eco, f, indent=6)
		await interaction.response.send_message(f'catalogue arrangé',ephemeral=True)
	else:
		await interaction.response.send_message(f'veuillez indiquer "plus", "moins" ou "arange"',ephemeral=True)

@bot.tree.command()
@discord.app_commands.checks.has_permissions(manage_channels=True)
async def removeitem(interaction: discord.Interaction,id:str,):
	'''Retirer un item du market. Commande réservée aux membres du staff (hors Recruteurs).'''
	with open('economie.json', 'r') as f:
		Eco = json.load(f)
	Eco["items"].pop(id)
	with open('economie.json', 'w') as f:
		json.dump(Eco, f, indent=6)
	await interaction.response.send_message(f'{id} à été retiré du catalogue avec succès')

@bot.tree.command()
@discord.app_commands.checks.has_any_role(960180290683293766,821787385636585513,790675782569164820)
async def claim(interaction: discord.Interaction):
	'''Claim une commande. Commande réservée aux vendeurs.'''
	if interaction.channel.name[:8] != "commande":
		await interaction.response.send_message(embed=create_small_embed(":warning: Cette commande ne peut etre utilisée que dans une commande !", discord.Color.red()))
		return
	await compte(interaction.user)
	vendeur = interaction.guild.get_role(960180290683293766)
	resp = interaction.guild.get_role(790675781789155329)
	await interaction.channel.set_permissions(interaction.user,read_messages=True, send_messages=True)
	await interaction.channel.set_permissions(resp,read_messages=True, send_messages=True)
	await interaction.channel.set_permissions(vendeur,overwrite= None)
	await interaction.channel.edit(name="✅"+interaction.channel.name)
	await interaction.response.send_message("Vous avez bien pris en charge cette commande")

@bot.tree.command()
@discord.app_commands.checks.has_any_role(960180290683293766,821787385636585513,790675782569164820)
async def livre(interaction: discord.Interaction):
	'''Annoncer la livraison d'une commande. Commande réservée aux vendeurs.'''
	if interaction.channel.name[:9] != '✅commande':
		await interaction.response.send_message(embed=create_small_embed(":warning: Cette commande ne peut etre utilisée que dans une commande !", discord.Color.red()))
		return
	transcript = await chat_exporter.export(interaction.channel)
	transcript_file = discord.File(
		io.BytesIO(transcript.encode()),
		filename=f"transcript-{interaction.channel.name}.html",
	)
	log = bot.get_channel(819580672310116356)
	with open('economie.json', 'r') as f:
		Eco = json.load(f)
	try:
		await log.send(embed=discord.Embed(description=f"**Vendeur :\n**{interaction.user.mention} ({interaction.user.name})\n\n"+Eco["Commandes"][str(interaction.channel.id)],color=discord.Color.gold()),file=transcript_file)
	except:
		await log.send(embed=discord.Embed(description=f"Commande de {interaction.user.mention}",color=discord.Color.gold()),file=transcript_file)
	await interaction.channel.delete()

class RouleR(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label='Jouer à la roulette russe', style=discord.ButtonStyle.green, custom_id='misrr')
	async def mise1(self, interaction: discord.Interaction, button: discord.ui.Button):
		await interaction.response.send_modal(mis())

class mis(discord.ui.Modal,title="Mise"):
	def __init__(self):
		super().__init__()
		self.qq = discord.ui.TextInput(
			label=f"Combien voulez-vous miser de DP ?"
		)
		self.add_item(self.qq)
	async def on_submit(self, interaction: discord.Interaction) -> None:
		with open('points.json', 'r') as f:
			pt = json.load(f)
		try:
			mise = round(float(str(self.qq)))
		except:
			await interaction.response.send_message(":warning: Veuillez mettre un chiffre valide !",ephemeral=True)
			return
		if str(interaction.user.id) not in pt or pt[str(interaction.user.id)] < mise:
			await interaction.response.send_message(":warning: Vous n'avez pas assez d'argent pour miser ca !",ephemeral=True)
			return
		pt[str(interaction.user.id)] -= mise
		with open('points.json', 'w') as f:
			json.dump(pt, f, indent=6)
		chance = random.randint(1, 6)
		if chance == 1: #perdu
			embed = discord.Embed(
						title='Vous avez perdu...',
						description='Vous pouvez toujours retenter votre chance !',
						timestamp=datetime.utcnow(),
					)
			embed.set_thumbnail(url='https://c.tenor.com/ZpBMkWyufhMAAAAC/dead.gif')
			await interaction.response.send_message(embed=embed,ephemeral=True)
			return
		else: #gain sans 
			mise = round(mise/(1-1/6))
			embed = discord.Embed(
					title='Vous avez gagné !',
					description=f"Vous avez gagné __**{mise}$**__ !\nTenterez vous de rejouer afin d'augmenter votre gain à __**{round(mise/(1-1/5))}$**__ ?",
					timestamp = datetime.utcnow()
					)
			embed.set_thumbnail(url='https://c.tenor.com/YjPBups7H48AAAAC/6m-rain.gif')
			await interaction.response.send_message(embed=embed, view=contijouer(mise,1),ephemeral=True)

class contijouer(discord.ui.View):
	def __init__(self,mise,nb):
		super().__init__(timeout=None)
		self.mise = mise
		self.nb = nb
	@discord.ui.button(label='Continuer à jouer', style=discord.ButtonStyle.green, custom_id='conti')
	async def contiroulette(self, interaction: discord.Interaction, button: discord.ui.Button):
		chance = random.randint(1, 6-int(str(self.nb)))
		mise = round(float(str(self.mise)))/(1-1/(6-round(float(str(self.nb)))))
		if chance == 1: #perdu
			embed = discord.Embed(
						title='Vous avez perdu...',
						description='Vous pouvez toujours retenter votre chance !',
						timestamp=datetime.utcnow(),
					)
			embed.set_thumbnail(url='https://c.tenor.com/ZpBMkWyufhMAAAAC/dead.gif')
			await interaction.response.edit_message(embed=embed,view=None)
			return

		elif int(str(self.nb)) == 4: #Max possible
			embed = discord.Embed(
			title='JACKPOT !',
			description=f"Vous avez gagné {mise}$ ! Vous avez touché le maximum d'argent possible !",
			timestamp = datetime.utcnow()
			)
			with open('points.json', 'r') as f:
				pt = json.load(f)
			pt[str(interaction.user.id)] += mise
			with open('points.json', 'w') as f:
				json.dump(pt, f, indent=6)
			embed.set_thumbnail(url='https://tenor.com/view/wealthy-rich-money-rain-money-money-money-fan-gif-14057775')
			await interaction.response.edit_message(embed=embed,view=None)

		else: #gain sans 
			embed = discord.Embed(
					title='Vous avez gagné !',
					description=f"Vous avez gagné __**{mise}$**__ !\nTenterez vous de rejouer afin d'augmenter votre gain à __**{round(mise/(1-1/(6-round(float(str(self.nb)))-1)))}$**__ ?",
					timestamp = datetime.utcnow()
					)
			embed.set_thumbnail(url='https://tenor.com/view/win-obama-mic-drop-winner-peace-gif-16949541')
			await interaction.response.edit_message(embed=embed, view=contijouer(mise,int(str(self.nb))+1))
	@discord.ui.button(label='Ne pas jouer', style=discord.ButtonStyle.red, custom_id='arret')
	async def Arretroulette(self, interaction: discord.Interaction, button: discord.ui.Button):
		with open('points.json', 'r') as f:
			pt = json.load(f)
		pt[str(interaction.user.id)] += round(float(str(self.mise)))
		with open('points.json', 'w') as f:
			json.dump(pt, f, indent=6)
		await interaction.response.edit_message(embed=create_small_embed(f'Vous avez arrete la partie et avez gagné {round(float(str(self.mise)))} DP'),view=None)

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

@bot.tree.command()
async def addpersonne(interaction: discord.Interaction,personne:discord.Member):
	'''Ajouter quelqu'un dans votre channel de jeu. Ne marche que dans un channel de jeu.'''
	if interaction.channel.name[:8] != 'roulette':
		await interaction.response.send_message(embed=create_small_embed(":warning: Cette commande ne peut etre utilisée que dans un salon de jeu !", discord.Color.red()))
		return
	await interaction.channel.edit(overwrites={personne: discord.PermissionOverwrite(read_messages=True, send_messages=True,)})
	await interaction.response.send_message(f'{personne.mention} à bien été ajouté',ephemeral=True)

class roulette(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label='Jouer à la Roulette Américaine', style=discord.ButtonStyle.green, custom_id='debutrouletteA')
	async def RoulletteA(self, interaction: discord.Interaction, button: discord.ui.Button):
		jeu = await interaction.guild.create_text_channel(f'roulette-{interaction.user.name}',overwrites={interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False,),interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True,)})
		embed = create_embed('Roulette Américaine','''Jouez à la roulette américaine avec vos amis !\nPour ajouter quelqu'un à votre partie faites /addpersonne\n:warning: **__NE PAS MISER PLUSIEURS A LA FOIS__**''')
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/772451269272928257/965658339428171876/unknown.png")
		await jeu.send(embed=embed,view=rouleView({},interaction.user.id))
		await interaction.response.send_message(f"Nouvelle partie crée dans le channel {jeu.mention}",ephemeral=True)

class rouleView(discord.ui.View):
	def __init__(self,mises,ide):
		super().__init__(timeout=None)
		self.add_item(roule(mises,ide))
		self.mises = mises
		self.ide = ide
	@discord.ui.button(label='Lancer la roulette', style=discord.ButtonStyle.green, custom_id='lancerrouletteA')
	async def lanroue(self, interaction: discord.Interaction, button: discord.ui.Button):
		if interaction.user.id != int(str(self.ide)):
			await interaction.response.send_message(':warning: Seul le créateur de la partie peut lancer la roue !',ephemeral=True)
			return
		mises = dict(self.mises)
		rouge = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
		with open('points.json', 'r') as f:
			pt = json.load(f)
		chance = random.randint(0,37)         #Tirage
		await interaction.response.edit_message(embed=create_embed(f"{chance}. {'Rouge' if chance in rouge else 'Noir'}."),view=None)
		if chance in mises.keys():            #Chiffre
			for gains in mises[chance]:
				pt[str(gains[0])] += gains[1]*36
				await interaction.channel.send(f'Félicitations à <@{gains[0]}> qui avait misé sur le {chance} et qui remporte **{gains[1]*36}** DP !')
		if chance == 0 or chance == 37:       #0 ou 00 = aucune recompense sauf les chiffres
			return
		
		bools = [[chance in rouge,['Rouge','Noir']],[chance%2 == 0,['Pair','Impair']],[chance//19 == 0,['Manque','Passe']]]
		for boole in bools:
			var = 1
			if boole[0]:
				var = 0
			if boole[1][var] in mises.keys():
				for gains in mises[boole[1][var]]:
					pt[str(gains[0])] += gains[1]*2
					await interaction.channel.send(f'Félicitations à <@{gains[0]}> qui avait misé sur {boole[1][var]} et qui remporte **{gains[1]*2}** DP !')
		
		valeurs = [['douzaine 1','douzaine 2','douzaine 3'],['colone 3','colone 1','colone 2']]
		val2 = [chance//13,chance%3]
		for i in range(2):
			if valeurs[i][val2[i]] in mises.keys():
				for gains in mises[valeurs[i][val2[i]]]:
					pt[str(gains[0])] += gains[1]*3
					await interaction.channel.send(f'Félicitations à <@{gains[0]}> qui avait misé sur {valeurs[i][val2[i]]} et qui remporte **{gains[1]*3}** DP !')
		with open('points.json', 'w') as f:
			json.dump(pt, f, indent=6)
		embed = create_embed('Roulette Américaine','''Jouez à la roulette américaine avec vos amis !\nPour ajouter quelqu'un à votre partie faites /addpersonne''')
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/772451269272928257/965658339428171876/unknown.png")
		await interaction.channel.send(embed=embed,view=rouleView({},interaction.user.id))
	@discord.ui.button(label='Fermer la partie', style=discord.ButtonStyle.red, custom_id='fermerroul')
	async def fermerchan(self, interaction: discord.Interaction, button: discord.ui.Button):
		await interaction.channel.delete()

# mises = {5:[[025451164521215,100],[584415458455545,200]],"Rouge":[[05059552624595656,500]]}
class roule(discord.ui.Select):
	def __init__(self,mises,ide):
		options = [
			discord.SelectOption(label='Miser sur un chiffre', description='Mise x36',value='chiffre'),
			discord.SelectOption(label='Miser sur Rouge', description='Mise x2',value='Rouge'),
			discord.SelectOption(label='Miser sur Noir', description='Mise x2',value='Noir'),
			discord.SelectOption(label='Miser sur Pair', description='Mise x2',value='Pair'),
			discord.SelectOption(label='Miser sur Impair', description='Mise x2',value='Impair'),
			discord.SelectOption(label='Miser sur Manque (1-18)', description='Mise x2',value='Manque'),
			discord.SelectOption(label='Miser sur Passe (19-36)', description='Mise x2',value='Passe'),
			discord.SelectOption(label='Miser sur la première douzaine (1-12)', description='Mise x3',value='douzaine 1'),
			discord.SelectOption(label='Miser sur la deuxième douzaine (13-24)', description='Mise x3',value='douzaine 2'),
			discord.SelectOption(label='Miser sur la troisième douzaine (25-36)', description='Mise x3',value='douzaine 3'),
			discord.SelectOption(label='Miser sur la première colone (1-12)', description='Mise x3',value='colone 1'),
			discord.SelectOption(label='Miser sur la deuxième colone (13-24)', description='Mise x3',value='colone 2'),
			discord.SelectOption(label='Miser sur la troisième colone (25-36)', description='Mise x3',value='colone 3'),
		]
		super().__init__(placeholder='Sur quoi voulez vous miser ?', min_values=1, max_values=1, options=options,
						 custom_id='inter')
		self.mises = mises
		self.ide = ide
	async def callback(self, interaction: discord.Interaction):
		await interaction.response.send_modal(roulemis(self.values[0],self.mises,self.ide))

class roulemis(discord.ui.Modal,title="Mise"):
	def __init__(self,choix,mises,ide):
		super().__init__()
		if str(choix) == 'chiffre':
			self.quoi= discord.ui.TextInput(
			label=f"Sur quel chiffre voulez-vous miser ?"
		)
			self.add_item(self.quoi)
		self.qq = discord.ui.TextInput(
			label=f"Combien voulez-vous miser de DP ?"
		)
		self.add_item(self.qq)
		self.choix = choix
		self.mises = mises
		self.ide = ide
	async def on_submit(self, interaction: discord.Interaction) -> None:
		with open('points.json', 'r') as f:
			pt = json.load(f)
		try:
			mise = round(float(str(self.qq)))
			if str(self.choix) == 'chiffre':
				chiffre = int(str(self.quoi))
		except:
			await interaction.response.send_message(":warning: Veuillez mettre un chiffre valide !",ephemeral=True)
			return
		if str(interaction.user.id) not in pt or pt[str(interaction.user.id)] < mise:
			await interaction.response.send_message(":warning: Vous n'avez pas assez d'argent pour miser ca !",ephemeral=True)
			return
		pt[str(interaction.user.id)] -= mise
		with open('points.json', 'w') as f:
			json.dump(pt, f, indent=6)
		mises = dict(self.mises)
		if str(self.choix) == 'chiffre':
			if chiffre in mises.keys():
				mises[chiffre].append([interaction.user.id,mise])
			else:
				mises[chiffre] = [[interaction.user.id,mise]]
		else:
			if str(self.choix) in mises.keys():
				mises[str(self.choix)].append([interaction.user.id,mise])
			else:
				mises[str(self.choix)] = [[interaction.user.id,mise]]
		await interaction.response.edit_message(view=rouleView(mises,self.ide))
		await interaction.channel.send(f'{interaction.user.mention} à misé {mise} sur {str(self.choix)}')

class blackjackview(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label='Jouer au BlackJack', style=discord.ButtonStyle.green, custom_id='debutBJ')
	async def RoulletteA(self, interaction: discord.Interaction, button: discord.ui.Button):
		await interaction.response.send_modal(BJmis())

class BJmis(discord.ui.Modal,title="Mise"):
	def __init__(self):
		super().__init__()
		self.qq = discord.ui.TextInput(
			label=f"Combien voulez-vous miser de DP ?"
		)
		self.add_item(self.qq)
	async def on_submit(self, interaction: discord.Interaction) -> None:
		with open('points.json', 'r') as f:
			pt = json.load(f)
		try:
			mise = round(float(str(self.qq)))
		except:
			await interaction.response.send_message(":warning: Veuillez mettre un chiffre valide !",ephemeral=True)
			return
		if str(interaction.user.id) not in pt or pt[str(interaction.user.id)] < mise:
			await interaction.response.send_message(":warning: Vous n'avez pas assez d'argent pour miser ca !",ephemeral=True)
			return
		pt[str(interaction.user.id)] -= mise
		
		cartes = addcarte([0])
		cartes = addcarte(cartes)

		croupier = addcarte([0])
		if cartes[0] == 21:
			croupier = addcarte(croupier)
			if croupier[0] == 21:
				pt[str(interaction.user.id)] += mise
				await interaction.response.send_message(embed=create_small_embed(f'Vous avez {", ".join([cartes[i] for i in range(1,len(cartes))])}.\nLe croupier à {", ".join([croupier[i] for i in range(1,len(croupier))])}.\nDouble Blackjack, vous recuperez votre mise.'),ephemeral=True)
			else:
				pt[str(interaction.user.id)] += 3*mise
				await interaction.response.send_message(embed=create_small_embed(f'Vous avez {", ".join([cartes[i] for i in range(1,len(cartes))])}.\nLe croupier à {", ".join([croupier[i] for i in range(1,len(croupier))])}.\nBlackjack ! Vous triplez votre mise !'),ephemeral=True)
		else:
			await interaction.response.send_message(embed=create_small_embed(f'Vous avez {", ".join([cartes[i] for i in range(1,len(cartes))])}.\nLe croupier à {", ".join([croupier[i] for i in range(1,len(croupier))])}.\nQue voulez-vous faire ?'),view=jeuBJ(mise,cartes,croupier),ephemeral=True)
		with open('points.json', 'w') as f:
			json.dump(pt, f, indent=6)

def addcarte(cartes):		
	cartess = [['un as','un deux','un trois','un quatre','un cinq','un six','un sept','un huit','un neuf','un dix','un valet','une dame','un roi'],['coeur','carreau','pique','trefle']]
	valeur,couleur = random.randint(0,12),random.randint(0,3)
	cartes[0] += (valeur+1 if valeur<10 else 10)
	cartes.append(f'{cartess[0][valeur]} de {cartess[1][couleur]}')
	return cartes

class jeuBJ(discord.ui.View):
	def __init__(self,mise,cartes,croupier):
		super().__init__(timeout=None)
		self.mise = mise
		self.cartes = cartes
		self.croupier = croupier
	@discord.ui.button(label='Tirer une carte', style=discord.ButtonStyle.green, custom_id='contiBJ')
	async def tir(self, interaction: discord.Interaction, button: discord.ui.Button):
		cartess = [['un as','un deux','un trois','un quatre','un cinq','un six','un sept','un huit','un neuf','un dix','un valet','une dame','un roi'],['coeur','carreau','pique','trefle']]
		croupier = list(self.croupier)
		cartes = addcarte(list(self.cartes))
		if cartes[0] > 21:
			await interaction.response.edit_message(embed=create_small_embed(f"""Vous avez {", ".join([cartes[i] for i in range(1,len(cartes))])}.\nLe croupier à {", ".join([croupier[i] for i in range(1,len(croupier))])}.\nVous avez sauté, vous perdez votre mise."""))
		else:
			await interaction.response.edit_message(embed=create_small_embed(f"""Vous avez {", ".join([cartes[i] for i in range(1,len(cartes))])}.\nLe croupier à {", ".join([croupier[i] for i in range(1,len(croupier))])}.\nQue voulez-vous faire ?"""),view=jeuBJ(self.mise,cartes,croupier))
	@discord.ui.button(label='Arreter', style=discord.ButtonStyle.red, custom_id='finBJ')
	async def sto(self, interaction: discord.Interaction, button: discord.ui.Button):
		cartess = [['un as','un deux','un trois','un quatre','un cinq','un six','un sept','un huit','un neuf','un dix','un valet','une dame','un roi'],['coeur','carreau','pique','trefle']]
		croupier = list(self.croupier)
		cartes = list(self.cartes)
		mise = round(float(self.mise))
		with open('points.json', 'r') as f:
			pt = json.load(f)
		while croupier[0] < 16:
			croupier = addcarte(croupier)
			if croupier[0] > 21:
				pt[str(interaction.user.id)] += 2*mise
				await interaction.response.edit_message(embed=create_small_embed(f"""Vous avez {", ".join([cartes[i] for i in range(1,len(cartes))])}.\nLe croupier à {", ".join([croupier[i] for i in range(1,len(croupier))])}.\nLe croupier à sauté, vous gagné deux fois votre mise ({2*mise} DP)."""))
		if croupier[0] > cartes[0]:
			await interaction.response.edit_message(embed=create_small_embed(f"""Vous avez {", ".join([cartes[i] for i in range(1,len(cartes))])}.\nLe croupier à {", ".join([croupier[i] for i in range(1,len(croupier))])}.\nLe croupier à plus que vous, vous perdez votre mise."""))
		elif croupier[0] == cartes[0]:
			pt[str(interaction.user.id)] += mise
			await interaction.response.edit_message(embed=create_small_embed(f"""Vous avez {", ".join([cartes[i] for i in range(1,len(cartes))])}.\nLe croupier à {", ".join([croupier[i] for i in range(1,len(croupier))])}.\nLe croupier à autant que vous, vous recuperez votre mise ({mise} DP)."""))
		else:
			pt[str(interaction.user.id)] += 2*mise
			await interaction.response.edit_message(embed=create_small_embed(f"""Vous avez {", ".join([cartes[i] for i in range(1,len(cartes))])}.\nLe croupier à {", ".join([croupier[i] for i in range(1,len(croupier))])}.\nVous avez plus que le croupier, vous recuperez deux fois votre mise ({2*mise} DP)."""))
		with open('points.json', 'w') as f:
			json.dump(pt, f, indent=6)

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def reset(interaction: discord.Interaction,res:str):
	'''Remettre tous les comptes (money) à zero. Commande réservée aux HG.'''
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
	await interaction.response.send_message("Tout s'est bien passé")

# =========== Relation Faction ===========

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def addpna(interaction: discord.Interaction,faction:str,member:discord.Member):
	'''Ajouter un pna. Commande réservée aux HG.'''
	if not faction:
		await interaction.response.send_message(embed=create_small_embed(":warning: Vous n'avez pas spécifié de faction !",discord.Color.red()))
		return
	if not member:
		await interaction.response.send_message(embed=create_small_embed(":warning: Vous n'avez pas spécifié d'Ambassadeur !",discord.Color.red()))
		return
	with open('rela.json', 'r') as f:
		rela = json.load(f)
	rela["pna"][faction] = {member.id:[]}
	with open('rela.json', 'w') as f:
		json.dump(rela, f, indent=6)
	await edditally()
	await interaction.response.send_message(embed=create_small_embed('Vous avez ajouté cette faction à la liste avec succès'))

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def addtruce(interaction: discord.Interaction,faction:str,member:discord.Member):
	'''Ajouter une truce. Commande réservée aux HG.'''
	if not faction:
		await interaction.response.send_message(embed=create_small_embed(":warning: Vous n'avez pas spécifié de faction !",discord.Color.red()))
		return
	if not member:
		await interaction.response.send_message(embed=create_small_embed(":warning: Vous n'avez pas spécifié d'Ambassadeur !",discord.Color.red()))
		return
	with open('rela.json', 'r') as f:
		rela = json.load(f)
	rela["truce"][faction] = {member.id:[]}
	with open('rela.json', 'w') as f:
		json.dump(rela, f, indent=6)
	role = interaction.guild.get_role(790675785412640768)
	await member.add_roles(role)
	await edditally()
	await interaction.response.send_message(embed=create_small_embed('Vous avez ajouté cette faction à la liste avec succès'))

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def addally(interaction: discord.Interaction,faction:str,member:discord.Member):
	'''Ajouter une ally. Commande réservée aux HG.'''
	if not faction:
		await interaction.response.send_message(embed=create_small_embed(":warning: Vous n'avez pas spécifié de faction !",discord.Color.red()))
		return
	if not member:
		await interaction.response.send_message(embed=create_small_embed(":warning: Vous n'avez pas spécifié d'Ambassadeur !",discord.Color.red()))
		return
	with open('rela.json', 'r') as f:
		rela = json.load(f)
	rela["ally"][faction] = {member.id:[]}
	with open('rela.json', 'w') as f:
		json.dump(rela, f, indent=6)
	role = interaction.guild.get_role(790675785412640768)
	await member.add_roles(role)
	await edditally()
	await interaction.response.send_message(embed=create_small_embed('Vous avez ajouté cette faction à la liste avec succès'))

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def endally(interaction: discord.Interaction,faction:str):
	'''Mettre fin a une alliance, quelle qu'elle soit. Commande réservée aux HG.'''
	if not faction:
		await interaction.response.send_message(embed=create_small_embed(":warning: Vous n'avez pas spécifié de faction !",discord.Color.red()))
		return
	with open('rela.json', 'r') as f:
		rela = json.load(f)
	for type in rela.items():
		for fac in type[1].items():
			if faction == fac[0]:
				typ = type[0]
				for id in fac[1].keys():
					memberid = id
	mem = interaction.guild.get_member(memberid)
	try:
		ally = interaction.guild.get_role(790675785412640768)
		await mem.remove_roles(ally)
		await mem.send(f'Notre alliance étant terminée votre grade {ally.mention} vous a été retiré')
	except:
		pass
	for personne in rela[typ][faction][memberid]:
		try:
			member = interaction.guild.get_member(int(personne))
			ally = interaction.guild.get_role(790675785412640768)
			await member.remove_roles(ally)
			await member.send(f'Notre alliance étant terminée votre grade {ally.mention} vous a été retiré')
		except:
			pass
	rela[typ].pop(faction)
	with open('rela.json', 'w') as f:
		json.dump(rela, f, indent=6)
	await edditally()
	await interaction.response.send_message(embed=create_small_embed('Vous avez retiré cette faction de la liste avec succès'))

@bot.tree.command()
async def addmember(interaction: discord.Interaction,member:discord.Member,faction:str):
	'''Ajouter un membre à votre faction pour leur donner le role "Ally/Truces". Commande réservée aux chefs de faction alliées.'''
	if not member:
		await interaction.response.send_message(embed=create_small_embed(":warning: Vous n'avez pas spécifié de membre à ajouter !",discord.Color.red()))
		return
	with open('rela.json', 'r') as f:
		rela = json.load(f)
	for type in rela.items():
		for fac in type[1].items():
			if str(interaction.user.id) in fac[1].keys():
				faction = fac[0]
				typ = type[0]
	try:
		if not typ or not faction:
			await interaction.response.send_message(embed=create_small_embed(":warning: Vous n'etes pas un Ambassadeur !",discord.Color.red()))
			return
	except:
		await interaction.response.send_message(embed=create_small_embed(":warning: Vous n'etes pas un Ambassadeur !",discord.Color.red()))
		return
	if member.id in rela[typ][faction][str(interaction.user.id)]:
		await interaction.response.send_message('Cette personne est déjà dans notre base de donnée.')
	else:
		rela[typ][faction][str(interaction.user.id)].append(member.id)
	with open('rela.json', 'w') as f:
		json.dump(rela, f, indent=6)
	role = interaction.guild.get_role(790675785412640768)
	await member.add_roles(role)
	await interaction.response.send_message(embed=create_small_embed(f'Vous avez ajouté {member.mention} à votre faction avec succès'))

@bot.tree.command()
async def removemember(interaction: discord.Interaction,member:discord.Member,faction:str):
	'''Retirer un membre de votre faction pour leur enlever le role "Ally/Truces". Commande réservée aux chefs de faction alliées.'''
	if not member:
		await interaction.response.send_message(embed=create_small_embed(":warning: Vous n'avez pas spécifié de membre à ajouter !",discord.Color.red()))
		return
	with open('rela.json', 'r') as f:
		rela = json.load(f)
	for type in rela.items():
		for fac in type[1].items():
			if str(interaction.user.id) in fac[1].keys():
				faction = fac[0]
				typ = type[0]
	if not typ or not faction:
		await interaction.response.send_message(embed=create_small_embed(":warning: Vous n'etes pas un Ambassadeur !",discord.Color.red()))
		return
	if member.id in rela[typ][faction][str(interaction.user.id)]:
		rela[typ][faction][str(interaction.user.id)].remove(member.id)
	else:
		await interaction.response.send_message("Cette personne n'est pas dans notre base de donnée.")
	with open('rela.json', 'w') as f:
		json.dump(rela, f, indent=6)
	role = interaction.guild.get_role(790675785412640768)
	await member.remove_roles(role)
	await interaction.response.send_message(embed=create_small_embed(f'Vous avez enlevé {member.mention} de votre faction avec succès'))

@bot.tree.command()
@discord.app_commands.checks.cooldown(1, 86400)
async def askally(interaction: discord.Interaction,faction:str):
	'''Demander à votre chef de faction le role "Ally/Truces". Cooldown de 4 heures pour eviter le spam.'''
	if not faction:
		await interaction.response.send_message(embed=create_small_embed(":warning: Vous n'avez pas spécifié de faction !",discord.Color.red()))
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
		await interaction.response.send_message(":warning: Vous n'etes pas en alliance ou avez spécifié la mauvaise faction !")
		return
	await member.send(f'{interaction.user.mention} est il de votre faction ?',view=IsAlly())
	await interaction.response.send_message(embed=create_small_embed(f'Vous avez demandé à {member.mention} de rejoindre la {faction} avec succès'))

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

""" @bot.event
async def on_member_join(member):
	if not member.bot:
		with open ('invite.json','r') as f:
			inv = json.load(f)
		guild = member.guild
		invit = guild.get_channel(791452088370069525)
		for inviteguild in await guild.invites():
			for invitemembre in inv["invites"].keys():
				if inviteguild.code == invitemembre:
					invitemembre = await bot.fetch_invite(invitemembre)
					if inviteguild.uses > inv['invites'][inviteguild.code] and member.id not in inv["members"][str(inviteguild.inviter.id)]:
						inviteur = inviteguild.inviter
						if inviteguild.inviter.id in inv["members"].keys():
							inv["members"][str(inviteguild.inviter.id)].append(member.id)
						else:
							inv["members"][str(inviteguild.inviter.id)] = [member.id]
		with open ('invite.json','w') as f:
			json.dump(inv,f,indent=6)
		await invit.send(embed=create_small_embed(f'{member.mention} à été invité par {inviteur.mention} !'))

@bot.event
async def on_member_remove(member):
	if not member.bot:
		with open ('invite.json','r') as f:
			inv = json.load(f)
		for mem in inv["members"].items():
			if member.id in mem[1]:
				inv["members"][mem[0]].pop(member.id)
		with open ('invite.json','w') as f:
			json.dump(inv,f,indent=6)

@bot.tree.command()
async def invtop(interaction: discord.Interaction):
	with open ('invite.json','r') as f:
		inv = json.load(f)
	roles = [791066207418712094,791066206437113897,790675784225521734,790675784120401932,790675783693500456,790675783549976579,790675783352975360,790675782364037131,790675782338740235]
	invitations = []
	for memberid in inv["members"].keys():
		invi = 0
		for invit in inv["members"][memberid]:
			member = interaction.guild.get_member(int(invit))
			for role in roles:
				role = interaction.guild.get_role(role)
				if role in member.roles:
					invi += 1
		invitations.append([int(memberid),invi])
	clas = [[0,0],[0,0],[0,0]]
	for invit in invitations:
		if invit[1] > clas[2][1]:
			if invit[1] > clas[1][1]:
				if invit[1] > clas[0][1]:
					clas[2] = clas[1]
					clas[1] = clas[0]
					clas[0] = invit
				else:
					clas[2] = clas[1]
					clas[1] = invit
			else:
				clas[2] = invit
	try:
		pr = bot.get_user(int(clas[0][0])).mention
	except:
		pr = 'Aucun'
	try:
		dx = bot.get_user(int(clas[1][0])).mention
	except:
		dx = 'Aucun'
	try:
		tr = bot.get_user(int(clas[2][0])).mention
	except:
		tr = 'Aucun'
	await interaction.response.send_message(embed=create_small_embed(f'Voici notre classement :\n\n1er : {pr}\ninvites : {clas[0][1]}\n\n2eme : {dx}\ninvites : {clas[1][1]}\n\n1er : {tr}\ninvites : {clas[2][1]}\n\n'))

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def blbl(interaction: discord.Interaction):
	with open('equipes.json','r') as f:
		eq = json.load(f)
	with open('voc.json','r') as f:
		voc = json.load(f)
	for element in eq.keys():
		role = interaction.guild.get_role(int(element))
		for membre in role.members:
			if str(membre.id) in voc['11/2022'].keys():
				eq[element]['membres'][str(membre.id)] = voc['11/2022'][str(membre.id)]
	with open ('equipes.json','w') as f:
		json.dump(eq,f,indent=6)
"""
# =========== Fun ===========

@bot.tree.command()
async def aleacrush(interaction: discord.Interaction,member:discord.Member):
	'''Trouvez votre crush (tirage aléatoire).'''
	if not member:
		member = interaction.user
	guild = interaction.guild
	member2 = guild.members[random.randint(0,len(guild.members))]
	await interaction.response.send_message(embed=create_small_embed(f'{member.mention}, Vous êtes tombé sous le charme de {member2.mention}'))

@bot.tree.command()
@discord.app_commands.checks.cooldown(1, 30)
async def pendu(interaction: discord.Interaction):
	'''Jouer au pendu (en maintenance)'''
	with open('liste_francais.txt','r',encoding="latin-1") as f:
		liste = f.readlines()
	f = 0
	pend = ["","```\n_______```","```\n|\n|\n|\n|\n|\n_______```","```\n__________\n|\n|\n|\n|\n|\n_______```","```\n__________\n|         |\n|\n|\n|\n|\n_______```","```\n__________\n|         |\n|         °\n|\n|\n|\n_______```","```\n__________\n|         |\n|         °\n|         |\n|\n|\n_______```","```\n__________\n|         |\n|         °\n|         |\n|         /\n|\n_______```","```\n__________\n|         |\n|         °\n|         |\n|         /\ \n|\n_______```","```\n__________\n|         |\n|         °\n|         |\ \n|         /\ \n|\n_______```","```\n__________\n|         |\n|         °\n|        /|\ \n|         /\ \n|\n_______```"]
	mot = list(liste[random.randint(0,len(liste))].lower())
	trouv = ['- ']*(len(mot)-1)
	util = []
	mot.pop(-1)
	message = await interaction.channel.send(" ".join(trouv))
	while f<10:
		let = await interaction.channel.send('\nVeuillez donner une lettre')
		lettre = (await waiting(interaction)).content
		if lettre in util:
			await interaction.channel.send('Vous avez déjà utilisé cette lettre !')
		else:
			if lettre in mot:
				for i in range(len(mot)):
					if mot[i] == lettre:
						trouv[i] = lettre
			else:
				await interaction.channel.send("Votre lettre n'est pas dans le mot")
				f += 1
			util.append(lettre)
		await message.delete()
		message = await interaction.channel.send(content=pend[f]+"\n"+' '.join(trouv))
		if trouv == mot:
			await interaction.response.send_message('Vous avez gagné ! Félicitations !')
			return
		await let.delete()
	await interaction.response.send_message(f"Vous avez perdu ! Le mot était {''.join(mot)}")

async def waiting(interaction: discord.Interaction):
	def check(m):
		return m.author == interaction.user and m.channel == interaction.channel
	lettre = await bot.wait_for('message', timeout=600, check=check)
	if len(lettre.content)>1 or ord(lettre.content)<97 or ord(lettre.content)>122:
		await interaction.response.send_message("Veuillez n'indiquer qu'une seule lettre minuscule")
		lettre = await waiting(interaction)
	return lettre

@bot.tree.command()
async def motus(interaction: discord.Interaction):
	'''Jouer au motus (en maintenance)'''
	with open('liste_francais.txt','r',encoding="latin-1") as f:
		liste = f.readlines()
	mot = list(liste[random.randint(0,len(liste))].upper())
	mot.pop(-1)
	message = await interaction.channel.send(f"Veuillez indiquer des mots en {len(mot)} lettres\n")
	for j in range(5):
		let = await interaction.channel.send('\nVeuillez donner un mot')
		motu = list(((await ww(interaction,len(mot))).content).upper())
		if motu == mot:
			await interaction.response.send_message('Vous avez gagné ! Félicitations !')
			await message.edit(content=message.content+'\n***__'+'__*** ***__'.join(motu)+'__***')
			return
		for i in range(len(motu)):
			if motu[i] in mot:
				if motu[i] == mot[i]:
					motu[i] = f'***{motu[i]}***'
				motu[i] = f'__{motu[i]}__'
		desc = message.content+"\n"+' '.join(motu)
		await message.delete()
		message = await interaction.channel.send(desc)
		await let.delete()
	await interaction.response.send_message(f"Vous avez perdu ! Le mot était {''.join(mot)}")

async def ww(interaction: discord.Interaction,ll):
	with open('liste_francais.txt','r',encoding="latin-1") as f:
		liste = f.readlines()
	def check(m):
		return m.author == interaction.user and m.channel == interaction.channel
	lettre = await bot.wait_for('message', timeout=600, check=check)
	if len(lettre.content)!=ll:
		await interaction.response.send_message(f"Veuillez n'indiquer que des mots francais de {ll} lettres")
		lettre = await ww(interaction,ll)
	if (lettre.content+'\n') not in liste:
		print("pb")
	return lettre

# =========== points ===========

@bot.tree.command()
@discord.app_commands.checks.has_any_role(790675781789155329,821787385636585513,790675782569164820)
async def renduquotas(interaction: discord.Interaction,catalogue:str,member:discord.Member):
	'''Annoncer le rendu d'un quota. Commande réservée aux membres du staff (hors recruteurs)'''
	cat = {"poussin":400,'tranquillou':800,'intermediaire':1200,'tryharder':2100,'giga chad':3000}
	if catalogue not in cat.keys():
		await interaction.response.send_message("Ce n'est pas un catalogue valide !")
		return
	with open ('points.json','r') as f:
		pt = json.load(f)
	if str(member.id) in pt.keys():
		pt[str(member.id)] += cat[catalogue]
	else:
		pt[str(member.id)] = cat[catalogue]
	with open ('equipes.json','r') as f:
		eq = json.load(f)
	for role in eq.keys():
		if int(role) in [t.id for t in member.roles]:
			eq[role]['total'] += cat[catalogue]
			if str(member.id) in eq[role]['membres'].keys():
				eq[role]['membres'][str(member.id)] += cat[catalogue]
			else:
				eq[role]['membres'][str(member.id)] = cat[catalogue]
	with open ('equipes.json','w') as f:
		json.dump(eq,f,indent=6)
	with open ('points.json','w') as f:
		json.dump(pt,f,indent=6)
	log = bot.get_channel(1026567820311531550)
	await log.send(f'{member.mention} à fait la quota "{catalogue}" et à reçu {cat[catalogue]} points')
	await member.send(f'Vous avez fait le quota "{catalogue}" cette semaine et avez reçu {cat[catalogue]} points !')
	await interaction.response.send_message('Le message à bien été envoyé')

@bot.tree.command()
async def dreampoints(interaction: discord.Interaction):
	'''Regarder votre solde de DreamPoints'''
	if interaction.channel.id != 811653993033891870:
		await interaction.response.send_message('Vous ne pouvez utiliser cette commande que dans le <#811653993033891870>',ephemeral=True)
		return
	with open ('points.json','r') as f:
		pt = json.load(f)
	if str(interaction.user.id) in pt.keys():
		points = pt[str(interaction.user.id)]
	else:
		points = 0
	await interaction.response.send_message(f'Vous avez ``{points}`` points')

@bot.tree.command()
async def paydp(interaction: discord.Interaction,member:discord.Member,montant:int):
	'''Donner à un membre un certain nombre de dp depuis votre solde'''
	if interaction.channel.id != 811653993033891870:
		await interaction.response.send_message('Vous ne pouvez utiliser cette commande que dans le <#811653993033891870>',ephemeral=True)
		return
	with open ('points.json','r') as f:
		pt = json.load(f)
	if str(interaction.user.id) in pt.keys() and pt[str(interaction.user.id)] >= montant:
		pt[str(interaction.user.id)] -= montant
		if str(member.id) in pt.keys():
			pt[str(member.id)] += montant
		else:
			pt[str(member.id)] = montant
		with open ('points.json','w') as f:
			json.dump(pt,f,indent=6)
		await interaction.response.send_message(f'Vous avez payé {montant} points à {member.mention}')
	else:
		await interaction.response.send_message(f'''Vous n'avez pas assez de DreamPoints pour faire cela''')

"""@bot.tree.command()
async def claimpoints(interaction: discord.Interaction,nombre:int,motif:str,preuve:typing.Optional[str]):
	if interaction.channel.id != 811653993033891870:
		await interaction.response.send_message('Vous ne pouvez utiliser cette commande que dans le <#811653993033891870>',ephemeral=True)
		return
	with open ('points.json','r') as f:
		pt = json.load(f)
	if str(interaction.user.id) in pt.keys():
		pt[str(interaction.user.id)] += nombre
	else:
		pt[str(interaction.user.id)] = nombre
	with open ('equipes.json','r') as f:
		eq = json.load(f)
	for role in eq.keys():
		if int(role) in [t.id for t in member.roles]:
			eq[role]['total'] += cat[catalogue]
			if str(member.id) in eq[role].keys():
				eq[role]['membres'][str(member.id)] += cat[catalogue]
			else:
				eq[role]['membres'][str(member.id)] = cat[catalogue]
	for role in eq.keys():
		if int(role) in [t.id for t in interaction.user.roles]:
			eq[role] += nombre
	with open ('equipes.json','w') as f:
		json.dump(eq,f,indent=6)
	with open ('points.json','w') as f:
		json.dump(pt,f,indent=6)
	logs = interaction.guild.get_channel(1026567820311531550)
	await logs.send(f'{interaction.user.mention} à demandé `{nombre}` points pour {motif} {"(preuve : "+preuve+")" if preuve !=None else ""}')
	await interaction.response.send_message(f'''{nombre} points vous ont été donnés.\n__**ATTENTION !**__ Une verification sera faite bientot et si ces points ne sont pas légitimes vous serez lourdement sanctionnés.\nSi c'est une erreur ou un test, veuillez contacter un hg le plus rapidement possible''')

 @bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def blbl(interaction: discord.Interaction):
	with open ('points.json','r') as f:
		pt = json.load(f)
	with open('voc.json','r') as f:
		voc = json.load(f)
	Roles = [[790675782338740235,48600],[790675782364037131,39600],[790675783352975360,31500],[790675783549976579,24300],[790675783693500456,18000],
			 [790675784120401932,12600],[790675784225521734,8100],[791066206437113897,4500],[791066207418712094,1800],[791066206109958204,0],[1011953852427272302,0]]
	for personne in voc['total'].items():
		role = None
		role2 = None
		mem = interaction.guild.get_member(int(personne[0]))
		if mem != None:
			for x in Roles:
				if x[0] in [t.id for t in mem.roles]:
					pt[str(mem.id)] = 3*(personne[1] - x[1])
	with open ('points.json','w') as f:
		json.dump(pt,f,indent=6)
	await interaction.response.send_message('Finito') """

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def addpoints(interaction: discord.Interaction,membre:discord.Member,nombre:int,motif:str,preuve:typing.Optional[str]):
	'''Donner (créer) des dreampoints à un membre. Commande réservée aux HG'''
	with open ('points.json','r') as f:
		pt = json.load(f)
	if str(membre.id) in pt.keys():
		pt[str(membre.id)] += nombre
	else:
		pt[str(membre.id)] = nombre
	with open ('equipes.json','r') as f:
		eq = json.load(f)
	for role in eq.keys():
		if int(role) in [t.id for t in membre.roles]:
			eq[role]['total'] += nombre
			if str(membre.id) in eq[role]['membres'].keys():
				eq[role]['membres'][str(membre.id)] += nombre
			else:
				eq[role]['membres'][str(membre.id)] = nombre
	with open ('equipes.json','w') as f:
		json.dump(eq,f,indent=6)
	with open ('points.json','w') as f:
		json.dump(pt,f,indent=6)
	logs = interaction.guild.get_channel(1026567820311531550)
	await logs.send(f'{interaction.user.mention} à donné `{nombre}` points à {membre.mention} pour {motif} {"(preuve : "+preuve+")" if preuve !=None else ""}')
	await interaction.response.send_message(f'''{nombre} points ont été donnés à {membre.mention}.''')

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def removepoints(interaction: discord.Interaction,membre:discord.Member,nombre:int,motif:str,preuve:typing.Optional[str]):
	'''Retirer (supprimer) des dreampoints à un membre. Commande réservée aux HG'''
	with open ('points.json','r') as f:
		pt = json.load(f)
	if str(membre.id) in pt.keys():
		pt[str(membre.id)] -= nombre
	else:
		pt[str(membre.id)] = -nombre
	with open ('equipes.json','r') as f:
		eq = json.load(f)
	for role in eq.keys():
		if int(role) in [t.id for t in membre.roles]:
			eq[role]['total'] -= nombre
			if str(membre.id) in eq[role]['membres'].keys():
				eq[role]['membres'][str(membre.id)] -= nombre
			else:
				eq[role]['membres'][str(membre.id)] = -nombre
	with open ('equipes.json','w') as f:
		json.dump(eq,f,indent=6)
	with open ('points.json','w') as f:
		json.dump(pt,f,indent=6)
	logs = interaction.guild.get_channel(1026567820311531550)
	await logs.send(f'{interaction.user.mention} à retiré `{nombre}` points à {membre.mention} pour {motif} {"(preuve : "+preuve+")" if preuve !=None else ""}')
	await interaction.response.send_message(f'''{nombre} points ont été retirés à {membre.mention}.''')

@bot.tree.command()
async def achatdp(interaction: discord.Interaction):
	'''Acheter une récompense avec des DP'''
	if interaction.channel.id != 811653993033891870:
		await interaction.response.send_message('Vous ne pouvez utiliser cette commande que dans le <@#811653993033891870>',ephemeral=True)
		return
	await interaction.response.send_message('Que voulez-vous acheter ?',ephemeral=True,view=achatdpp())
	
	
	'''ach = {'Rankup Penseur':[791066207418712094,10000],'Rankup Maitre penseur':[791066206437113897,15000],'Rankup Inventeur':[790675784225521734,20000],
					'Rankup Utopiste':[790675784120401932,30000],'Rankup Songeur':[790675783693500456,40000],'Rankup Dreamer':[790675783549976579,50000],
					'Rankup Chimère':[790675783352975360,70000],'Rankup Fantaisiste':[790675782364037131,90000],'Rankup Idéaliste':[790675782338740235,110000], 'Grade Perso':20000, 'Emoji Perso':20000}
	salon = interaction.guild.get_channel(1034854483911512115)
	if achat not in ach.keys():
		await interaction.response.send_message("L'achat spécifié n'est pas correct, veuillez acheter : ``Rankup Penseur/Maitre penseur/etc``, ``Grade Perso``, ``Emoji Perso`` ou ``Commande Perso``")
		return
	
	if achat[:6] == 'Rankup':
		await salon.send(f"{interaction.user.mention} veut passer <@&{ach[achat][0]}>")
	else:
		'''

class achadp(discord.ui.Select):
	def __init__(self):
		options=[discord.SelectOption(label='Rankup',description='Prix variable',value='Rankup',emoji="\u2705"),
				discord.SelectOption(label='Grade perso',description='20.000 DP',value='Grade perso',emoji='<:Brisestorm:1024423730585276486>'),
				discord.SelectOption(label='Emoji perso',description='20.000 DP',value='Emoji perso',emoji='<:derp:804803664824238080>')]
		super().__init__(placeholder='Achats', min_values=1, max_values=1, options=options, custom_id='achdp')
	async def callback(self, interaction: discord.Interaction):
		if self.values[0] == 'Rankup':
			rank = {791066207418712094:10000,791066206437113897:15000,790675784225521734:20000,790675784120401932:30000,790675783693500456:40000,
			790675783549976579:50000,790675783352975360:70000,790675782364037131:90000,790675782338740235:110000}
			guild = interaction.guild
			Roles = {9:790675782338740235,8:790675782364037131,7:790675783352975360,6:790675783549976579,5:790675783693500456,4:790675784120401932,3:790675784225521734,2:791066206437113897, 1:791066207418712094}
			for x in Roles.items():
				rol = guild.get_role(x[1])
				if rol in interaction.user.roles:
					role = x[0]
			try:
				role = role
			except:
				await interaction.response.send_message(":warning: Une erreur s'est produite ! <@790574682294190091> Aled")
				return
			if role+1 == 10:
				await interaction.response.send_message('Vous ne pouvez pas rankup car vous êtes déjà au rôle maximal !',ephemeral=True)
				return
			role_voulu = guild.get_role(Roles[role+1])
			await interaction.response.send_message(f"Confirmez-vous l'achat du rank {role_voulu.mention} pour {rank[role_voulu.id]} DP ?",ephemeral=True,view=confach(f'Rankup {role_voulu.mention}',rank[role_voulu.id]))
		elif self.values[0] == 'Grade perso' or self.values[0] == 'Emoji perso':
			await interaction.response.send_modal(emojgr(self.values[0]))

class emojgr(discord.ui.Modal, title='Demande de recompense personalisée'):
    def __init__(self,voeu) -> None:
        super().__init__()
        self.nom = discord.ui.TextInput(
        	label='''Quel nom voulez-vous lui donner ?''',
        	placeholder=f'''Nom''')
        self.add_item(self.nom)
        self.coul = discord.ui.TextInput(
        	label='''Quelle couleur voulez-vous lui donner ?''',
        	placeholder=f'''Couleur''')
        self.add_item(self.coul)
        self.emo = discord.ui.TextInput(
        	label='''Quel emoji voulez-vous lui donner ?''',
        	placeholder=f'''Emoji''')
        self.add_item(self.emo)
        self.voeu = voeu
    async def on_submit(self, interaction: discord.Interaction):
        with open ('points.json','r') as f:
            pt = json.load(f)
        if str(interaction.user.id) in pt.keys() and pt[str(interaction.user.id)] >= 20000:
            pt[str(interaction.user.id)] -= 20000
        else:
            await interaction.response.send_message("Vous n'avez pas assez de points pour cela !",ephemeral=True)
            return
        salon = interaction.guild.get_channel(1034854483911512115)
        await salon.send(f"{interaction.user.mention} veut un {self.voeu} :\n- Nom : {self.nom}\n- Couleur : {self.coul}\n- Emoji : {self.emo}")
        with open ('points.json','w') as f:
            json.dump(pt,f,indent=6)
        await interaction.response.send_message(f''':white_check_mark: Votre demande d'achat d'un {self.voeu} à correctement été envoyée au Staff.''',ephemeral=True)
    #async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
    #    await interaction.response.send_message('Il y a eu un problème', ephemeral=True)

class achatdpp(discord.ui.View):
	def __init__(self, *, timeout: Optional[float] = 180):
		super().__init__(timeout=timeout)
		self.add_item(achadp())

class confach(discord.ui.View):
	def __init__(self,voeu,prix) -> None:
		super().__init__(timeout=None)
		self.voeu = voeu
		self.prix = prix
	@discord.ui.button(label="Confirmer", style=discord.ButtonStyle.green, custom_id='confach',emoji="\u2705")
	async def actu(self, interaction: discord.Interaction, button: discord.ui.Button):
		with open ('points.json','r') as f:
			pt = json.load(f)
		if str(interaction.user.id) in pt.keys() and pt[str(interaction.user.id)] >= int(str(self.prix)):
			pt[str(interaction.user.id)] -= int(str(self.prix))
		else:
			await interaction.response.send_message("Vous n'avez pas assez de points pour cela !",ephemeral=True)
			return
		salon = interaction.guild.get_channel(1034854483911512115)
		await salon.send(f"{interaction.user.mention} veut un {self.voeu}")
		with open ('points.json','w') as f:
			json.dump(pt,f,indent=6)
		await interaction.response.send_message(f"Votre demande d'achat de {self.voeu} à été prise en compte. Sachez qu'elle peut etre rejetée si :\n- Vous avez récemment enfreint le règlement\n- un hg à mis son véto sur votre demande\nPour les rankups :\n- Vous demandez plus de trois rankups a la fois\n- Vous n'avez pas le rang nécéssaire au rankup suivant\n\nSi votre demande est refusée vous en serez avertis et vos points seront remboursés, sinon vous serez rankup lors de la prochaine vague.\n\n",ephemeral=True)

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
@discord.app_commands.checks.cooldown(1, 604800)
async def sleep(interaction: discord.Interaction) -> None:
	'''Dormez pour recuperer des DP toutes les semaines ! Offre entre 100 et 200 DP.'''
	nombre = random.randint(100,200)
	with open ('points.json','r') as f:
		pt = json.load(f)
	if str(interaction.user.id) in pt.keys():
		pt[str(interaction.user.id)] += nombre
	else:
		pt[str(interaction.user.id)] = nombre
	with open ('equipes.json','r') as f:
		eq = json.load(f)
	for role in eq.keys():
		if int(role) in [t.id for t in interaction.user.roles]:
			eq[role]['total'] += nombre
			if str(interaction.user.id) in eq[role]['membres'].keys():
				eq[role]['membres'][str(interaction.user.id)] += nombre
			else:
				eq[role]['membres'][str(interaction.user.id)] = nombre
	with open ('equipes.json','w') as f:
		json.dump(eq,f,indent=6)
	with open ('points.json','w') as f:
		json.dump(pt,f,indent=6)
	logs = interaction.guild.get_channel(1026567820311531550)
	await logs.send(f'{interaction.user.mention} à gagné `{nombre}` points pour  avoir /sleep')
	await interaction.response.send_message(f'''Vous avez gagné {nombre} points !''')

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
@discord.app_commands.checks.cooldown(1, 86400)
async def work(interaction: discord.Interaction) -> None:
	'''Travaillez pour recuperer des DP tous les jours ! Offre entre 5 et 25 DP.'''
	nombre = random.randint(5,25)
	with open ('points.json','r') as f:
		pt = json.load(f)
	if str(interaction.user.id) in pt.keys():
		pt[str(interaction.user.id)] += nombre
	else:
		pt[str(interaction.user.id)] = nombre
	with open ('equipes.json','r') as f:
		eq = json.load(f)
	for role in eq.keys():
		if int(role) in [t.id for t in interaction.user.roles]:
			eq[role]['total'] += nombre
			if str(interaction.user.id) in eq[role]['membres'].keys():
				eq[role]['membres'][str(interaction.user.id)] += nombre
			else:
				eq[role]['membres'][str(interaction.user.id)] = nombre
	with open ('equipes.json','w') as f:
		json.dump(eq,f,indent=6)
	with open ('points.json','w') as f:
		json.dump(pt,f,indent=6)
	logs = interaction.guild.get_channel(1026567820311531550)
	await logs.send(f'{interaction.user.mention} à gagné `{nombre}` points pour  avoir /work')
	await interaction.response.send_message(f'''Vous avez gagné {nombre} points !''')

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
@discord.app_commands.checks.cooldown(1, 3600)
async def crime(interaction: discord.Interaction) -> None:
	'''Volez des DP toutes les heures, mais faites attention a la police ! Offre entre -10 et 15 DP.'''
	nombre = random.randint(-10,15)
	with open ('points.json','r') as f:
		pt = json.load(f)
	if str(interaction.user.id) in pt.keys():
		pt[str(interaction.user.id)] += nombre
	else:
		pt[str(interaction.user.id)] = nombre
	with open ('equipes.json','r') as f:
		eq = json.load(f)
	for role in eq.keys():
		if int(role) in [t.id for t in interaction.user.roles]:
			eq[role]['total'] += nombre
			if str(interaction.user.id) in eq[role]['membres'].keys():
				eq[role]['membres'][str(interaction.user.id)] += nombre
			else:
				eq[role]['membres'][str(interaction.user.id)] = nombre
	with open ('equipes.json','w') as f:
		json.dump(eq,f,indent=6)
	with open ('points.json','w') as f:
		json.dump(pt,f,indent=6)
	logs = interaction.guild.get_channel(1026567820311531550)
	await logs.send(f'{interaction.user.mention} à gagné `{nombre}` points pour  avoir /crime')
	await interaction.response.send_message(f'''Vous avez {f'gagné {nombre}' if nombre >= 0 else f'perdu {-nombre}'} points !''')

@bot.tree.command()
async def classement(interaction: discord.Interaction):
	'''Voir le classement du Festivau'''
	if interaction.channel.id not in [811653993033891870,791452088370069525,1037477592573415545,1037478755821686864]:
		await interaction.response.send_message('Vous ne pouvez utiliser cette commande que dans le <#811653993033891870>',ephemeral=True)
		return
	with open('equipes.json','r') as f:
		eq = json.load(f)
	roles = [interaction.guild.get_role(int(t)) for t in eq.keys()]
	dic = {}
	for role in roles:
		dic[role.id] = len(role.members)
	s = sorted(dic,key = lambda t : dic[t],reverse=True)
	y = ['🥇 **__1er :__**','🥈 **__2eme :__**','🥉 **__3eme :__**'] + [f'**__{i}eme :__**' for i in range(4,len(s)+1)]
	msg = f'__**Equipe la plus choisie :**__\n\n'
	for i in range(len(s)):
		msg += f"{y[i]} <@&{s[i]}> *({dic[s[i]]} membres)*\n\n"
	dic = {}
	for role in roles:
		dic[role.id] = eq[str(role.id)]['total']/len(role.members)
	msg += '\n**__Moyenne de points la plus haute :__**\n\n'
	s = sorted(dic,key = lambda t : dic[t],reverse=True)
	for i in range(len(s)):
		msg += f"{y[i]} <@&{s[i]}> *({round(dic[s[i]])} points par personne)*\n\n"
	dic = {}
	for role in roles:
		s = sorted(eq[str(role.id)]['membres'],key=lambda o : eq[str(role.id)]['membres'][o],reverse=True)
		dic[role.id] = [eq[str(role.id)]['membres'][s[0]],s[0]]
	msg += '\n**__Plus gros farmeur :__**\n\n'
	s = sorted(dic,key = lambda t : dic[t][0],reverse=True)
	for i in range(len(s)):
		msg += f"{y[i]} <@&{s[i]}> *({round(dic[s[i]][0])} points max par <@{dic[s[i]][1]}>)*\n\n"
	await interaction.response.send_message(embed=discord.Embed(title=f'Classement',description=msg,timestamp=datetime.now()),view=actu())

class actu(discord.ui.View):
	def __init__(self) -> None:
		super().__init__(timeout=None)
	@discord.ui.button(label="Actualiser", style=discord.ButtonStyle.green, custom_id='actual',emoji="\U0001f504")
	async def actu(self, interaction: discord.Interaction, button: discord.ui.Button):
		with open('equipes.json','r') as f:
			eq = json.load(f)
		roles = [interaction.guild.get_role(int(t)) for t in eq.keys()]
		dic = {}
		for role in roles:
			dic[role.id] = len(role.members)
		s = sorted(dic,key = lambda t : dic[t],reverse=True)
		y = ['🥇 **__1er :__**','🥈 **__2eme :__**','🥉 **__3eme :__**'] + [f'**__{i}eme :__**' for i in range(4,len(s)+1)]
		msg = f'__**Equipe la plus choisie :**__\n\n'
		for i in range(len(s)):
			msg += f"{y[i]} <@&{s[i]}> *({dic[s[i]]} membres)*\n\n"
		dic = {}
		for role in roles:
			dic[role.id] = eq[str(role.id)]['total']/len(role.members)
		msg += '\n**__Moyenne de points la plus haute :__**\n\n'
		s = sorted(dic,key = lambda t : dic[t],reverse=True)
		for i in range(len(s)):
			msg += f"{y[i]} <@&{s[i]}> *({round(dic[s[i]])} points par personne)*\n\n"
		dic = {}
		for role in roles:
			s = sorted(eq[str(role.id)]['membres'],key=lambda o : eq[str(role.id)]['membres'][o],reverse=True)
			dic[role.id] = [eq[str(role.id)]['membres'][s[0]],s[0]]
		msg += '\n**__Plus gros farmeur :__**\n\n'
		s = sorted(dic,key = lambda t : dic[t][0],reverse=True)
		for i in range(len(s)):
			msg += f"{y[i]} <@&{s[i]}> *({round(dic[s[i]][0])} points max par <@{dic[s[i]][1]}>)*\n\n"
		await interaction.response.edit_message(embed=discord.Embed(title=f'Classement',description=msg,timestamp=datetime.now()),view=actu())

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def adminclassement(interaction: discord.Interaction):
	'''Voir le classement des DP. Commande réservée aux HG'''
	with open('points.json','r') as f:
		pt = json.load(f)
	s = sorted(pt,key = lambda t : pt[t],reverse=True)
	msg = ""
	if len(s) < 20:
		for i in range(len(s)):
			msg += f'{i+1} : <@{s[i]}> - ({pt[s[i]]})\n'
	else:
		for i in range(20):
			msg += f'{i+1} : <@{s[i]}> - ({pt[s[i]]})\n'
	await interaction.response.send_message(embed=discord.Embed(title=f'Page 1',description=msg),view=pagecl())

class pagecl(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
	@discord.ui.button(label="Page précédente", style=discord.ButtonStyle.red, custom_id='prec')
	async def prec(self, interaction: discord.Interaction, button: discord.ui.Button):
		for element in interaction.message.embeds:
			tir = int(element.title[-1])
		if tir == 1:
			await interaction.response.send_message('Vous êtes déjà à la première page',ephemeral=True)
			return
		with open('points.json','r') as f:
			pt = json.load(f)
		msg = ''
		s = sorted(pt,key = lambda t : pt[t],reverse=True)
		for i in range((tir-2)*20,(tir-1)*20):
			msg += f'{i+1} : <@{s[i]}> - ({pt[s[i]]})\n'
		await interaction.message.edit(embed=discord.Embed(title=f'Page {tir-1}',description=msg))
		await interaction.response.send_message('Message modifié',ephemeral=True)
	@discord.ui.button(label="Page suivante", style=discord.ButtonStyle.green, custom_id='suiv')
	async def suiv(self, interaction: discord.Interaction, button: discord.ui.Button):
		for element in interaction.message.embeds:
			tir = int(element.title[-1])
		with open('points.json','r') as f:
			pt = json.load(f)
		if tir*20 >= len(pt.keys()):
			await interaction.response.send_message('Vous êtes déjà à la dernière page',ephemeral=True)
			return
		msg = ''
		s = sorted(pt,key = lambda t : pt[t],reverse=True)
		if len(pt.keys()) < (tir+1)*20:
			for i in range(tir*20,len(pt.keys())):
				msg += f'{i+1} : <@{s[i]}> - ({pt[s[i]]})\n'
		else:
			for i in range(tir*20,(tir+1)*20):
				msg += f'{i+1} : <@{s[i]}> - ({pt[s[i]]})\n'
		await interaction.message.edit(embed=discord.Embed(title=f'Page {tir+1}',description=msg))
		await interaction.response.send_message('Message modifié',ephemeral=True)

class auto(discord.ui.Select):
	def __init__(self,roles):
		options=[discord.SelectOption(label=str(t.name),value=t.id,emoji=t.unicode_emoji) for t in roles]
		super().__init__(placeholder='Auto Rôles', min_values=1, max_values=1, options=options, custom_id='autor')
	async def callback(self, interaction: discord.Interaction):
		guild = bot.get_guild(790367917812088864)
		t = guild.get_role(int(str(self.values[0])))
		if t in interaction.user.roles:
			await interaction.user.remove_roles(t)
			await interaction.response.send_message('Rôle retiré !',ephemeral=True)
		else:
			await interaction.user.add_roles(t)
			await interaction.response.send_message('Rôle ajouté !',ephemeral=True)

class fest(discord.ui.Select):
	def __init__(self,roles):
		options=[discord.SelectOption(label=str(t.name),value=t.id,emoji=t.unicode_emoji) for t in roles]
		super().__init__(placeholder='Rôles Festivau', min_values=1, max_values=1, options=options, custom_id='fest')
	async def callback(self, interaction: discord.Interaction):
		if 791066206109958204 in [x.id for x in interaction.user.roles]:
			await interaction.response.send_message('Seuls les membres officiels de la faction peuvent obtenir un role du Festivau',ephemeral=True)
			return
		with open('equipes.json','r') as f:
			eq = json.load(f)
		for y in eq.keys():
			if int(y) in [t.id for t in interaction.user.roles]:
				await interaction.response.send_message('Vous avez déjà un rôle de ce festivau !',ephemeral=True)
				return
		guild = bot.get_guild(790367917812088864)
		t = guild.get_role(int(str(self.values[0])))
		await interaction.user.add_roles(t)
		await interaction.response.send_message('Rôle ajouté !',ephemeral=True)

class autoview(discord.ui.View):
	def __init__(self,options,roles):
		super().__init__(timeout=None)
		self.add_item(auto(options))
		self.add_item(fest(roles))

async def majauto():
	with open('warnblame.json','r') as f:
		au = json.load(f)
	with open('equipes.json','r') as f:
		eq = json.load(f)
	msg = '___***Auto Rôles :***___\n'
	for t in au['autoroles']:
		msg += f'- <@&{t}>\n'
	msg += '\n___***Rôles du festivau***___\n'
	for t in eq.keys():
		msg += f'- <@&{t}>\n'
	guild = bot.get_guild(790367917812088864)
	options = []
	for i in au['autoroles']:
		t = guild.get_role(int(i))
		options.append(t)
	roles = []
	for i in eq.keys():
		t = guild.get_role(int(i))
		roles.append(t)
	return [discord.Embed(title=f'Rôles Automatiques',description=msg),options,roles]

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def majroleauto(interaction: discord.Interaction,channel:discord.TextChannel,message:str):
	'''Mettre à jour les rôles automatiques. Commande réservée aux HG'''
	message = channel.get_partial_message(message)
	t = await majauto()
	await message.edit(embed=t[0],view=autoview(t[1],t[2]))
	await interaction.response.send_message('Fait')

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def sendroleauto(interaction: discord.Interaction):
	'''Envoyer le message pour prendre les rôles automatiques. Commande réservée aux HG'''
	t = await majauto()
	await interaction.response.send_message(embed=t[0],view=autoview(t[1],t[2]))

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def addroleauto(interaction: discord.Interaction,role_id:str):
	'''Ajouter un rôle automatique. Commande réservée aux HG'''
	with open('warnblame.json', 'r') as f:
		au = json.load(f)
	au["autoroles"].append(int(role_id))
	with open ('warnblame.json','w') as f:
		json.dump(au,f,indent=6)
	await interaction.response.send_message('Fait')

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def removeroleauto(interaction: discord.Interaction,role_id:str):
	'''Retirer un rôle automatique. Commande réservée aux HG'''
	with open('warnblame.json', 'r') as f:
		au = json.load(f)
	au["autoroles"].remove(int(role_id))
	with open ('warnblame.json','w') as f:
		json.dump(au,f,indent=6)
	await interaction.response.send_message('Fait')

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator=True)
async def newfest(interaction: discord.Interaction,equipes:str):
	'''Commencer un nouveau festivau. Coller les équipes avec "_" et les séparer par un espace. Commande réservée aux HG'''
	with open('equipes.json','r') as f:
		eq = json.load(f)
	for rol in eq.keys():
		role = interaction.guild.get_role(int(rol))
		await role.delete()
	eq = {}
	guild = bot.get_guild(790367917812088864)
	for element in equipes.rsplit():
		rol = await guild.create_role(name=f'『⚔️』Equipe {element}')
		eq[str(rol.id)] = {"total":0,"membres":{}}
	with open ('equipes.json','w') as f:
		json.dump(eq,f,indent=6)
	await interaction.response.send_message('Fait')

# =========== Blacklist ==========

class bl(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="Envoyer une demande de blacklist", style=discord.ButtonStyle.green, custom_id='bl')
    async def bl(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(demandebl())

@bot.tree.command()
async def demande_bl(interaction: discord.Interaction) -> None:
    '''Envoyer le formulaire pour faire une demande de blacklist.'''
    await interaction.response.send_message(embed = create_embed('```​📌​ ‒ Demande de Blacklist```',f'''
                           Bonjour __{interaction.user.mention}__,
                           
                           Sachez tout d'abord qu'en cliquant sur ce bouton, vous devrez répondre à 5 questions.
                           
                           • Toutes demandes troll ou visant à ne pas faire une vraie demande, seront sanctionnées.
						   
						   Le staff SweetDream''',0xffffff),view=bl())

class demandebl(discord.ui.Modal, title='Demande de blacklist'):
    ide = discord.ui.TextInput(
        label='''Quel est l'id de la personne à blacklist''',# souhaitez blacklister ?
        placeholder=f'''Pour recuperer l'id, faites click droit -> Copier ID''',
    )
    nom = discord.ui.TextInput(
        label='''Quel est son nom ?''',
        placeholder=f'''Marquer ici son nom discord avec son #''',
    )
    uuid = discord.ui.TextInput(
        label='''Quel est son UUID ? (sur https://namemc.com/)''',
        placeholder=f'''Pour trouver l'UUID mettez son pseudo sur https://namemc.com/''',
		style=discord.TextStyle.paragraph
    )
    raison = discord.ui.TextInput(
        label='''Pour quelle raison voulez vous la blacklist ?''',
        placeholder=f'''Marquer ici la/les raison.s''',
    )
    preuves = discord.ui.TextInput(
        label='Vos Preuves',
        style=discord.TextStyle.long,
        placeholder='Merci de mettre ici toutes les preuves récoltées (vidéos youtube, liens vers des screens, etc)',
    )

    async def on_submit(self, interaction: discord.Interaction):
        data = requests.get(f"https://sessionserver.mojang.com/session/minecraft/profile/{self.uuid.value}").json()
        embed = create_embed(f'```​📌​ ‒ Demande de Blacklist```',f'''
                              Auteur de la demande : `{interaction.user.name}#{interaction.user.discriminator}` (*{interaction.user.id}*)
                              Joueur à Blacklister : {self.nom.value} (*`{self.ide.value}`*)
                              Pseudo IG : `{data["name"]}` (`{self.uuid.value}`)                         
                              Raison de la demande : `{self.raison.value}`
                              Preuves fournies : `{self.preuves.value}`''',0xffffff)
        await interaction.user.send(embed = embed)
        channel = bot.get_channel(794021749196718121)
        msg = await channel.send(f'''__@everyone__ \​​📬​ Nouvelle demande''',embed = embed,view=blaccept())
        with open('blacklist.json', 'r') as f:
            bl = json.load(f)
        bl["Attente"][msg.id] = [interaction.user.id,self.ide.value,self.uuid.value,self.raison.value,self.preuves.value,self.nom.value]
        with open('blacklist.json', 'w') as f:
            json.dump(bl, f, indent=6)
        await interaction.response.send_message(f''':white_check_mark: Votre demande à correctement été envoyée au Staff.''',ephemeral=True) 
    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Il y a eu un problème', ephemeral=True)

class blaccept(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="Accepter la demande de blacklist", style=discord.ButtonStyle.green, custom_id='bla')
    async def bl(self, interaction: discord.Interaction, button: discord.ui.Button):
        with open('blacklist.json', 'r') as f:
            bl = json.load(f)
        user = bl["Attente"][str(interaction.message.id)][1]
        bl["black"][user] = bl["Attente"][str(interaction.message.id)][2:]
        bl["Attente"].pop(str(interaction.message.id))
        with open('blacklist.json', 'w') as f:
            json.dump(bl, f, indent=6)
        await interaction.message.edit(view=None)
        await interaction.response.send_message(f'Vous avez ajouté <@{user}> à la blacklist avec succès !')
    @discord.ui.button(label="Refuser la demande de blacklist", style=discord.ButtonStyle.red, custom_id='nonbl')
    async def nonbl(self, interaction: discord.Interaction, button: discord.ui.Button):
        with open('blacklist.json', 'r') as f:
            bl = json.load(f)
        user = bl["Attente"][str(interaction.message.id)][1]
        bl["Attente"].pop(str(interaction.message.id))
        with open('blacklist.json', 'w') as f:
            json.dump(bl, f, indent=6)
        await interaction.message.edit(view=None)
        await interaction.response.send_message(f"Vous n'avez pas ajouté {user} à la blacklist")

class actu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="Actualiser", style=discord.ButtonStyle.green, custom_id='actu',emoji='<a:TR_Online:1005062612138066010>')
    async def actu(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.message.edit(embed = await embed_blacklist(interaction.guild,interaction.user))
        await interaction.response.send_message('La blacklist à été actualisée',ephemeral=True) 


@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator = True)
async def blacklist(interaction: discord.Interaction) -> None:
    '''Envoyer la blacklist. Commande réservée aux HG'''
    await interaction.response.send_message(embed = await embed_blacklist(interaction.guild,interaction.user), view=actu())

async def embed_blacklist(guild,user):
    with open('blacklist.json','r') as f:
        bl = json.load(f)
    msg = ''
    for pers in bl['black'].keys():
        if bl['black'][pers][0] == "":
            data = {"name":"Aucun pseudo connu"}
        else:
            data = requests.get(f"https://sessionserver.mojang.com/session/minecraft/profile/{bl['black'][pers][0]}").json()
        msg += f'''\📌 | **{bl['black'][pers][3]}** *(<@{pers}>)*\n\💻 | `{data["name"]}` ({bl['black'][pers][0]})\n> __{bl['black'][pers][1]}__\n\n'''
    embed = discord.Embed(title = 'Blacklist V8.5',
                          description = msg,
                          timestamp = datetime.now(),
                          color = 0xc18fff)
    embed.set_author(name = f'Blacklist | {guild.name}', icon_url = guild.icon.url)
    embed.set_footer(text = f'Dernière actualisation par {user.name}#{user.discriminator}')
    return embed

@bot.tree.command()
@discord.app_commands.checks.has_permissions(administrator = True)
async def purge(interaction: discord.Interaction) -> None:
	'''Retirer les personnes parties de la fac du classement des DP. Commande réservée aux HG'''
	await interaction.response.defer()
	with open ('points.json','r') as f:
		pt = json.load(f)
	p = []
	for memb in pt.keys():
		membe = interaction.guild.get_member(int(memb))
		if membe == None or await infac(membe)==False:
			p.append(memb)
	for memb in p:
		pt.pop(memb)
	with open ('points.json','w') as f:
		json.dump(pt,f,indent=6)
	await interaction.followup.send('ok')

# =========== Autre ===========

@bot.tree.command()
@discord.app_commands.checks.cooldown(1, 480)
async def bug_report(interaction: discord.Interaction,bug:str) -> None:
	'''Report un bug.'''
	await interaction.response.defer()
	channel_send_bug = bot.get_channel(791452088370069525)
	embed = discord.Embed(description = f''':bookmark_tabs: | **Bug** : `{bug}`
	
	>  :astronaut_tone1: | **Report de** : `{interaction.user.name}`
	>  :robot: | **ID** : `{interaction.user.id}`''')
	embed.set_author(name = f'Report de {interaction.user}', icon_url = interaction.user.avatar.url)
	embed.set_thumbnail(url = interaction.guild.icon.url)
	embed.timestamp = datetime.now()
	await channel_send_bug.send(embed = embed)
	await interaction.followup.send(f'''Votre report à bien été signalé au staff, merci de participer à l'amélioration du bot !''')

class NewHelpCommand(commands.MinimalHelpCommand):
	async def send_pages(self):
		destination = self.context.author
		guild = self.context.guild
		message = "__*help__ : Voir cette page"
		recrutements = guild.get_role(791426367362433066)
		resp = guild.get_role(790675781789155329)
		Chef = guild.get_role(790675782569164820)
		reveur = guild.get_role(821787385636585513)
		vendeur = guild.get_role(960180290683293766)
		if recrutements in destination.roles or Chef in destination.roles or reveur in destination.roles:
			message += "\n\n__**=== Recrutements ===**__" \
					   "\n> __***refuse** membre raison__ : Refuser un membre qui a fait une candidature" \
					   "\n> __***accept** membre__ : Accepter un membre qui a fait une candidature" \
					   "\n> __***oralyes** membre__ : Accepter une personne ayant fait un entretien" \
					   "\n> __***oralno** membre__ : Refuser une personne ayant fait un entretien"
			if resp in destination.roles or Chef in destination.roles or reveur in destination.roles:
				message += "\n> __***addtime** membre (temps)__ : Ajouter du temps à une personne en attente d'entretien" \
						   "\n> __***finphases** membre__ : Faire entrer une personne ayant fini ses phases dans la faction" \
						   "\n> __***kickphases** membre (raison)__ : Retirer une personne des phases"
		message += "\n\n__**=== Economie ===**__" \
				   '\n> __***creercompte**__ : Créer votre compte (marche aussi avec "createaccount","openaccount","ouvrircompte") ' \
				   '\n> __***money**__ : Consulter votre solde actuel (marche aussi avec "balance","bal") ' \
				   "\n> __***pay** membre montant__ : Payer quelqu'un"
		if vendeur in destination.roles or Chef in destination.roles or reveur in destination.roles:
			message += "\n> __***claim**__ : Prendre en charge une commande" \
					   "\n> __***livre**__ : Declarer la livraison d'une commande"
			if resp in destination.roles or Chef in destination.roles or reveur in destination.roles:
				message += "\n> __***adminaddmoney** membre__ : Ajouter de l'argent à quelqu'un (marche aussi avec \"adminpay\",\"admingive\",\"add\ et \"give\")" \
						   "\n> __***adminremovemoney** membre__ : Retirer de l'argent à quelqu'un (marche aussi avec \"remove\") "
		if Chef in destination.roles or reveur in destination.roles:
			message += "\n\n__**=== HG ===**__" \
			"\n> __***warn** membre (raison)__ : Warn un membre" \
			"\n> __***unwarn** member (numéro) (raison)__ : Retirer le warn d'un membre" \
			"\n> __***blame** membre (raison)__ : Blamer un membre" \
			"\n> __***unblame** membre (numéro) (raison)__ : Retirer le blame d'un membre" \
			"\n> __***rankup** membre __ : Rankup un membre" \
			"\n> __***derank** membre (raison)__ : Derank un membre" \
			"\n> __***ban** membre (raison)__ : Bannir un membre" \
			"\n> __***unban** membre__ : Débannir un membre" \
			"\n> __***sanctions** membre__ : Consulter les sanctions d'un joueur" \
			"\n> __***prepare**__ : Prepare le système de tickets" \
			"\n> __***close**__ : Fermer un ticket"
		embed = discord.Embed(
			title="Commande Help",
			description=message,
			color=discord.Color.blue()
		)
		await destination.send(embed=embed)

bot.help_command = NewHelpCommand()

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	with open('Interview.json', 'r') as f:
		interviews = json.load(f)
	if isinstance(message.channel, discord.DMChannel): # dont allow dm channel
		anino = await bot.fetch_user(790574682294190091)
		await anino.send(f'message de {message.author.mention} ({message.author.name}) : {message.content}')
		if str(message.author.id) in list(interviews['Wait']):
			interviews['Wait'].pop(str(message.author.id))
			interviews['Responded'][message.author.id] = str(datetime.utcnow())
			with open('Interview.json', 'w') as f:
				json.dump(interviews, f, indent=6)
			log = await bot.fetch_channel(937312061833240586)
			await log.send(embed=discord.Embed(
				title='Demande de ralonge de temps :',
				description=f'User: {message.author.mention}\n{message.content}',
				color=discord.Color.magenta()
			))
		if message.content.startswith('SD'):
			await message.author.send("Vous ne pouvez pas m'utiliser en message privé !")
		return
	bonj = bot.get_channel(811653900611354704)
	if message.channel == bonj:
		if message.content.lower()[:11] == "bonjour tlm":
			if await infac(message.author):
				with open ('points.json','r') as f:
					pt = json.load(f)
				if str(message.author.id) in pt.keys():
					pt[str(message.author.id)] += 20
				else:
					pt[str(message.author.id)] = 20
				with open ('equipes.json','r') as f:
					eq = json.load(f)
				for role in eq.keys():
					if int(role) in [t.id for t in message.author.roles]:
						eq[role]['total'] += 20
						if str(message.author.id) in eq[role]['membres'].keys():
							eq[role]['membres'][str(message.author.id)] += 20
						else:
							eq[role]['membres'][str(message.author.id)] = 20
				with open ('equipes.json','w') as f:
					json.dump(eq,f,indent=6)
				with open ('points.json','w') as f:
					json.dump(pt,f,indent=6)
				await message.author.send('Vous avez gagné 20 points de bonjour tlm')
				logs = bot.get_channel(1026567820311531550)
				await logs.send(f'{message.author.mention} à gagné `20` points pour bonjour tlm ')
	await bot.process_commands(message)

def run_bot(token=TOKEN, debug=False):
	if debug: print(bot._connection.loop)
	bot.run(token)
	if debug: print(bot._connection.loop)
	return bot._connection.loop.is_closed()

if not SERVER:
	bot.run(TOKEN)
