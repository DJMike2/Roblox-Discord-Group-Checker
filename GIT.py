import discord
import asyncio
import time
from discord.ext import commands
import requests
from gtts import gTTS



token = "...."
client = discord.Client(intents=discord.Intents.default())
    
def getPlayerGroups(playerId):
    r = requests.get("https://groups.roblox.com/v2/users/" + str(playerId) + "/groups/roles").json()
    groups = []
    for elem in r:
        print(elem["id"])
    #for x in range(0,len(r)):
    #    groups.append(r[x]["Id"])
    #return groups
    #time.sleep(100)

#getPlayerGroups("/groups/roles")

def Verification_Checklist():   
    intents = discord.Intents().all()
    bot = commands.Bot(command_prefix='-', case_insensitive=True,intents=intents)

    @bot.event
    async def on_ready():
        print('logged in')
        channel = bot.get_channel(....)#

    @bot.command()
    async def Deep_Scan(ctx):
        await ctx.send("This will take a minute...")
        time.sleep(5)
        await ctx.send("Due to a specific target scan, we will emailed it to root {CONFIDENTIAL}")

    @bot.command()
    async def List_All_Users(ctx):
        Member_List = ctx.guild.members
        Discord_Printer = []

        ##Gets all the groups someone is in
        kingdomGroups = []
        membersNotInGroup = []
        membersOfNobility = []
        basicMembers = []
        unableToCheckMembers = []
 
        def listToString(arrayPassed):
            return (', '.join([str(elem) for elem in arrayPassed]))

        def getGroupAllies(groupid):
            #https://groups.roblox.com/v1/groups/8488180/relationships/allies?model.maxRows=1000&model.startRowIndex=0
            r1 = requests.get("https://groups.roblox.com/v1/groups/" + str(groupid) + "/relationships/allies?model.maxRows=1000&model.startRowIndex=0").json()
            for x in range(0,len(r1["relatedGroups"])):
                kingdomGroups.append(r1["relatedGroups"][x]["id"])
            #for x in range(0,len(r1["relatedGroups"])):
             #   pass
        
        def getPlayerGroups(playerId):
            r = requests.get("https://groups.roblox.com/v2/users/" + str(playerId) + "/groups/roles").json()
            groups = []
            try:
                for i in range(0,len(r["data"])):
                    lst = r["data"][i]["group"]["id"]
                    groups.append(lst)
                return groups
            except:
                pass

        def comparePlayerGroupsToOthers(playerGroups,allyGroups):
            matchingGroups = []
            for item in playerGroups:
                if item in kingdomGroups:
                    matchingGroups.append(item)
            return matchingGroups

        for Member in Member_List:
            hasNickname = isinstance(Member.nick,str)
            houseMemberRole = discord.utils.get(ctx.guild.roles, name="{Casterly Member}")
            #houseOfficerRole = discord.utils.get(ctx.guild.roles, name="{Casterly Nobility}") #HIcom
            houseNobilityRole = discord.utils.get(ctx.guild.roles, name="{Casterly Nobility}") #HIcom
            
            if hasNickname:
                if houseNobilityRole in Member.roles:
                    membersOfNobility.append(Member.nick)
                elif houseMemberRole in Member.roles and houseNobilityRole not in Member.roles:
                    if "-" in Member.nick:
                        try:
                            Member.nick.partition("-")[2]##
                        except ValueError:
                            basicMembers.append(Member.nick + " has a bad nickname.")
                        else:
                            matchingGroups = comparePlayerGroupsToOthers(getPlayerGroups(Member.nick.partition("-")[2]),getGroupAllies(8488180))##
                            isInCasterly = False
                            otherHouses = []
                            for item in matchingGroups:
                                if item == 7410838:
                                    isInCasterly = True
                                if item != 8481232 and item != 7410838:
                                    otherHouses.append(item)
                            if isInCasterly == False and len(otherHouses) == 0:
                                basicMembers.append(Member.nick + " is not in the Casterly group!")
                            elif isInCasterly == True and len(otherHouses) == 0:
                                basicMembers.append(Member.nick)
                            elif isInCasterly == False and len(otherHouses) > 0:
                                basicMembers.append(Member.nick + " is not in the Casterly group and is a member of: " + listToString(otherHouses))
                            elif isInCasterly == True and len(otherHouses) > 0:
                                basicMembers.append(Member.nick + " is a member of: " + listToString(otherHouses))
                    else:
                        basicMembers.append(Member.nick + " has a bad nickname.")

            else:
                membersNotInGroup.append(Member.name)

        #Print to discord all data
        await ctx.send("```" + '\n' + "**House Casterly Nobility**" + '\n' + '\n'.join(membersOfNobility) + "```")

        chunked_list = list()
        for i in range(0, len(basicMembers), 30):
            chunked_list.append(basicMembers[i:i+30])
        #for i in range(1):
        await ctx.send("```" + '\n' + "**House Casterly Members**" + '\n' + '\n'.join(chunked_list[i]) + "```")
        time.sleep(.5)

        #await ctx.send("```" + '\n' + "**House Casterly Members**" + '\n' + '\n'.join(basicMembers) + "```")
        await ctx.send("```" + '\n' + "**Not in Casterly Group**" + '\n' + '\n'.join(membersNotInGroup) + "```")
        print(kingdomGroups)
        #Check who has specific role
        @bot.command()
        async def Check_Verifications(ctx):
            role = discord.utils.get(ctx.guild.roles, name="✧ Casterly Hicom")
            if role in ctx.author.roles:
                await ctx.send(f'User already has {role.name}')
            else:
                await ctx.send(":white_check_mark: User has role")

    bot.run(token)

Verification_Checklist()

