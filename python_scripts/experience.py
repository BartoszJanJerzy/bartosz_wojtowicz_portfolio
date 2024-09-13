import plotly.graph_objects as go
from datetime import date


dates_academic = [date(year=2019, month=10, day=1), date(year=2022, month=2, day=1)]
dates_flow = [date(year=2020, month=11, day=1), date(year=2021, month=7, day=1)]
dates_abs = [date(year=2021, month=8, day=1), date(year=2023, month=2, day=1)]
dates_wesub = [date(year=2023, month=3, day=1), date(year=2023, month=12, day=1)]
dates_playstrict_side = [date(year=2023, month=6, day=1), date(year=2023, month=10, day=1)]
dates_df_side = [date(year=2023, month=10, day=1), date(year=2023, month=11, day=1)]
dates_essyo_side = [date(year=2023, month=11, day=1), date(year=2023, month=12, day=1)]
dates_df_b2b = [date(year=2024, month=3, day=1), date(year=2024, month=8, day=1)]


total_days = 0
for dataset in [
    dates_academic,
    dates_flow,
    dates_abs,
    dates_wesub,
    dates_df_side,
    dates_playstrict_side,
    dates_essyo_side,
    dates_df_b2b
]:
    total_days += (dataset[1] - dataset[0]).days
total_months = int(total_days / 30)
total_years = f'{int(total_months/12)}y {total_months % 12}m'

it_days = 0
for dataset in [
    dates_abs,
    dates_wesub,
    dates_df_side,
    dates_playstrict_side,
    dates_essyo_side,
    dates_df_b2b
]:
    it_days += (dataset[1] - dataset[0]).days
it_months = int(it_days / 30)
it_years = f'{int(it_months/12)}y {it_months % 12}m'

title = f'Total experience with analytical work: {total_years}<br>Included IT experience: {it_years}'

def add_trace(label: str, name: str, values, showlegend: bool = True):
    fig.add_trace(go.Scatter(
        name=name,
        x=[label, label],
        y=values,
        mode='lines',
        line=dict(width=20),
        showlegend=showlegend
    ))


fig = go.Figure()

add_trace('', '', [dates_abs[0], dates_abs[0]], False)
add_trace('Academic Work', f'PhD', dates_academic)
add_trace('Flow Research Center', f'Junior Researcher', dates_flow)
add_trace('Asseco Business Solutions', f'Junior Data Scientist', dates_abs)
add_trace('WeSub', f'Data Scientist', dates_wesub)
add_trace('Playstrict (side)', f'Data Scientist (side project)', dates_playstrict_side)
add_trace('DigitalFirst (side)', f'Data Scientist (side project)', dates_df_side)
add_trace('Essyo (side)', f'Data Scientist (side project)', dates_essyo_side)
add_trace('DigitalFirst (current)', f'Senior Data Scientist', dates_df_b2b)
add_trace(' ', '', [dates_abs[0], dates_abs[0]], False)


fig.update_layout(
    title=title,
    width=1000,
    height=800,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(gridcolor='silver', linecolor='black', title='company'),
    yaxis=dict(gridcolor='rgba(0,0,0,0)', linecolor='black', title='timeline', range=(dates_academic[0], dates_df_b2b[1])),
)


with open('plotly_figures/experience_figure.html', 'w', encoding='UTF-8') as file:
    file.write(fig.to_html())