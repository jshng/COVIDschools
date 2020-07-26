from matplotlib import pyplot as plt
import pandas

denmark = pandas.read_csv('denmark_data.csv', parse_dates=True, dayfirst=True)
DKr = pandas.read_csv('DK.csv')
DKr_ub = pandas.read_csv('DK-ub.csv')
DKr_lb = pandas.read_csv('DK-lb.csv')
dates = denmark['Dates']
DK_sch_dates = [dates[14], dates[47], dates[56]]
DK_other_dates = [dates[19], dates[40]]


fig = plt.figure(figsize=(15,8))
ax = fig.gca()

# sp1
plt.subplot(121)
plt.plot(denmark['Dates'], denmark['Hospital'], "x:", lw=2, label='Observed cases')
for intv in DK_sch_dates:
    plt.axvline(x=intv, linewidth=2, color='k', alpha=0.2)
for intv in DK_other_dates:
    plt.axvline(x=intv, linewidth=2, color='k', alpha=0.2, linestyle=':')
plt.xticks(ticks=dates[::7], labels=dates[::7], rotation=45, ha='right')
plt.xlabel('Date')
plt.ylabel('Daily Hospital Admissions')
plt.legend

# sp2
plt.subplot(122)
plt.plot(denmark['Dates'], DKr['V1'], "-", lw=2, label='Observed cases')
plt.plot(denmark['Dates'], DKr_lb['V1'], "b:", color='dodgerblue', lw=1)
plt.plot(denmark['Dates'], DKr_ub['V1'], "b:",color='dodgerblue', lw=1)
plt.fill_between(denmark['Dates'], DKr['V1'], DKr_lb['V1'], facecolor='dodgerblue', alpha=0.25,)
plt.fill_between(denmark['Dates'], DKr['V1'], DKr_ub['V1'], facecolor='dodgerblue', alpha=0.25,)
for intv in DK_sch_dates:
    plt.axvline(x=intv, linewidth=2, color='k', alpha=0.2)
for intv in DK_other_dates:
    plt.axvline(x=intv, linewidth=2, color='k', alpha=0.2, linestyle=':')
plt.ylim(-0.15,0.05)
plt.xticks(ticks=dates[::7], labels=dates[::7], rotation=45, ha='right')
plt.xlabel('Date')
plt.ylabel('Instantaneous growth rate')
plt.legend

#plt.show()
plt.tight_layout()
plt.savefig("Denmark.pdf")
