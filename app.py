import dash

app = dash.Dash()
server = app.server
app.config.suppress_callback_exceptions = True

app.css.append_css({"external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"})