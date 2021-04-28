'''
#############################################################################################
#*******************************************************************************************#
#           Copyright (c) 2020 pyCoder|semih Corporation;) All rights reserved.            ##
#                                   [Timestamp:20210420]                                   ##
#*******************************************************************************************#
#############################################################################################
'''

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Output, Input, State
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import psycopg2
import pandas.io.sql as sqlio

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

##### Database queryleri ve sonuclari

conn = psycopg2.connect("dbname=dvd_rental user=postgres password=Fsm1453.")
cur = conn.cursor()
cur.execute("select count(*) from my_dbproject")
a=cur.fetchone()             # bu metod tuple return ediyor. cursor.rowcount() kullanilirsa integer return ediyor.

cur.execute("select count(*) from film")
b=cur.fetchone()

cur.execute("select count(*) from category")
c=cur.fetchone()

cur.execute("select count(*) from country")
d=cur.fetchone()
########################################################################
cur.execute("select count(*) from film_category where category_id=1")
e=cur.fetchone()

cur.execute("select count(*) from film_category where category_id=2")
f=cur.fetchone()

cur.execute("select count(*) from film_category where category_id=3")
g=cur.fetchone()

cur.execute("select count(*) from film_category where category_id=4")
h=cur.fetchone()

cur.execute("select count(*) from film_category where category_id=5")
j=cur.fetchone()

cur.execute("select count(*) from film_category where category_id=6")
k=cur.fetchone()

cur.execute("select count(*) from film_category where category_id=7")
l=cur.fetchone()

cur.execute("select count(*) from film_category where category_id=8")
m=cur.fetchone()

cur.execute("select count(*) from film_category where category_id=9")
n=cur.fetchone()

cur.execute("select count(*) from film_category where category_id=10")
v=cur.fetchone()

cur.execute("select count(*) from customer where active=1")
customer_a = cur.fetchone()

cur.execute("select count(*) from customer where active=0")
customer_i = cur.fetchone()

tot = customer_a+customer_i # tuple donuyor
totl=list(tot)

total=e+f+g+h+j+k+l+m+n+v
s=sum(list(total))
r=[]
for i in total:
    r.append(round((100/s)*i))

cur.close()
conn.commit()
conn.close()

# Use the hovertext kw argument for hover text
fig = go.Figure(
    data=[go.Bar(x= ['Action','Animation','Children','Classics','Comedy','Documentary','Drama','Family','Foreign','Games'],
                 y=[r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9]])]

)

# Customize aspect
fig.update_traces(marker_color='rgb(97, 185, 231)',
                  marker_line_color='rgb(97, 185, 231)')

fig.update_layout(title_text='Categories & Number of Movies',
                  height= 300,
                  paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  bargap=0.45,
                  font_color="white",
                  yaxis=dict(
                      tickfont_size=12,
                    ),
                  xaxis=dict(
                      tickfont_size=7,
                      tickangle=40,
                  ),
                  margin=dict(l=50, r=0, b=50, t=100)
                  )

fig.update_yaxes(showgrid=True,
                 gridwidth=1,
                 gridcolor='DarkBlue')

# Use `hole` to create a donut-like pie chart
fig2 = go.Figure(data=[go.Pie(labels=['Active','Inactive'],
                              values=[totl[0],totl[1]],
                              hole=.8)])
fig2.update_traces(marker=dict(colors=['rgb(255 ,165, 0)',
                                       'rgb(255, 0, 0)'])),
fig2.update_layout(title_text='Active-Inactive Customers',
                  height= 350,
                  paper_bgcolor = 'rgba(0,0,0,0)',
                  plot_bgcolor = 'rgba(0,0,0,0)',
                  font_color = "white",
                  margin = dict(l=0, r=0, b=100, t=100)
                  )


