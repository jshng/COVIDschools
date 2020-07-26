from matplotlib import pyplot as plt
import pandas

germany = pandas.read_csv('germany_data_hosp.csv', parse_dates=True, dayfirst=True)
DEr = pandas.read_csv('DE.csv')
DEr_ub = pandas.read_csv('DE-ub.csv')
DEr_lb = pandas.read_csv('DE-lb.csv')
dates = germany['Dates']
DE_sch_dates = [dates[5], dates[12], dates[19], dates[26]]
DE_other_dates = [dates[8]]


fig = plt.figure(figsize=(15,8))
ax = fig.gca()

# sp1
plt.subplot(121)
plt.plot(germany['Dates'], germany['Hospital'], "x--", lw=2, label='Observed cases')
for intv in DE_sch_dates:
    plt.axvline(x=intv, linewidth=2, color='k', alpha=0.2)
for intv in DE_other_dates:
    plt.axvline(x=intv, linewidth=2, color='k', alpha=0.2, linestyle=':')
plt.xticks(ticks=dates[::7], labels=dates[::7], rotation=45, ha='right')
plt.xlabel('Date')
plt.ylabel('Daily Hospital Admissions')
plt.legend

# sp2
plt.subplot(122)
plt.plot(germany['Dates'], DEr['V1'], "-", lw=2, label='Observed cases')
plt.plot(germany['Dates'], DEr_lb['V1'], "b:", color='dodgerblue', lw=1)
plt.plot(germany['Dates'], DEr_ub['V1'], "b:", color='dodgerblue', lw=1)
plt.fill_between(germany['Dates'], DEr['V1'], DEr_lb['V1'], facecolor='dodgerblue', alpha=0.25)
plt.fill_between(germany['Dates'], DEr['V1'], DEr_ub['V1'], facecolor='dodgerblue', alpha=0.25)
for intv in DE_sch_dates:
    plt.axvline(x=intv, linewidth=2, color='k', alpha=0.2)
for intv in DE_other_dates:
    plt.axvline(x=intv, linewidth=2, color='k', alpha=0.2, linestyle=':')
plt.ylim(-0.4,0.7)
plt.xticks(ticks=dates[::7], labels=dates[::7], rotation=45, ha='right')
plt.xlabel('Date')
plt.ylabel('Instantaneous growth rate')
plt.legend

#plt.show()
plt.tight_layout()
plt.savefig("Germany.pdf")
