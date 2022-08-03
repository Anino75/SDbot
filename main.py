import asyncio
import io
import json
import random
import sys
import time
import traceback
from datetime import datetime, timedelta
import chat_exporter
import discord
import toml
from discord.ext import commands
import mysql.connector

# --- Other files ---
import divers
import economie
import fun
import quotas
import Recrutements
import relations
import staff
import tickets


debug = True
SERVER = True
config = toml.load(open('config.toml'))
PREFIX = config['Prefix']
intents = discord.Intents().all()


class PersistentViewBot(commands.Bot):
	def __init__(self):
		super().__init__(command_prefix=commands.when_mentioned_or(PREFIX), help_command=None, case_insensitive=True, intents=intents)
	async def setup_hook(self) -> None:
		self.add_view(tickets.PersistentView())
		self.add_view(tickets.fermerticket())
		self.add_view(economie.PvPView())
		self.add_view(economie.NombreView())
		self.add_view(economie.Methode())
		self.add_view(economie.rouletteruss())
		self.add_view(economie.gains())
		self.add_view(economie.roulette())
		self.add_view(economie.rouleView())
		self.add_view(divers.regl())
		self.add_view(relations.IsAlly())
		self.add_view(Recrutements.testview())
		self.add_view(Recrutements.candid())

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

@bot.command()
async def ilemosh(ctx,member: discord.Member=None):
	if ctx.author.id != 790574682294190091:
		await ctx.reply("t'es pas la grande maitresse supreme toi")
		return
	with open('phases.json', 'r') as f:
		phases = json.load(f)
	phases["A faire"].pop(str(member.id))
	with open('phases.json', 'w') as f:
		json.dump(phases, f, indent=6)
	await ctx.reply('nickel')

@bot.command()
async def renduphases(ctx,member: discord.Member=None,rendu='non spécifié'):
	if ctx.author.id != 790574682294190091:
		await ctx.reply("t'es pas la grande maitresse supreme toi")
		return
	with open('phases.json', 'r') as f:
		phases = json.load(f)
	phases["A faire"].pop(str(member.id))
	phases["fait"]=[datetime.now(),rendu]
	with open('phases.json', 'w') as f:
		json.dump(phases, f, indent=6)
	await ctx.reply('nickel')

def get_left_space(str1_, str2_):
	rv = len(str1_) - len(str2_)
	return "".join([' ' for x in range(rv)])

async def effectif():
	guild = bot.get_guild(790367917812088864)
	channel = await bot.fetch_channel(937006102653071452)
	role_ids = {'Staff': [790675782569164820, 821787385636585513, 798301141094891620, 790675781789155329, 791426367362433066],
				'Membres VIP': [790675782338740235, 790675782364037131, 790675783352975360],
				'Membres +': [790675783549976579, 790675783693500456, 790675784120401932],
				'Membres': [790675784225521734, 791066206437113897, 791066207418712094]}
	abs_role = guild.get_role(813928386946138153)
	while True:
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
				v_field = ", ".join([x.mention for x in role.members if abs_role.id not in [r.id for r in x.roles]])
				_embed.description += f"{role.mention} : {v_field}\n\n"
		await message.edit(embed=_embed)
		await asyncio.sleep(3600)

@bot.event
async def on_ready():
	print(f'[{datetime.now().strftime("%Y:%m:%d %H:%M:%S")}]', 'Bot is online!')
	# functions
	bot.loop.create_task(effectif())
	bot.loop.create_task(inactivity())
	#bot.loop.create_task(candids())
	# print
	field_placeholder = '+----------------------------------+'
	fields = [f"| Username: {bot.user}", f"| ID: {bot.user.id}", f"| Version: {str(discord.__version__)}"]
	print(field_placeholder)
	for field in fields:
		print(f"{field}{get_left_space(field_placeholder, field)[:-1]}|")
	print(field_placeholder)
	BOT_INVITE_LINK = f'https://discord.com/api/oauth2/authorize?client_id={str(bot.user.id)}&permissions=8&scope=applications.commands%20bot'
	act = discord.Game(name="*help pour voir les commandes auxquelles vous avez accès")
	await bot.change_presence(activity=act)
	guild = bot.get_guild(790367917812088864)
	with open('invite.json', 'r') as f:
		inv = json.load(f)
	inv["invites"] = {}
	for invite in await guild.invites():
		inv["invites"][invite.code] = invite.uses
	with open('invite.json', 'w') as f:
		json.dump(inv, f, indent=6)

async def del_message(message):
	try:
		await message.delete()
	except:
		pass

def create_small_embed(description=None, color=discord.Color.blue()):
	embed = discord.Embed(
		description=description,
		color=color
	)
	return embed


# =========== Divers ===========
@bot.command()
async def pluschef(ctx,member:discord.Member = None):
	await pluschef2(ctx,member)

@bot.command()
async def moinschef(ctx,member:discord.Member = None):
	await moinschef2(ctx,member)

