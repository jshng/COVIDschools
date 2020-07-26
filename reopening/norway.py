from matplotlib import pyplot as plt
import pandas
import datetime

norway = pandas.read_csv('norway_data.csv', parse_dates=True, dayfirst=True)
NOr = pandas.read_csv('NO.csv')
NOr_ub = pandas.read_csv('NO-ub.csv')
NOr_lb = pandas.read_csv('NO-lb.csv')
dates = norway['Dates']
NO_sch_dates = [dates[19], dates[26], dates[40]]
NO_other_dates = [dates[36]]


fig = plt.figure(figsize=(15,8))
ax = fig.gca()

# sp1
plt.subplot(121)
plt.plot(norway['Dates'], norway['Confirmed'], "x:", lw=2, label='Observed cases')
for intv in NO_sch_dates:
    plt.axvline(x=intv, linewidth=2, color='k', alpha=0.2)
for intv in NO_other_dates:
    plt.axvline(x=intv, linewidth=2, color='k', alpha=0.2, linestyle=':')
plt.xticks(ticks=dates[::7], labels=dates[::7], rotation=45, ha='right')
plt.xlabel('Date')
plt.ylabel('Daily Confirmed Cases')
plt.legend

# sp2
plt.subplot(122)
plt.plot(norway['Dates'], NOr['V1'], "-", lw=2, label='Observed cases')
plt.plot(norway['Dates'], NOr_lb['V1'], "b:", color='dodgerblue', lw=1)
plt.plot(norway['Dates'], NOr_ub['V1'], "b:",color='dodgerblue', lw=1)
plt.fill_between(norway['Dates'], NOr['V1'], NOr_lb['V1'], facecolor='dodgerblue', alpha=0.25,)
plt.fill_between(norway['Dates'], NOr['V1'], NOr_ub['V1'], facecolor='dodgerblue', alpha=0.25,)
for intv in NO_sch_dates:
    plt.axvline(x=intv, linewidth=2, color='k', alpha=0.2)
for intv in NO_other_dates:
    plt.axvline(x=intv, linewidth=2, color='k', alpha=0.2, linestyle=':')
plt.ylim(-0.06,-0.035)
plt.xticks(ticks=dates[::7], labels=dates[::7], rotation=45, ha='right')
plt.xlabel('Date')
plt.ylabel('Instantaneous growth rate')
plt.legend

#plt.show()
plt.tight_layout()
plt.savefig("Norway.pdf")
