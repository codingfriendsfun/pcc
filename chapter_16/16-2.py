import matplotlib.pyplot as plt

import dv_highs_lows
import sitka_highs_lows

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()

# Graph death valley highs and lows
ax.plot(dv_highs_lows.dv_dates, dv_highs_lows.dv_highs, color='red', alpha=0.5)
ax.plot(dv_highs_lows.dv_dates, dv_highs_lows.dv_lows, color='blue', alpha=0.5)
ax.fill_between(dv_highs_lows.dv_dates, dv_highs_lows.dv_highs, 
                dv_highs_lows.dv_lows, facecolor='blue', alpha=0.1)

# Graph sitka highs and lows
ax.plot(sitka_highs_lows.s_dates, sitka_highs_lows.s_highs, color='red', alpha=0.5)
ax.plot(sitka_highs_lows.s_dates, sitka_highs_lows.s_lows, color='blue', alpha=0.5)
ax.fill_between(sitka_highs_lows.s_dates, sitka_highs_lows.s_highs, 
                sitka_highs_lows.s_lows, facecolor='blue', alpha=0.1)

# Format plot.
title = 'Daily High and Low Temperatures, 2021\nDeath Valley, CA vs Sitka, Alaska'
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
plt.ylim(0,140)

fig.autofmt_xdate()

ax.set_ylabel(f'Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
