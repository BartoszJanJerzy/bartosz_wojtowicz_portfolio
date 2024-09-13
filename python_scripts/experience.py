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


def add_trace(label: str, name: str, values, color: str):
    fig.add_trace(go.Scatter(
        name=name,
        y=[label, label],
        x=values,
        mode='lines',
        line=dict(width=20),
        marker_color=color
    ))


colors = [
    'rgb(169, 214, 229)',
    'rgb(137, 194, 217)',
    'rgb(97, 165, 194)',
    'rgb(70, 143, 175)',
    'rgb(44, 125, 160)',
    'rgb(42, 111, 151)',
    'rgb(1, 79, 134)',
    'rgb(1, 73, 124)',
]


fig = go.Figure()

add_trace('Academic Work - PhD', f'PhD', dates_academic, colors[0])
add_trace('Flow Research Center - Jr Researcher', f'Junior Researcher', dates_flow, colors[1])
add_trace('Asseco Business Solutions - Jr Data Scientist', f'Jr Data Scientist', dates_abs, colors[2])
add_trace('WeSub - Data Scientist', f'Data Scientist', dates_wesub, colors[3])
add_trace('Playstrict - Data Scientist (side project)', f'Data Scientist (side project)', dates_playstrict_side, colors[4])
add_trace('DigitalFirst - Data Scientist (side project)', f'Data Scientist (side project)', dates_df_side, colors[5])
add_trace('Essyo - Data Scientist (side project)', f'Data Scientist (side project)', dates_essyo_side, colors[6])
add_trace('DigitalFirst - Senior Data Scientist (current)', f'Senior Data Scientist (current)', dates_df_b2b, colors[7])

fig.add_trace(
    go.Scatter(
        x=[dates_abs[0], dates_abs[0]],
        y=['Academic Work - PhD', 'DigitalFirst - Senior Data Scientist (current)'],
        mode='lines+text',
        text=['', 'Here I changed my career to IT'],
        textposition='top right',
        marker_color='rgb(187, 68, 48)'
    )
)

fig.update_layout(
    title=title,
    width=1600,
    height=600,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    yaxis=dict(gridcolor='rgba(217, 217, 217, 0.5)', linecolor='rgba(0,0,0,0)'),
    xaxis=dict(gridcolor='rgba(0,0,0,0)', linecolor='rgba(0,0,0,0)', title='timeline', range=(dates_academic[0], dates_df_b2b[1])),
    font=dict(color='rgb(217, 217, 217)', family='Verdana'),
    showlegend=False
)


with open('assets/experience_figure.html', 'w', encoding='UTF-8') as file:
    file.write(fig.to_html())