app.layout = html.Div([
                dbc.Row(
                    dbc.Col([
############################################################## 1st Part
                        dbc.Row(
                            dbc.Col([
                                dbc.NavbarSimple(
                                    children=[
                                        dbc.NavItem(dbc.NavLink("ACTION", href="/action")),
                                        dbc.NavItem(dbc.NavLink("ANIMATION", href="/animation")),
                                        dbc.NavItem(dbc.NavLink("CHILDREN", href="/children")),
                                        dbc.NavItem(dbc.NavLink("CLASSICS", href="/classics")),
                                        dbc.NavItem(dbc.NavLink("COMEDY", href="/comedy")),
                                        dbc.NavItem(dbc.NavLink("DOCUMENTARY", href="/documentary")),
                                        dbc.NavItem(dbc.NavLink("DRAMA", href="/drama")),
                                        dbc.NavItem(dbc.NavLink("FAMILY", href="/family")),
                                        dbc.NavItem(dbc.NavLink("FOREIGN", href="/foreign")),
                                        dbc.NavItem(dbc.NavLink("GAMES", href="/games")),
                                        dbc.NavItem(dbc.NavLink("HORROR", href="/horror")),
                                        dbc.DropdownMenu(
                                        [dbc.DropdownMenuItem("MUSIC", href="/music"),
                                         dbc.DropdownMenuItem("NEW", href="/new"),
                                         dbc.DropdownMenuItem("SCI-FI", href="/sci-fi"),
                                         dbc.DropdownMenuItem("SPORTS", href="/sports"),
                                         dbc.DropdownMenuItem("TRAVEL", href="/travel")],
                                        label="MORE...",
                                        nav=True,

                                    ),

                                    ],
                                    brand="FILM S T O R E",
                                    brand_href="/home",
                                    id='nav',
                                ),
                                html.P("Semih's Dashboard", id='name',style={'marginBottom':0,'marginLeft':100,'margin-top': 1})
                            ]),
                        ),
############################################################## 2nd Part
                        dbc.Row([
                            dbc.Col([
                                dbc.Row([
                                    dbc.Col([
                                        html.P('Customers'),  # sol ust tablo, sol ust veri
                                        html.H3(a)
                                    ], width=5),
                                    dbc.Col([
                                        html.P('Films'),     # sol ust tablo, sag ust
                                        html.H3(b)
                                    ], width=5)
                                ],id='first', justify='center'),
                                dbc.Row([
                                    dbc.Col([
                                        html.P('Categories'), # sol ust tablo, sol alt veri
                                        html.H3(c)
                                    ], width=5),
                                    dbc.Col([
                                        html.P('Countries'), # sol ust tablo, sag alt veri
                                        html.H3(d)
                                    ], width=5)
                                ],id='second',justify='center')
                            ],id='first-middle', width=4
                            ),
                            dbc.Col(
                                dcc.Graph(
                                    id ='graph',
                                    figure = fig
                                ),width=4, id='second-middle',align='center'
                            ),
                            dbc.Col(
                                dcc.Graph(
                                    id='graph2',
                                    figure= fig2,
                                ), width=4, id='third-middle')
                        ],id='graphs'
                        ),
############################################################## 3rd Part
                        dbc.Row([
                            dbc.Col(dbc.Input(id="customer_id", placeholder="Customer ID", type="number")),
                            dbc.Col(dbc.Input(id="first_name", placeholder="First Name", type="text")),
                            dbc.Col(dbc.Input(id="last_name", placeholder="Last Name", type="text")),
                            dbc.Col(dbc.Input(id="email", placeholder="e-mail", type="text")),
                            ], className="mt-3", justify='center'),

                        # dbc.Row(
                        #
                        #     dbc.Col(id='table', width=12
                        #     ), className="mt-3", justify='center'
                        # ),

                        dbc.Row(
                            dbc.Col([
                                dbc.Button('Show', id='show', n_clicks=0),
                                dbc.Button('Add', id='add', n_clicks=0),
                                dbc.Button('Update', id='update', n_clicks=0),
                                dbc.Button('Delete', id='delete', n_clicks=0),
                            ], width=4), className="mt-3", justify='center'
                        ),html.Div(id='place')
                    ]), id='middle'

              ),

            ], id='main-page')

# Callback func. ##############################################################

