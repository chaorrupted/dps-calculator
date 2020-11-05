dmg = 100.0
cd = 1.0
duration = 10000.0

crit_chance = float(input("critical hit chance: (eg: 43.27)"))
if(crit_chance > 100.0):
    crit_chance = 100.0

crit_damage_multiplier = float(input("crit damage: (eg: 43.27)"))

crit_dmg = dmg + (dmg * crit_damage_multiplier / 100)

hit_count = duration // cd
crit_count = hit_count * (crit_chance / 100)
non_crit_count = hit_count - crit_count

total_dmg = (non_crit_count * dmg) + (crit_count * crit_dmg)
dps = total_dmg / duration
no_crit_dps = (hit_count * dmg) / duration
dmg_increase = ((dps/no_crit_dps)*100.0) - 100.0

print("\n","--calculation results--")
print("crit chance: {0:.2f}%".format(crit_chance))
print("crit multiplier: +{0:.2f}%".format(crit_damage_multiplier))
print("dps with 0% crit:", no_crit_dps)
print("dps: {0:.3f}".format(dps))
print("dps increase with crit: +{0:.3f}%".format(dmg_increase))