@bot.command()
async def spam(ctx,member: discord.Member=None,nombre=100):
	await spam2(ctx,member,nombre)

@bot.command()
async def embed(ctx,channelid,*,message):
	await embed2(ctx,channelid,message)

@bot.command()
@commands.has_permissions(administrator=True)
async def prepare(ctx,prep=None):
	await prepare2(ctx,prep)

# =========== Economie ===========

@bot.command(aliases=["createaccount","openaccount","ouvrircompte"])
async def creercompte(ctx):
	await creercompte2(ctx)

@creercompte.error
async def creercompte(ctx, error):
	await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command(aliases=['balance',"bal"])
async def money(ctx,member:discord.User=None):
	await money2(ctx,member)

@money.error
async def money(ctx, error):
	await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command(aliases=['adminpay',"admingive",'add','give'])
@commands.has_any_role(791426367362433066, 798301141094891620, 790675782569164820)
async def adminaddmoney(ctx,member:discord.Member=None,money=0):
	await adminaddmoney2(ctx,member,money)

@adminaddmoney.error
async def adminaddmoney(ctx, error):
	if isinstance(error, commands.MissingAnyRole):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les responsables market peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command(aliases=['remove'])
@commands.has_any_role(791426367362433066, 798301141094891620, 790675782569164820)
async def adminremovemoney(ctx,member:discord.Member=None,money=0):
	await adminremovemoney2(ctx,member,money)

@adminremovemoney.error
async def adminremovemoney(ctx, error):
	if isinstance(error, commands.MissingAnyRole):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les responsables market peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
async def pay(ctx,member:discord.Member=None,money=0):
	await pay2(ctx,member,money)

@pay.error
async def pay(ctx, error):
	await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
@commands.has_any_role(960180290683293766 or 798301141094891620 or 790675782569164820)
async def claim(ctx):
	await claim2(ctx)

@claim.error
async def claim(ctx, error):
	if isinstance(error, commands.MissingAnyRole):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les responsables market peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
@commands.has_any_role(960180290683293766 or 798301141094891620 or 790675782569164820)
async def livre(ctx):
	await livre2(ctx)

@livre.error
async def livre(ctx, error):
	if isinstance(error, commands.MissingAnyRole):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les responsables market peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))


@bot.command(aliases=['RR'])
async def rouletterusse(ctx,mise=None):
	await rouletterusse2(ctx,mise)

@bot.command()
@commands.has_permissions(administrator=True)
async def reset(ctx,res=None):
	await reset2(ctx,res)

