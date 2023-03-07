import json
import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output

#reading the json file
with open("graph1_blogs_languages.json") as json_file:
    data = json.load(json_file)

df = pd.DataFrame(data=data)


#first graph - looking at the languages of the articles that i can access from twitch.blogs
graph1 = df.groupby("language")["language"].count().reset_index(name="articles")


#second graph - looking at the titles of the articles, and their diversity (only english)
df = df.drop("date", axis=1)

df["title"] = df["title"].str.lower()
df["keywords"] = df["title"].str.contains("twitch")

graph2 = df[df["language"] == "english"]
graph2 = graph2.groupby("keywords").count().reset_index()


#third graph - looking at which year from the english articles showed the most diversion in themes
df["key words"] = df["title"].str.contains("hispanic|asian|american|black|korean|african|heritage|history|women's|woman|female|girls|girl|representation|LGBTQIA+|pride|awareness|lesbians|gays|celebrate|celebrates|party|month|parties|season|holiday|holidays|valentine's|winter|summer|birthday|week|day|twitchcon|cosplay|contest|event|gamescon|tournament|win|awards|award|health|violence|security|accessibility|safety|policy|guidelines")
graph3 = df[df["language"] == "english"]
graph3 = graph3.groupby("year").sum().reset_index()


#getting csv together and making it ready to work with

folder_csv = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

empty_csv = []

for filename in folder_csv:
    a = pd.read_csv("csv/SullyGnome"+filename+".csv")
    empty_csv.append(a)

fourth_graph_data = pd.concat(empty_csv)

    # removing weird unnames
fourth_graph_data = fourth_graph_data.drop("Unnamed: 0", axis=1)
fourth_graph_data = fourth_graph_data.drop("Unnamed: 1", axis=1)
fourth_graph_data = fourth_graph_data.drop("Unnamed: 13", axis=1)


#fourth graph - looking at the streamers and their diversity, from the csv file
graph4 = fourth_graph_data.groupby("Language")["Language"].count().sort_values(ascending=False).reset_index(name="streamers")


#fifth and six graphs - looking at the top 100 most viewed streamers, and their differences in games, gender and language

exec(open("graph4_api.py").read())

graph56 = merged.groupby("games")["games"].count().sort_values(ascending=False).reset_index(name="streamers")

exec(open("graph4_api_female.py").read())

graph562 = merged2.groupby("games")["games"].count().sort_values(ascending=False).reset_index(name="streamers")


# some graph things

fig_graph1 = px.bar(graph1, x="language", y="articles")
fig_graph2 = px.bar(graph2, x="keywords", y="title", color="keywords")
fig_graph3 = px.line(graph3, x="year", y="key words")
fig_graph4 = px.bar(graph4, x="Language", y="streamers")
fig_graph5 = px.pie(graph56, values="streamers", names="games")
fig_graph6 = px.pie(graph562, values="streamers", names="games")


# make app to internet

