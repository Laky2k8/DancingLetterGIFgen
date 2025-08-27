from flask import Flask, render_template, send_from_directory, send_file, Response, request, redirect
import os
from unidecode import unidecode
import gif_merge
from gif_merge import merge_gif_frames
import base64

app = Flask(__name__)


@app.route("/")
def default():
	return render_template("index.html")

@app.route("/word/")
def word_redirect():
	# Redirect to /
	return redirect("/")

@app.route("/word/<word>")
def generate_dancing_gif(word):

	# Get width 
	widthParam = request.args.get("width")
	if widthParam:
		try:
			width = int(widthParam)
		except ValueError:
			return "Invalid width parameter", 400
	else:
		# Default width
		width = 2000

	word_ascii = unidecode(word)

	path = "./dancing_letter_gifs"

	images = []
	gif_paths = []

	newline = False

	# For calculating gif sizing
	characters = 0
	newline_count = 0

	for letter in word_ascii:

		# Get letter file
		if letter.isalnum():
			letter = letter.upper()

			# newline
			if letter == "N" and newline:
				letter_path = f"newline"
				print("New line")
				newline_count += 1
				newline = False
			else:
				letter_path = f"dancing_{letter}.gif"
				print(letter_path)

		elif letter == " ":
			letter_path = "dancing_space.gif"
		elif letter == "&":
			letter_path = "dancing_and.gif"
		elif letter == "@":
			letter_path = "dancing_at.gif"
		elif letter == "$":
			letter_path = "dancing_dollar.gif"
		elif letter == "?":
			letter_path = "dancing_question.gif"
		elif letter == "!":
			letter_path = "dancing_exclamation.gif"

		# newline
		elif letter == "\\":
			newline = True
			continue

		else:
			continue

		if os.path.exists(path):

			if letter_path == "newline":
				images.append(f"/img/dancing_space.gif")
				gif_paths.append("newline")
			else:
				images.append(f"/img/{letter_path}")
				gif_paths.append(os.path.join(path, letter_path))



	# Merge GIFs
	try:
		merged_path = None
		if gif_paths:
			merged_frames, merged_durations, total_rows = merge_gif_frames(gif_paths, max_width=width)

			merged_filename = f"{word}.gif"
			# Clean merged_filename from special characters
			merged_filename = ''.join(c for c in merged_filename if c.isalnum() or c in (' ', '.', '_')).rstrip()

			# Edge case if filename is empty (only special characters for example)
			if merged_filename == ".gif":
				merged_filename = "generated.gif"

			merged_path = os.path.join(path, merged_filename)
			merged_frames[0].save(
				merged_path,
				save_all=True,
				append_images=merged_frames[1:],
				duration=merged_durations,
				loop=0,
				disposal=2,  # overwrite previous frame
			)

		gif_dataURI = f"data:image/gif;base64,{base64.b64encode(open(merged_path, 'rb').read()).decode('utf-8')}" if merged_path else None

		return render_template("word.html", word=word, filename=merged_filename, images=images, merged=gif_dataURI, row_count=total_rows)

	finally:
		# Remove merged GIFs after serving
		if merged_path and os.path.exists(merged_path):
			os.remove(merged_path)
	
	
	# return images


	#return render_template("index.html", word=word)


@app.route('/img/<path:filename>') 
def send_file(filename): 
	return send_from_directory("./dancing_letter_gifs/", filename)

@app.route('/static/<path:filename>')
def send_static_file(filename):
	return send_from_directory("static", filename)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')