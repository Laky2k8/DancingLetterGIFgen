from PIL import Image, ImageSequence

def merge_gif_frames(gif_paths, max_width=None, bg_color=(255, 255, 255, 255)):
	"""Merge GIFs with wrapping: place them in rows, wrapping to a new line if max_width is exceeded."""
	gifs_data = []
	gif_size = 100

	for path in gif_paths:
		frames = []
		durations = []
		newline = False


		if "space" in path.lower():
			white_frame = Image.new('RGBA', (100, 100), bg_color)
			frames = [white_frame] * 10
			durations = [100] * 10
		elif "newline" in path.lower():

			newline = True

			# Dummy fames so the loop works lmao
			dummy_frame = Image.new('RGBA', (100, 100), bg_color)
			frames = [dummy_frame] * 10
			durations = [100] * 10


		else:
			im = Image.open(path)
			for frame in ImageSequence.Iterator(im):
				frame = frame.convert('RGBA')
				bg = Image.new('RGBA', frame.size, bg_color)
				bg.paste(frame, (0, 0), frame)
				frames.append(bg)
				durations.append(frame.info.get('duration', 100))

		gifs_data.append({
				'frames': frames, 
				'durations': durations,
				'is_newline': newline
			})

	max_frames = max(len(g['frames']) for g in gifs_data)
	target_height = max(frame.height for g in gifs_data for frame in g['frames'])

	merged_frames = []
	merged_durations = []

	for i in range(max_frames):
		resized_frames = []
		frame_durations = []

		for g in gifs_data:

			# Check for newlines
			if g.get('is_newline', False):
				resized_frames.append('NEWLINE')
				frame_durations.append(g['durations'][i % len(g['durations'])])
			else:
				frame = g['frames'][i % len(g['frames'])]
				dur = g['durations'][i % len(g['frames'])]
				w, h = frame.size
				new_w = int(w * target_height / h)
				frame = frame.resize((new_w, target_height), Image.LANCZOS)
				resized_frames.append(frame)
				frame_durations.append(dur)

		# Arrange frames into rows based on max_width
		rows = []
		current_row = []
		row_width = 0
		for f in resized_frames:

			if f == 'NEWLINE':
				# Create a new row
				if current_row:
					rows.append(current_row)
					current_row = []
					row_width = 0
				continue  # Don't add the newline marker to the actual row

			elif max_width and row_width + f.width > max_width and current_row:
				rows.append(current_row)
				current_row = []
				row_width = 0
			current_row.append(f)
			row_width += f.width

		if current_row:
			rows.append(current_row)

		# If we have no rows (that shouldn't happen lol) just make an empty row
		if not rows:
			rows = [[Image.new('RGBA', (1, target_height), bg_color)]]

		total_width = max(sum(f.width for f in row) for row in rows)
		total_height = len(rows) * target_height

		merged = Image.new('RGBA', (total_width, total_height), bg_color)
		y_offset = 0
		for row in rows:
			x_offset = 0
			for f in row:
				merged.paste(f, (x_offset, y_offset), f)
				x_offset += f.width
			y_offset += target_height

		merged_frames.append(merged)
		merged_durations.append(max(frame_durations))

	return merged_frames, merged_durations, len(rows)