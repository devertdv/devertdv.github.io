from dash import html
import dash_bootstrap_components as dbc


homepage_layout = html.Div(
    [
        html.H1("Welcome"),
        html.H2("Некоторая приветственная речь и объяснение, как что и куда жмать"),
        dbc.Nav(
            [
                html.Div(
                    [
                        dbc.NavLink("Общая информация по научной области", href="/general_info", active="exact"),
                        html.P("Тут тоже какой то небольшой текст про то, что будет в разделе \"Общая информация по научной области\"")
                    ],
                    style={
                                "border-radius": "5px",
                                "background-color": "#f9f9f9",
                                "margin": "10px",
                                "padding": "15px",
                                "position": "relative",
                                "box-shadow": "2px 2px 2px lightgrey",
                            },
                ),
                html.Div(
                    [
                        dbc.NavLink("Инфографика по наиболее релевантным статьям", href="/top_relevant", active="exact"),
                        html.P("Тут тоже какой то небольшой текст про то, что будет в разделе \"Инфографика по наиболее релевантным статьям\"")
                    ],
                    style={
                                "border-radius": "5px",
                                "background-color": "#f9f9f9",
                                "margin": "10px",
                                "padding": "15px",
                                "position": "relative",
                                "box-shadow": "2px 2px 2px lightgrey",
                            },
                ),
            ],
            style={
                "display": "flex",
            }
        )
    ],
    style={
        "margin": "auto",
        "width": "50%",
        "padding": "10px",
    }
)
