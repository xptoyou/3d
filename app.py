from flask import Flask, render_template, request, send_file
import magenta
from magenta.models.music_rnn import music_rnn
from magenta.music import note_sequence_io
import tensorflow as tf

app = Flask(__name__)

# Load the pre-trained model
model_name = 'basic_rnn'
bundle = music_rnn.read_bundle_file('basic_rnn.mag')  # Make sure this path is correct
generator = music_rnn.MusicRNNModel(bundle)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_music():
    num_steps = int(request.form.get('num_steps', 64))
    sequence = generator.generate(num_steps=num_steps, temperature=1.0)

    # Save the generated sequence to a MIDI file
    midi_file_path = 'generated_music.mid'
    note_sequence_io.note_sequence_to_midi_file(sequence, midi_file_path)

    return send_file(midi_file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

