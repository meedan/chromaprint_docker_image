import acoustid
files = ["sample.wav","test_audio_1.mp3","test_audio_2.mp4"]

def audio_hasher(filename):
  try:
    return acoustid.chromaprint.decode_fingerprint(
      acoustid.fingerprint_file(filename)[1]
    )[0]
  except acoustid.FingerprintGenerationError:
    return []

hashes = [audio_hasher(filename) for filename in files]