app = dash.Dash()
app.layout = html.Div(children=[

    html.H4("Student: Anouk Vreeburg - Professor: Erik Hekman - Subject: Fundamentals of Data Science Blok A"),
    html.H1("Twitch Diversity Analysis"),
    html.H2("Twitch has had it's backlash of promoting mostly white males and not stopping hate raids against minorities. Around 2017, it arranged a team to combat these claims and to promote diversity on its platform. To test their success, we look at (1) how Twitch promotes diversity on their website, (2) how diverse the top 1000 streamers are and (3) how diverse their content is in range of games."),

    html.H3("With help of webscraping we can see how many articles are available on their website for each language"),
    html.Div([

        dcc.Graph(

        id="graph1",
        figure = fig_graph1

    )

    ], style={"width": "100%", "display": "inline-block"}),

    
    html.Div([

        html.H3("Next we look at the English articles and how many diverse keywords their titles possess"),

        dcc.Dropdown(

        id="select_platform2",
        options = [

            #learned | in value from: https://stackoverflow.com/questions/48631769/pandas-str-contains-search-for-multiple-values-in-a-string-and-print-the-value/48632835
            # i went through the articles to look for words that were used
            {"label": "culture (hispanic, asian, ...)", "value": "hispanic|asian|american|black|korean|african|heritage|history"},
            {"label": "minorities (female, LGBTQIA+, ...)", "value": "women's|woman|female|females|girls|girl|representation|LGBTQIA+|pride|awareness|lesbians|gays"},
            {"label": "holidays (holidays, seasons, ...)", "value": "celebrate|celebrates|party|month|parties|season|holiday|holidays|valentine's|winter|summer|birthday|week|day"},
            {"label": "tournaments (twitchCon, cosplay events, ...)", "value": "twitchcon|cosplay|contest|event|gamescon|tournament|win|awards|award"},
            {"label": "twitch community (partners, streamers, ...)", "value": "creator|creators|partners|members|play|developer|developers|community|friends|friend|player|streamer|streamers|players"},
            {"label": "games (games, league, ...)", "value": "games|game|gamers"},
            {"label": "safety (health, security, ...)", "value": "health|violence|security|accessibility|safety|policy|guidelines"}


        ],
        value="hispanic|asian|american|black|korean|african|heritage|history"

    ),

        dcc.Graph(

        id="select-graph2",
        figure = fig_graph2

    )

    ], style={"width": "50%", "display": "inline-block"}),

    html.Div([

        html.H3("Together these keywords come forth the most in these years (not including community and games keywords)"),

        dcc.Graph(

        id="graph3",
        figure = fig_graph3

    )

    ], style={"width": "50%", "display": "inline-block"}),

    html.H3("With the help of a CSV file we now look at the top 1000 most watched streamers of the last 365 days (taken on 8 nov) to learn more about them"),
    dcc.Dropdown(

        id="graph4_dropdown",
        options = [

            {"label": "spoken language", "value": "Language"},
            {"label": "maturnity streams", "value": "Mature"},
            {"label": "partnered with Twitch", "value": "Partnered"}

        ],
        value="Language"

    ), 

    dcc.Graph(

        id="select-graph4",
        figure = fig_graph4

    ),

    html.H3("Lastly, we look at the top 100 from above, males and females, with the help of an API (Get videos API from Twitch), we look at their last taken video (from 8 nov or further down) and its content"),

    html.Div([

        dcc.Dropdown(

        id="graph5_dropdown",
        options = [

            {"label": "males: recent played games", "value": "games"},
            {"label": "males: spoken language", "value": "language"},

        ],
        value="games"

    ),

        dcc.Graph(

        id="select-graph5",
        figure = fig_graph5

    )

    ], style={"width": "50%", "display": "inline-block"}),

    html.Div([

        dcc.Dropdown(

        id="graph6_dropdown",
        options = [

            {"label": "females: recent played games", "value": "games"},
            {"label": "females: spoken language", "value": "language"},

        ],
        value="games"

    ),

        dcc.Graph(

        id="select-graph6",
        figure = fig_graph6

    )

    ], style={"width": "50%", "display": "inline-block"})

])

@app.callback(

    Output("select-graph2", "figure"),
    Input("select_platform2", "value")

)

def update_figure(value):
    df["title"] = df["title"].str.lower()
    df["keywords"] = df["title"].str.contains(value)

    graph2 = df[df["language"] == "english"]
    graph2 = graph2.groupby("keywords").count().reset_index()
    fig_graph2 = px.bar(graph2, x="keywords", y="title", color="keywords")
    return fig_graph2

@app.callback(

    Output("select-graph4", "figure"),
    Input("graph4_dropdown", "value")

)

def update(value):

    graph4 = fourth_graph_data.groupby(value)[value].count().sort_values(ascending=False).reset_index(name="streamers")
    oi = px.bar(graph4, x=value, y="streamers")
    return oi


@app.callback(

    Output("select-graph5", "figure"),
    Input("graph5_dropdown", "value")

)

def update(value):

    graph56 = merged.groupby(value)[value].count().sort_values(ascending=False).reset_index(name="streamers")
    fig_graph5 = px.pie(graph56, values="streamers", names=value)
    return fig_graph5


@app.callback(

    Output("select-graph6", "figure"),
    Input("graph6_dropdown", "value")

)

def update(value):

    graph562 = merged2.groupby(value)[value].count().sort_values(ascending=False).reset_index(name="streamers")
    fig_graph6 = px.pie(graph562, values="streamers", names=value)
    return fig_graph6


if __name__ == "__main__":

    app.run_server(debug=False)