from flask import Flask, render_template, url_for
from flask import request, flash
import time

# weather_report() returns a dictionary with weather data
from weather_details import weather_report

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == "POST":
        city = request.form.get("city")
        if city == "":
            return "<h2>Please enter a city</h2>"
        secs = time.time()
        current_time = time.ctime(secs)
        # extracting only the day of the week, month and year from current_time
        ctime = {"date":current_time[:11],"year":current_time[-4:]}
        weather_data = weather_report(city)
        weather_description = weather_data["desc"]
        # if weather_description == "Clouds":
        #     weather_logo = "scattered_clouds"
        # else:
        #     weather_logo = "clear_sky_day"
        return render_template("weather.html", ctime = ctime,
        weather_data = weather_data)

    return render_template("homepage.html")



if __name__ == "__main__":
    app.run(debug = True, port = 8080)
