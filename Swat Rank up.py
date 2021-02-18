# dictionary to find number an
ranks = {
      "Private": 1,
      "Corpporal": 2,
      "Sergeant" : 3,
      "Staff Sergeant" : 4,
      "Sergeant First Class": 5,
      "Lieutenant": 6,
      "Captain": 7,
      "Major": 8,
      "Team Leader": 9,
      "Co-Commander": 10,
      "Commander": 11,
      }
async def giverole(ctx, member: discord.Member, *, who):
    aif check_role not in member.roles:
    await client.say(f"You don't have the role '{str(role)}'")
  else:
    await client.say("@who you have been promoted to '" + str(role) + "' by " + member.mention + " .")