@reset.error
async def reset(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les HG peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

# =========== Fun ===========

@bot.command()
async def aleacrush(ctx,member:discord.Member = None):
	await aleacrush2(ctx,member)

@aleacrush.error
async def aleacrush(ctx, error):
	await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def pendu(ctx):
	await pendu2(ctx)

@pendu.error
async def pendu(ctx, error):
	await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
async def motus(ctx):
	await motus2(ctx)

@motus.error
async def motus(ctx, error):
	await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

# =========== Quotas ===========

@bot.command()
@commands.has_any_role(791426367362433066, 798301141094891620, 790675782569164820)
async def debutquotas(ctx):
	await debutquotas2(ctx)

@debutquotas.error
async def debutquotas(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les HG peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
@commands.has_any_role(791426367362433066, 798301141094891620, 790675782569164820)
async def renduquotas(ctx,divi,member:discord.Member=None):
	await renduquotas2(ctx,divi,member)

@renduquotas.error
async def renduquotas(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les HG peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
@commands.has_any_role(791426367362433066, 798301141094891620, 790675782569164820)
async def listequotas(ctx,semaine=None):
	await listequotas2(ctx,semaine)

@listequotas.error
async def listequotas(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les HG peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

# =========== Recrutements ===========

@bot.command()
@commands.has_any_role(791426367362433066, 821787385636585513, 790675782569164820)
async def refuse(ctx, member: discord.Member=None, *, raison="Le recruteur n'a pas spécifié de raison"):
	await refuse2(ctx,member,raison)

@refuse.error
async def refuse(ctx, error):
	if isinstance(error, commands.MissingAnyRole):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les recruteurs peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
@commands.has_any_role(791426367362433066, 821787385636585513, 790675782569164820)
async def accept(ctx, member: discord.Member=None):
	await accept2(ctx,member)

@accept.error
async def accept(ctx, error):
	if isinstance(error, commands.MissingAnyRole):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les recruteurs peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
@commands.has_any_role(790675781789155329, 821787385636585513, 790675782569164820)
async def addtime(ctx, member: discord.Member=None, time_string=None):
	await addtime2(ctx, member, time_string)

@addtime.error
async def addtime(ctx, error):
	if isinstance(error, commands.MissingAnyRole):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les responsables recrutement peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
@commands.has_any_role(791426367362433066, 821787385636585513, 790675782569164820)
async def oralyes(ctx, member: discord.Member=None):
	await oralyes2(ctx, member)

@bot.command()
@commands.has_any_role(791426367362433066, 821787385636585513, 790675782569164820)
async def oralno(ctx, member: discord.Member=None):
	await oralno2(ctx, member)

@oralno.error
async def oralno(ctx, error):
	if isinstance(error, commands.MissingAnyRole):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les recruteurs peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
@commands.has_any_role(791426367362433066, 821787385636585513, 790675782569164820)
async def finphases(ctx, member: discord.Member=None,rendu="Non spécifié"):
	await finphases2(ctx, member,rendu)

@bot.command()
@commands.has_any_role(791426367362433066, 821787385636585513, 790675782569164820)
async def kickphases(ctx, member: discord.User=None, *, raison="Le recruteur n'a pas spécifié de raison"):
	await kickphases2(ctx, member, raison)

# =========== Relations ===========

@bot.command()
@commands.has_permissions(administrator=True)
async def addpna(ctx,faction=None,member:discord.Member=None):
	await addpna2(ctx,faction,member)

@addpna.error
async def addpna(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les HG peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
@commands.has_permissions(administrator=True)
async def addtruce(ctx,faction=None,member:discord.Member=None):
	await addtruce2(ctx,faction,member)

@addtruce.error
async def addtruce(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les HG peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
@commands.has_permissions(administrator=True)
async def addally(ctx,faction=None,member:discord.Member=None):
	await addally2(ctx,faction,member)

@addally.error
async def addally(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les HG peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
@commands.has_permissions(administrator=True)
async def endally(ctx,faction=None):
	await endally2(ctx,faction)

@endally.error
async def endally(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les HG peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
async def addmember(ctx,member:discord.Member=None,faction=None):
	await addmember2(ctx,member,faction)

@addmember.error
async def addmember(ctx, error):
	await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
async def removemember(ctx,member:discord.Member=None,faction=None):
	await removemember2(ctx,member,faction)

@removemember.error
async def removemember(ctx, error):
	await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def askally(ctx,faction=None):
	await askally2(ctx,faction)

@askally.error
async def askally(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.reply(f"Afin d'éviter de spammer nos truces, cette commande n'est accèssible qu'une fois par jour.")
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
async def editally(ctx):
	await edditally()

# =========== Staff ===========

@bot.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, member : discord.Member=None, *, raison="Pas de raison fournie"):
	await warn2(ctx, member , raison)

@warn.error
async def warn(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les HG peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
@commands.has_permissions(administrator=True)
async def unwarn(ctx, member : discord.Member=None, nbw=None, *, raison="Pas de raison fournie"):
	await unwarn(ctx, member, nbw,raison)

@unwarn.error
async def unwarn(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les HG peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
@commands.has_permissions(administrator=True)
async def blame(ctx, member : discord.Member=None, *, raison="Pas de raison fournie"):
	await blame2(ctx,member,raison)

@blame.error
async def blame(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les HG peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
@commands.has_permissions(administrator=True)
async def unblame(ctx, member : discord.Member=None, nbw=None, *, raison="Pas de raison fournie"):
	await unblame2(ctx,member,raison)

@unblame.error
async def unblame(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les HG peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
@commands.has_permissions(administrator=True)
async def rankup(ctx, member:discord.Member=None):
	await rankup2(ctx,member)

@rankup.error
async def rankup(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les HG peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
@commands.has_permissions(administrator=True)
async def derank(ctx, member:discord.Member=None,*,raison="Pas de raison spécifiée"):
	await derank2(ctx,member)

@derank.error
async def derank(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les HG peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.Member=None,*,raison="Pas de raison spécifiée"):
	await ban2(ctx,member,raison)

@ban.error
async def ban(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les HG peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, member:discord.User=None,*,raison="Pas de raison spécifiée"):
	await unban2(ctx,member,raison)

@unban.error
async def unban(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les HG peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

@bot.command()
@commands.has_permissions(administrator=True)
async def sanctions(ctx, member: discord.Member = None):
	await sanctions2(ctx,member)

@sanctions.error
async def sanctions(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.reply(embed=create_small_embed(':warning: Seuls les HG peuvent utiliser cette commande !',discord.Color.red()))
	else:
		await ctx.reply(embed=create_small_embed(":warning: Une erreur inconnue s'est produite, veuillez mp Anino75",discord.Color.red()))

# =========== Tickets ===========

@bot.command()
async def close(ctx):
	await close2(ctx)

# =========== Autre ===========

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
		if message.content.startswith(PREFIX):
			await message.author.send("Vous ne pouvez pas m'utiliser en message privé !")
		return
	await bot.process_commands(message)

def run_bot(token=TOKEN, debug=False):
	if debug: print(bot._connection.loop)
	bot.run(token)
	if debug: print(bot._connection.loop)
	return bot._connection.loop.is_closed()

if not SERVER:
	bot.run(TOKEN)
