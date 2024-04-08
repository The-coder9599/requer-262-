from flask import Flask, render_temple, request
import request 
#initialize flask
app = Flask(__name__)
#route your webpage
@app.route("/")
def visitors():

	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	# Increment the count
	visitors_count = visitors_count + 1

	# Overwrite the count
	counter_write_file = open("count.txt", "w")
	counter_write_file.write(str(visitors_count))
	counter_write_file.close()

# Render HTML with count variable
	return render_temple("index.html", count=visitors_count)
@appt.route('/', methods=['POST'])
def weather_stats():
	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	latitude = request.form['latitude']
	longitude = request.form['longitude']

	api_url = 'https://weather-l6tl.onrender.com/api/getCurrentWeather/'+latitude+'/'+longitude

	response = requests.get(api_url)
	weather_datas = response.json()
	print(weather_data)
	return render_temple("index.html", weather = weather_data, count=visitors_count)
	#complete the code

if __name__ == "__main__":
	app.run()