from matplotlib import pyplot as plt
import pandas

germany = pandas.read_csv('germany_data_raw.csv', parse_dates=True, dayfirst=True)
DEstaffr = pandas.read_csv('DEstaff.csv')
DEstaffr_ub = pandas.read_csv('DEstaff-ub.csv')
DEstaffr_lb = pandas.read_csv('DEstaff-lb.csv')
DEstudentsr = pandas.read_csv('DEstudents.csv')
DEstudentsr_ub = pandas.read_csv('DEstudents-ub.csv')
DEstudentsr_lb = pandas.read_csv('DEstudents-lb.csv')
dates = germany['Dates']
DE_sch_dates = [dates[5], dates[12], dates[19], dates[26]]
DE_sch_dates_short = [dates[12], dates[19], dates[26]]
DE_other_dates = [dates[8]]


fig = plt.figure(figsize=(15,8))
ax = fig.gca()

# sp1
plt.subplot(121)
plt.plot(germany['Dates'], germany['Staff'], "xr--", lw=2, label='Observed cases')
plt.plot(germany['Dates'], germany['Students'], "x--", lw=2, label='Observed cases')
for intv in DE_sch_dates:
    plt.axvline(x=intv, linewidth=2, color='k', alpha=0.2)
for intv in DE_other_dates:
    plt.axvline(x=intv, linewidth=2, color='k', alpha=0.2, linestyle=':')
plt.xticks(ticks=dates[::7], labels=dates[::7], rotation=45, ha='right')
plt.xlabel('Date')
plt.ylabel('Daily Confirmed Cases')
plt.legend

# sp2
plt.subplot(122)
plt.plot(germany['Dates'], DEstaffr['V1'], "r-", lw=2, label='Observed cases')
plt.plot(germany['Dates'], DEstaffr_lb['V1'], "r:", lw=1)
plt.plot(germany['Dates'], DEstaffr_ub['V1'], "r:", lw=1)
plt.fill_between(germany['Dates'], DEstaffr['V1'], DEstaffr_lb['V1'], facecolor='red', alpha=0.25)
plt.fill_between(germany['Dates'], DEstaffr['V1'], DEstaffr_ub['V1'], facecolor='red', alpha=0.25)
plt.plot(germany['Dates'], DEstudentsr['V1'], "-", lw=2, label='Observed cases')
plt.plot(germany['Dates'], DEstudentsr_lb['V1'], "b:", color='dodgerblue', lw=1)
plt.plot(germany['Dates'], DEstudentsr_ub['V1'], "b:",color='dodgerblue', lw=1)
plt.fill_between(germany['Dates'], DEstudentsr['V1'], DEstudentsr_lb['V1'], facecolor='dodgerblue', alpha=0.25)
plt.fill_between(germany['Dates'], DEstudentsr['V1'], DEstudentsr_ub['V1'], facecolor='dodgerblue', alpha=0.25)
for intv in DE_sch_dates:
    plt.axvline(x=intv, linewidth=2, color='k', alpha=0.2)
for intv in DE_other_dates:
    plt.axvline(x=intv, linewidth=2, color='k', alpha=0.2, linestyle=':')
plt.ylim(-0.1,0.1)
plt.xticks(ticks=dates[::7], labels=dates[::7], rotation=45, ha='right')
plt.xlabel('Date')
plt.ylabel('Instantaneous growth rate')
plt.legend

#plt.show()
plt.tight_layout()
plt.savefig("Germany-schools.pdf")
