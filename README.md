# COVIDschools
Data and code required to reproduce findings pertaining to COVID-19 related school interventions

--- School closure ---

The following file names include the data for school closure (including date accessed as numbers may since have changed):
- Denmark (accessed 20/06/2020): DK_data.csv
- Norway (accessed 02/06/2020): NO_data.csv
- Sweden (accessed 05/06/2020): SE_data.csv
- Germany: DE_reg_data_new.csv

Data from studied German states were obtained daily (with a day's delay). These files also include the projected trajectories resulting from the Gaussian Process forecast:
- Baden-Württemberg: Baden_results.csv
- Bavaria: Bavaria_results.csv
- Berlin: Berlin_results.csv
- Hesse: Hesse_results.csv
- Lower Saxony: LSaxony_results.csv
- North Rhine-Westphalia: NRW_results.csv
- Rhineland-Palatinate: Rhineland_results.csv

The script ConstGrowthRates.r will produce the pre- and post-response growth rates for each state.

--- School reopening ---

The following file names include the data for school reopening (including date accessed as numbers may since have changed):
- Denmark (hospital admissions, accessed 13/06/2020): denmark_data.csv
- Denmark (confirmed cases, accessed 13/06/2020): denmark_cases.csv
- Norway (accessed 13/06/2020): norway_data.csv
- Germany (hospital admissions, accessed 09/07/2020): germany_data_hosp.csv
- Germany (confirmed cases among staff and students, accessed 09/07/2020): germany_data_raw.csv

The script InstGrowthRates.r will produce the instantaneous growth rates for each data stream of interest, and this should be run first. For each data set of interest, the following Python scripts will overlay the instantaneous growth rates with the dates of key interventions:
- Danish daily hospital admissions: denmark.py
- Danish daily confirmed cases: denmark-cases.py
- Norwegian daily confirmed cases: norway.py
- German daily hospital admissions: germany_hosp.py
- German daily confirmed cases among staff and students: germany.py
