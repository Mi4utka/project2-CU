from flask import Flask, render_template, request
from stuff.weather import get_data, normalize_data
from stuff.badweather import check_bad_weather

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def occ():
    if request.method == "POST":
        try:
            # Получение координат начальной и конечной точек
            start_lat = request.form.get("start_lat", type=float)
            start_lon = request.form.get("start_lon", type=float)
            end_lat = request.form.get("end_lat", type=float)
            end_lon = request.form.get("end_lon", type=float)

            raw_start_weather = get_data(start_lat, start_lon)
            raw_end_weather = get_data(end_lat, end_lon)

            start_weather = normalize_data(raw_start_weather)
            end_weather = normalize_data(raw_end_weather)
            
            # Анализ погоды
            start_result = check_bad_weather(start_weather)
            end_result = check_bad_weather(end_weather)

            # Передача данных в шаблон
            return render_template(
                "res.html", 
                start_weather=start_weather, 
                start_result=start_result,
                end_weather=end_weather, 
                end_result=end_result
            )
        except Exception as e:
            return render_template("err.html", error=str(e)), 500
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)