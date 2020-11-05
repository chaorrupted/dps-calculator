what is this? it is a damage per second (dps) calculator in python3.

note: the "simulation" considers randomly generated effects perfectly fair. for example, 23.45 percent critical hit chance will crit exactly 2345 times in 10000 attacks.

note2: crit damage in this context refers to bonus damage percentage you do on a critical hit. for example, 100 regular attack damage with 20% crit damage means your critical hits will deal 120 damage. 100% crit damage will double your damage on a critical hit, and 200% crit damage will triple it. 

note3: only two significant figures are supported for crit chance & crit damage, but you can edit the code to change that.

note4: you can modify duration to be a fixed number instead of 10000*cooldown and uncomment lines related to idle time so you can see how much time is wasted due to your time limit and ability cooldown.
what is time wasted? i mean the 20 seconds you spend doing nothing when you have a 40 second cooldown attack and only 100 seconds to deal damage.

note5: might act weird because god knows how computers work??? feature requests, criticism and PRs are welcome.
