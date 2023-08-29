import plotly.graph_objects as go
import pandas as pd

class TeamExpertiseTreemap:
    def __init__(self, data_file):
        self.df = pd.read_excel(data_file)
        self.color_scale = {
            'White': 'rgb(255, 255, 255)',
            'Light Green': 'rgb(173, 255, 47)',
            'One level above light green': 'rgb(0, 255, 0)',
            'Two levels above light green': 'rgb(0, 128, 0)',
            'Two levels below dark green': 'rgb(0, 32, 0)',
            'One level below dark green': 'rgb(0, 100, 0)',
            'Dark Green': 'rgb(0, 64, 0)',
        }
        self.df['Color'] = self.df['Average Team Expertise(1-5)'].map(self.color_scale)

    def create_treemap(self):
        treemap_figure = go.Figure(go.Treemap(
            labels=self.df.apply(lambda row: f'{row["Area"]} ({row["Existing Team Members Proficient with this area"]})', axis=1),
            parents=['' for _ in self.df['Area']],
            values=self.df['Existing Team Members Proficient with this area'],
            customdata=self.df['Color'],
            hovertemplate='<b>Area:</b> %{label}<br><b>Team Size:</b> %{value}<br>',
            marker=dict(
                colorscale=['white', 'rgb(173, 255, 47)', 'rgb(0, 255, 0)', 'rgb(0, 128, 0)', 'rgb(0, 100, 0)', 'rgb(0, 64, 0)', 'rgb(0, 32, 0)'],
            ),
        ))

        treemap_figure.update_layout(
            title='Team Expertise Treemap',
        )

        return treemap_figure

    def show_treemap(self):
        treemap_fig = self.create_treemap()
        treemap_fig.show()

if __name__ == "__main__":
    expertise_treemap = TeamExpertiseTreemap('Aug Task 9 Excel.xlsx')
    expertise_treemap.show_treemap()
