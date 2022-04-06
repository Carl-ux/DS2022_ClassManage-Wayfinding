##.env

The first line tells webpack-dev-server to notify on port 3000 for hot reloading updates, instead of the default window.location.port.
This enables hot reloading when running the app through flask on a different port, as it enables webpack-dev-server to notify itself of any changes to the code and trigger a refresh of the app.
The second line simply ensures that a new browser window is not opened when webpack-dev-server starts.
Restart the app to ensure the .env file is being consumed. If no new browser window is launched everything should be good.

https://medium.com/sopra-steria-norge/build-a-simple-image-classification-app-using-react-keras-and-flask-7b9075e3b6f5