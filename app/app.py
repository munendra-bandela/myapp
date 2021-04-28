import flask
from flask import Flask, request, jsonify, render_template


app=Flask(__name__)
app.config["DEBUG"] = True


# Creating test data for the books catalog
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]



@app.route('/', methods=['GET'])
def home():
	return render_template('index.html')


# API to return all available books catalog
@app.route('/api/v1/books/all', methods=['GET'])
def all_books():
	"""API to return all available books catalog"""
	return jsonify(books)


#API to return book details by ID
@app.route('/api/v1/books', methods=['GET'])
def bookinfo():
	print("Filter by", request.args)
	if 'id' in request.args:
		id = int(request.args['id'])
	else:
		return "Error: No id filed provided. Please specify an id."
	records = list(filter(lambda record: record['id'] == id, books))
	print("Returning records: ", records)
	return jsonify(records)

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")