@app.callback(
    Output(component_id='place', component_property='children'),

    [Input(component_id='show', component_property='n_clicks'),
    Input(component_id='add', component_property='n_clicks'),
    Input(component_id='delete', component_property='n_clicks'),
    Input(component_id='update', component_property='n_clicks')],

    [State(component_id='customer_id', component_property='value'),
     State(component_id='first_name', component_property='value'),
     State(component_id='last_name', component_property='value'),
     State(component_id='email', component_property='value')]
    )

def save(n_clicks1, n_clicks2, n_clicks3, n_clicks4, value1, value2, value3, value4):
    ctx = dash.callback_context
    pie = ctx.triggered[0]['prop_id'].split('.')[0]

    if pie == 'show':
        conn = psycopg2.connect("dbname=dvd_rental user=postgres password=Fsm1453.")
        sql = "select customer_id,first_name,last_name,email from my_dbproject order by first_name LIMIT 3;"
        dat = sqlio.read_sql_query(sql, conn)
        conn.close()

        return dash_table.DataTable(
            id='table_ratio',
            data=dat.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in dat.columns],
            style_cell={'textAlign': 'center', 'width': '100px', 'minWidth': '100px', 'maxWidth': '100px'},
            fixed_rows={'headers': True, 'data': 0},
            style_header={'fontWeight': 'bold'},
            style_table={'overflowX': 'auto'},
            editable=True
        )

    elif pie =='add':
        conn = psycopg2.connect("dbname=dvd_rental user=postgres password=Fsm1453.")
        cur = conn.cursor()
        cur.execute('INSERT INTO my_dbproject VALUES(%s,%s,%s,%s)', (value1,value2,value3,value4))
        sql = "select customer_id,first_name,last_name,email from my_dbproject;"
        dat = sqlio.read_sql_query(sql, conn)
        cur.close()
        conn.commit()
        conn.close()

        return dash_table.DataTable(
            id='table_ratio',
            data=dat.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in dat.columns],
            style_cell={'textAlign': 'center', 'width': '100px', 'minWidth': '100px', 'maxWidth': '100px'},
            fixed_rows={'headers': True, 'data': 0},
            style_header={'fontWeight': 'bold'},
            style_table={'overflowX': 'auto'},
            editable=True
        )

    elif pie == 'delete':

        conn = psycopg2.connect("dbname=dvd_rental user=postgres password=Fsm1453.")
        cur = conn.cursor()
        cur.execute("DELETE FROM my_dbproject WHERE customer_id = %s", (value1,))
        sql = "select customer_id,first_name,last_name,email from my_dbproject;"
        dat = sqlio.read_sql_query(sql, conn)
        cur.close()
        conn.commit()
        conn.close()

        return dash_table.DataTable(
            id='table_ratio',
            data=dat.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in dat.columns],
            style_cell={'textAlign': 'center', 'width': '100px', 'minWidth': '100px', 'maxWidth': '100px'},
            fixed_rows={'headers': True, 'data': 0},
            style_header={'fontWeight': 'bold'},
            style_table={'overflowX': 'auto'},
            editable=True
        )

    elif pie == 'update':

        conn = psycopg2.connect("dbname=dvd_rental user=postgres password=Fsm1453.")
        cur = conn.cursor()
        cur.execute('UPDATE my_dbproject SET first_name=%s WHERE customer_id=%s', (value2,value1))
        sql = "select customer_id,first_name,last_name,email from my_dbproject;"
        dat = sqlio.read_sql_query(sql, conn)
        cur.close()
        conn.commit()
        conn.close()

        return dash_table.DataTable(
                id='table_ratio',
                data=dat.to_dict('records'),
                columns=[{'id': c, 'name': c} for c in dat.columns],
                style_cell={'textAlign': 'center', 'width': '100px', 'minWidth': '100px', 'maxWidth': '100px'},
                fixed_rows={'headers': True, 'data': 0},
                style_header={'fontWeight': 'bold'},
                style_table={'overflowX': 'auto'},
                editable=True
            )

if __name__ == '__main__':
    app.run_server(debug=True)